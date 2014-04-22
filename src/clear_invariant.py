import sqlite3, logging, argparse, os, collections, ast
import subprocess
import numpy as np
from helper_functions import load_graph_database, grab_scalar,attach_ref_table

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
    graph_conn[n] = load_graph_database(n)

cmd_find_id = '''
SELECT invariant_id from ref_invariant_integer 
WHERE function_name = "{function_name}" '''.format(**cargs)

#cmd_remove_from_ref = '''
#DELETE FROM ref_invariant_integer
#WHERE function_name = "{function_name}" '''.format(**cargs)

cmd_remove_from_invariants = '''
DELETE FROM invariant_integer
WHERE invariant_id = "{invariant_id}" '''

cmd_remove_computed = '''
DELETE FROM computed
WHERE function_name = "{function_name}" '''

for n in graph_conn:
    conn = graph_conn[n]
    attach_ref_table(conn)
    
    cargs["invariant_id"] = None
    try:
        cargs["invariant_id"] = grab_scalar(conn, cmd_find_id)
    except Exception as Ex:
        print "Exception:",Ex
        pass 

    if cargs["invariant_id"] != None:

        msg = "Starting removal {function_name} from graph database {}"
        logging.info(msg.format(n, **cargs))
       
        conn.execute(cmd_remove_from_invariants.format(**cargs))
        conn.execute(cmd_remove_computed.format(**cargs))
        conn.commit()

        msg = "Removed {function_name} from graph database {}"
        logging.info(msg.format(n, **cargs))



