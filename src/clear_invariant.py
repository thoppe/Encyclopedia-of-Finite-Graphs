import sqlite3, logging, argparse, os, collections, ast
import subprocess
import numpy as np
import helper_functions
from helper_functions import load_graph_database, grab_scalar

desc   = "Remove an invariant calculation from the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('remove_function_list',type=str,nargs="+")
parser.add_argument('--max_n',type=int,default=10,
                    help="Maximum graph size n to remove invariant")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

graph_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"]+1):
    graph_conn[n] = load_graph_database(n)

cmd_remove_invariant = '''
UPDATE invariant_integer 
SET {} = NULL'''

cmd_remove_computed = '''
DELETE FROM computed
WHERE function_name = "{}" '''

def remove_invariant(name, conn):
    conn.execute(cmd_remove_invariant.format(name,name))
    conn.execute(cmd_remove_computed.format(name))

for n,conn in graph_conn.items():
    for function_name in cargs["remove_function_list"]:
        msg = "Starting removal of {} from graph database {}"
        logging.info(msg.format(function_name, n))
        remove_invariant(function_name, conn)
    conn.commit()

# Remove the sequence database as it may be corrupted (will have to rebuild)
f_sequence = os.path.join("database","sequence.db")
if os.path.exists(f_sequence):
    os.remove(f_sequence)
    logging.warning("Removed {}. Please rebuild.".format(f_sequence))


