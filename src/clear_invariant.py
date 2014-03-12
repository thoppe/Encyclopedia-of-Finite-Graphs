import sqlite3, logging, argparse, os, collections, ast
import subprocess
import numpy as np
import helper_functions
#from src.invariants import graph_tool_representation, convert_to_numpy
import graph_tool

desc   = "Remove an invariant calculation from the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('function_name',type=str)
parser.add_argument('--max_n',type=int,default=10,
                    help="Maximum graph size n to remove invariant")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

graph_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"]+1):
    graph_conn[n] = helper_functions.load_graph_database(n)

def grab_scalar(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()][0]

cmd_find_id = '''
SELECT invariant_id from ref_invariant_integer 
WHERE function_name = "{function_name}" '''.format(**cargs)

cmd_remove_from_ref = '''
DELETE FROM ref_invariant_integer
WHERE function_name = "{function_name}" '''.format(**cargs)

cmd_remove_from_invariants = '''
DELETE FROM invariant_integer
WHERE invariant_id = "{invariant_id}" '''

for n in graph_conn:
    conn = graph_conn[n]
    cargs["invariant_id"] = grab_scalar(conn, cmd_find_id)

    conn.execute(cmd_remove_from_ref.format(**cargs))
    conn.execute(cmd_remove_from_invariants.format(**cargs))
    conn.commit()

    msg = "Remove {function_name} from graph database {}".format(n, **cargs)
    logging.info(msg)



