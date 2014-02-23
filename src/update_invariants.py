import sqlite3, logging, argparse, os, multiprocessing
from helper_functions import grouper, select_itr
from calc_invariants import *

desc   = "Updates the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=10000)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

logging.info("Starting invariant calculation for {N}".format(**cargs))

cargs["table_name"] = "graph{N}".format(**cargs)
f_database = 'database/{table_name}.db'.format(**cargs)
conn = sqlite3.connect(f_database, check_same_thread=False)

# Check if database exists, if so exit!
if not os.path.exists(f_database):
    err = "Database %s does not exist. Run generate_db.py first."%f_database
    logging.critical(err)
    exit()

# Find all the columns
cmd = "PRAGMA table_info({table_name})".format(**cargs)
cursor = conn.execute(cmd)
col_names = set([x[1] for x in cursor.fetchall()])
col_names.discard("id")
col_names.discard("adj")
#logging.info("Columns found %s"%col_names)

known_invariant_functions = set(invariant_function_map.keys())
#logging.info("Invariant functions found %s"%known_invariant_functions)

# Warn here, for now turn this off
#func_missing = col_names.difference(known_invariant_functions)
#if func_missing:
#    logging.warning("Missing functions %s"%list(func_missing))

func_found = col_names.intersection(known_invariant_functions)

#########################################################################

def compute_invariant(terms):
    idx = terms[0]
    graph_adj = terms[1]
    func = cargs["column"]
    result = eval(func)(graph_adj,N = cargs["N"])
    return (result,idx)

def insert_invariants(vals):
    msg = "Inserting {} values into {table_name}.{column}"
    msg = msg.format(len(vals), **cargs)
    logging.info(msg)
    cmd = "UPDATE {table_name} SET {column}=? WHERE id=?"
    cmd = cmd.format(**cargs)
    conn.executemany(cmd, vals)

#########################################################################

for func in func_found:

    cargs["column"] = func

    cmd  = "SELECT id,adj FROM {table_name} WHERE {column} IS NULL"
    cmd  = cmd.format(**cargs)
    graph_allocator = grouper(select_itr(conn,cmd), cargs["chunksize"])

    # Note, we are passing "func" globally, make sure everything is closed
    P = multiprocessing.Pool()

    for gitr in graph_allocator:
        P.map_async(compute_invariant, gitr,
                    chunksize=10, 
                    callback=insert_invariants)

    P.close()
    P.join()

    logging.info("Completed calculation for {column}".format(**cargs))

    conn.commit()
