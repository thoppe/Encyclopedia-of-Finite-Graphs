import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from helper_functions import load_graph_database, grab_scalar

desc   = "Verify the sequences produced are the correct ones"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--max_n',type=int,default=9,
                    help="Maximum graph size n to compute tests")
parser.add_argument('--min_n',type=int,default=2,
                    help="Minimum graph size n to match tests")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)

graph_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"]+1):
    graph_conn[n] = load_graph_database(n)

# Assume that ref's are the same for all DB's
cmd = '''SELECT invariant_id,function_name FROM ref_invariant_integer'''
invariant_list = graph_conn[1].execute(cmd).fetchall()
invariant_dict = dict(invariant_list)

f_known_sequence = "verification/known.txt"
f_report = "verification/report.md"
F_REPORT = open(f_report,'w')

msg = "## Unit tests for N={{3, ..., {max_n}}}\n\n"
F_REPORT.write(msg.format(**cargs))


cmd_count = '''
SELECT COUNT(*) FROM invariant_integer as a 
LEFT JOIN ref_invariant_integer as b
ON  a.invariant_id  = b.invariant_id 
WHERE b.function_name = "{function_name}"
AND   a.value {conditional} {value}
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
    #args["check_seq"] = args['seq'][n0:n1]
    #args["database_seq"] = grab_sequence(**args)[::args["skip"]]

    args["check_seq"] = args['seq'][n0:n1]
    args["database_seq"] = grab_sequence(**args)[n0:n1]   

    # Check and record the match
    args["status"] = args["check_seq"] == args["database_seq"]
    return args


fail_msg = '''
**FAILED**  : `{function_name}{conditional}{value}`
OEIS        : [`{check_seq}`]({comment})
received    : `{database_seq}`\n'''.lstrip()

pass_msg = '''
*passed*  : `{function_name}{conditional}{value}`
OEIS      : [`{check_seq}`]({comment})
received  : `{database_seq}`\n'''.lstrip()

def report_seq(**args):
    if args["status"]:
        s = pass_msg.format(**args)
        sp = "passed {function_name}{conditional}{value}".format(**args)
    else:
        s = sp = fail_msg.format(**args)

    F_REPORT.write(s+'\n\n')
    print sp

def parse_known_sequence(line):
    info, seq = line.split('|')

    key_names = ["function_name","conditional","value"]
    info = [key_names,info.strip().split(' ')]
    args = dict(zip(*info))

    seq = seq.strip()
    if seq:
        seq = map(int, seq.split(','))
        args['seq'] = seq
    else:
        args['seq'] = []

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
