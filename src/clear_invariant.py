import sqlite3, logging, argparse, os, collections, ast
import subprocess
import numpy as np
import helper_functions
from helper_functions import load_graph_database, grab_scalar,attach_ref_table

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

cmd_find_id = '''
SELECT invariant_id from ref_invariant_integer 
WHERE function_name = "{function_name}" '''

cmd_remove_from_invariants = '''
DELETE FROM invariant_integer
WHERE invariant_id = "{invariant_id}" '''

cmd_remove_computed = '''
DELETE FROM computed
WHERE function_name = "{function_name}" '''

cmd_clear_search = '''UPDATE graph_search SET {function_name}=NULL'''

for n in graph_conn:
    conn = graph_conn[n]
    attach_ref_table(conn)

    f_database = helper_functions.generate_database_name(n)
    f_search_database = f_database.replace('.db','_search.db')
    search_conn = sqlite3.connect(f_search_database, check_same_thread=False)

    for function_name in cargs["remove_function_list"]:
        cargs["function_name"] = function_name
    
        cargs["invariant_id"] = None
        try:
            cargs["invariant_id"] = grab_scalar(conn, 
                                                cmd_find_id.format(**cargs))
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

            try:
                search_conn.execute(cmd_clear_search.format(**cargs))
                search_conn.commit()
            except:
                pass




