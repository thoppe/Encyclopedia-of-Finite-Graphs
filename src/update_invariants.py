import sqlite3, logging, argparse, os, gc
from helper_functions import load_graph_database, parallel_compute, select_itr
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

# Load the database
conn = load_graph_database(cargs["N"])

logging.info("Starting invariant calculation for {N}".format(**cargs))

# Find all the columns
cmd = "SELECT * FROM ref_invariant_integer"
invariant_search = conn.execute(cmd).fetchall()
col_names = set(zip(*invariant_search)[1])

known_invariant_functions = set(invariant_function_map.keys())
#logging.info("Invariant functions found %s"%known_invariant_functions)

# Warn here, for now turn this off
#func_missing = col_names.difference(known_invariant_functions)
#if func_missing:
#    logging.warning("Missing functions %s"%list(func_missing))

func_found = col_names.intersection(known_invariant_functions)


#########################################################################

# TODO, handle error checking in eval(func)
def compute_invariant(terms):
    adj,idx = terms
    func = cargs["column"]
    try:
        result = eval(func)(adj,N = cargs["N"])
    except Exception as ex:
        err = "{}:{} idx:{} adj:{}".format(func, ex, idx, adj)
        logging.critical(err)
        raise ex
    
    return (idx,cargs["invariant_id"],result)

def insert_invariants(vals):
    msg = "Inserting {} values into graph.{column}"
    msg = msg.format(len(vals), **cargs)
    logging.info(msg)
    cmd  = "INSERT or REPLACE INTO invariant_integer "
    cmd += "(graph_id, invariant_id, value) VALUES (?,?,?)"

    # Cast vals to ints, skip if Error was reached
    vals = [map(int, x) for x in vals]
    conn.executemany(cmd, vals)

#########################################################################

# Identify the invariants that have not been computed
cmd = '''
SELECT invariant_id, function_name 
FROM ref_invariant_integer WHERE NOT computed'''
compute_invariant_ids = conn.execute(cmd).fetchall()

for invariant_id,func in compute_invariant_ids:
    cargs["column"] = func
    cargs["invariant_id"] = invariant_id

    logging.info("Starting calculation for {column}".format(**cargs))

    cmd = '''
    SELECT a.adj,a.graph_id FROM graph as a
    LEFT JOIN invariant_integer as b
    ON a.graph_id = b.graph_id AND b.invariant_id={invariant_id}
    WHERE b.value IS NULL '''

    cmd = cmd.format(**cargs)

    # Note, we are passing cargs globally, only do one at a time
    itr = select_itr(conn, cmd)

    success = parallel_compute(itr, compute_invariant, 
                               callback=insert_invariants, 
                               **cargs)

    # Once changes have been completed, 
    # mark the invariant as complete if successful
    cmd = '''
          UPDATE ref_invariant_integer SET computed=1 
          WHERE invariant_id={invariant_id}'''

    if success:
        conn.execute(cmd.format(**cargs))
        conn.commit()
    else:
        err = "{column} calculation failed"
        logging.critical(err.format(**cargs))

    gc.collect()
    
conn.close()
