import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from helper_functions import load_graph_database, grab_scalar
from helper_functions import attach_ref_table
import pyparsing as pypar

desc   = "Verify the sequences produced are the correct ones"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--max_n',type=int,default=10,
                    help="Maximum graph size n to compute tests")
parser.add_argument('--min_n',type=int,default=3,
                    help="Minimum graph size n to match tests")
parser.add_argument('--skip_check_complete',default=False,
                    action="store_true",
                    help="Skip the check on completeness")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)

graph_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"]+1):
    graph_conn[n] = load_graph_database(n)
    attach_ref_table(graph_conn[n])

# Assume that ref's are the same for all DB's
cmd = '''SELECT invariant_id,function_name FROM ref_invariant_integer'''
invariant_list = graph_conn[1].execute(cmd).fetchall()
invariant_dict = dict(invariant_list)

f_known_sequence = "verification/known.txt"
f_report = "verification/report.md"
F_REPORT = open(f_report,'w')

msg = "## Unit tests for N={{{min_n}, ..., {max_n}}}\n\n"
F_REPORT.write(msg.format(**cargs))


# Make sure that all invariants have the proper number of terms
cmd_count_terms = '''
SELECT invariant_id,COUNT(*) FROM invariant_integer
GROUP BY invariant_id'''

# Taken from OEIS A001349, starting at n=0 to n=13
expected_counts = [1, 1, 1, 2, 6, 21, 112, 853, 
                   11117, 261080, 11716571, 1006700565, 
                   164059830476, 50335907869219]

msg_incomplete = '''
**MISSING**     : `{function_name}` at n={n}
expected/received : `{expected_counts}`, `{received_counts}`\n'''.lstrip()

if not cargs["skip_check_complete"]:

    for n in graph_conn:
        logging.info("Checking for complete terms n=%i"%n)
        cursor = graph_conn[n].execute(cmd_count_terms)
        ex = expected_counts[n]
        for invariant_id,count in cursor.fetchall():
            if ex!=count:
                msg_args = {"function_name":invariant_dict[invariant_id]}
                msg_args["n"] = n
                msg_args["expected_counts"]=ex
                msg_args["received_counts"]=count
                msg = msg_incomplete.format(**msg_args)
                F_REPORT.write(msg+'\n\n')
                print msg

cmd_count = '''
SELECT COUNT(*) FROM invariant_integer as a 
LEFT JOIN ref_invariant_integer as b
ON  a.invariant_id  = b.invariant_id 
WHERE b.function_name = "{function_name}" 
AND a.value {conditional} {value}
'''

def grab_sequence(**args):
    cmd = cmd_count.format(**args)

    vec = []
    for n in graph_conn:
        sol = grab_scalar(graph_conn[n], cmd)
        vec.append(sol)

    return vec

def test_seq(**args):
    n0,n1 = cargs["min_n"],cargs["max_n"]
    n0 -= 1

    args["check_seq"] = args['seq'][n0:n1]
    args["database_seq"] = grab_sequence(**args)[n0:n1]   

    # Check and record the match
    args["status"] = args["check_seq"] == args["database_seq"]
    return args


fail_msg = '''
**FAILED**  : `{function_name}{conditional}{value}`
OEIS        : [`{check_seq}`]({comment})
received    :  `{database_seq}`\n'''.lstrip()

pass_msg = '''
*passed*  : `{function_name}{conditional}{value}`
OEIS      : [`{check_seq}`]({comment})
received  :  `{database_seq}`\n'''.lstrip()

def report_seq(**args):
    if args["status"]:
        s = pass_msg.format(**args)
        sp = "passed {function_name}{conditional}{value}".format(**args)
    else:
        s = sp = fail_msg.format(**args)

    F_REPORT.write(s+'\n\n')
    print sp


# Extra tests (for now done by hand)
# oeis.org/A002851
cmd_special = '''
SELECT * FROM invariant_integer as X WHERE X.graph_id IN 
(
SELECT graph_id FROM invariant_integer as a 
LEFT JOIN ref_invariant_integer as b
ON  a.invariant_id  = b.invariant_id 
WHERE b.function_name = "is_k_regular" 
AND a.value=3
) AND X.invariant_id=7
'''
#for n in graph_conn:
#    logging.info("Checking special")
#    cursor = graph_conn[n].execute(cmd_special)
#    for adj in cursor.fetchall():
#        print adj
#exit()    


operators = [">", "<", "is not", ">=", "<=", "="]
gmr_conditional = pypar.Or(map(pypar.Keyword, operators))("conditional")
gmr_seqname  = pypar.Word(pypar.alphanums + "_")("function_name")
gmr_value    = pypar.Word(pypar.nums)("value")
gmr_phrase   = pypar.Group(gmr_seqname + gmr_conditional + gmr_value)

gmr_seq_sep  = pypar.Keyword("|").suppress()
gmr_seq      = pypar.Group(pypar.commaSeparatedList)
gmr_full     = gmr_phrase("phrase") + gmr_seq_sep + gmr_seq("seq")

def parse_known_sequence(line):
   
    sol  = gmr_full.parseString(line)

    args = {}
    try:    args['seq']  = map(int, sol["seq"])
    except: args['seq'] = []

    args.update( sol["phrase"].asDict() )

    return args

previous_comment = ''

with open(f_known_sequence) as FIN:  

    for line in FIN:
        line = line.strip()

        if line and line[0] == "#":
            previous_comment = line[1:].strip()

        if line and line[0] != "#":

            try: seq_args = parse_known_sequence(line)
            except Exception as ex:
                err = "Error parsing unit_test line: %s\n%s"%(line,ex)
                raise SyntaxError(err)

            seq_args['comment'] = previous_comment
          
            seq_args = test_seq(**seq_args)
            report_seq(**seq_args)

F_REPORT.close()


