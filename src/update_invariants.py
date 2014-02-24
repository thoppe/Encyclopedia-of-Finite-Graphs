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
cmd = "SELECT * FROM invariant_ref"
invariant_search = conn.execute(cmd).fetchall()
integer_invariants = [x for x in invariant_search if x[2]=="INTEGER"]
col_names = set(zip(*integer_invariants)[1])

known_invariant_functions = set(invariant_function_map.keys())
#logging.info("Invariant functions found %s"%known_invariant_functions)

# Warn here, for now turn this off
#func_missing = col_names.difference(known_invariant_functions)
#if func_missing:
#    logging.warning("Missing functions %s"%list(func_missing))

func_found = col_names.intersection(known_invariant_functions)

#########################################################################

def compute_invariant(terms):
    adj,idx = terms
    func = cargs["column"]
    result = eval(func)(adj,N = cargs["N"])
    return (idx,cargs["invariant_id"],result)

def insert_invariants(vals):
    msg = "Inserting {} values into graph.{column}"
    msg = msg.format(len(vals), **cargs)
    logging.info(msg)
    cmd  = "INSERT or REPLACE INTO invariant_int "
    cmd += "(graph_id, invariant_id, value) VALUES (?,?,?)"
    conn.executemany(cmd, vals)

#########################################################################

for func in func_found:

    cargs["column"] = func

    # First get the invariant_id
    cmd = "SELECT (invariant_id) from invariant_ref WHERE name='{column}'"
    cmd = cmd.format(**cargs)
    cargs["invariant_id"] = conn.execute(cmd).fetchone()[0]

    cmd  = "SELECT adj,a.graph_id FROM graph as a "
    cmd += "LEFT JOIN invariant_int as b "
    cmd += "ON a.graph_id = b.graph_id AND b.invariant_id={invariant_id} "
    cmd += "WHERE b.value IS NULL"
    cmd = cmd.format(**cargs)
    graph_allocator = grouper(select_itr(conn,cmd), cargs["chunksize"])

    '''
    # Test run without multiprocessing
    for gitr in graph_allocator:
        for g in gitr:
            v = compute_invariant(g)
            print g, v
            insert_invariants(v)

    exit()
    '''
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
