import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
import helper_functions

desc   = "Verify the sequences produced are the correct ones"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--max_n',type=int,default=8,
                    help="Maximum graph size n to compute tests")
parser.add_argument('--min_n',type=int,default=3,
                    help="Minimum graph size n to match tests")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)

graph_conn = collections.OrderedDict()
for n in range(cargs["min_n"], cargs["max_n"]+1):
    graph_conn[n] = helper_functions.load_graph_database(n)

# Assume that ref's are the same for all DB's
cmd = '''SELECT invariant_id,function_name FROM ref_invariant_integer'''
invariant_list = graph_conn[cargs["min_n"]].execute(cmd).fetchall()
invariant_dict = dict(invariant_list)

def grab_vector(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()]

def grab_scalar(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()][0]

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
    args["check_seq"] = args['seq'][n0-1:n1]
    args["database_seq"] = grab_sequence(**args)

    # Check and record the match
    args["status"] = args["check_seq"] == args["database_seq"]
    return args

def report_seq(**args):
    if args["status"]:
        print "GOOD"
    else:
        msg = '''
        FAILED  : {function_name}{conditional}{value}
        expected: {check_seq}
        received: {database_seq}'''
        print msg.rstrip().format(**args)
    


f_known_sequence = "src/verify_seq/known.txt"

def parse_known_sequence(line):
    info, seq = line.split('|')
    seq = map(int, seq.split(','))
    key_names = ["function_name","conditional","value"]

    info = [key_names,info.strip().split(' ')]
    args = dict(zip(*info))
    args['seq'] = seq
    return args

with open(f_known_sequence) as FIN:
    for line in FIN:
        line = line.strip()
        if line and line[0] != "#":

            try: seq_args = parse_known_sequence(line)
            except Exception as ex:
                err = "Error parsing unit_test line: %s\n%s"%(line,ex)
                raise SyntaxError(err)
          
            seq_args = test_seq(**seq_args)
            report_seq(**seq_args)


#print grab_sequence(function_name="automorphism_group_n", value=2)
