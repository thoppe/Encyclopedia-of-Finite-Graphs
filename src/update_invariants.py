import sqlite3, logging, argparse, os, gc, inspect
from helper_functions import load_graph_database, parallel_compute, select_itr

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

# Create a mapping to all the known invariant functions
import invariants
invariant_funcs = dict(inspect.getmembers(invariants,inspect.isfunction))

#########################################################################

def compute_invariant(terms):
    func_name = cargs["column"]
    adj,idx   = terms
    try:
        func   = invariant_funcs[func_name]
        result = func(adj,N = cargs["N"])
    except Exception as ex:
        err = "{}:{} idx:{} adj:{}".format(func_name, ex, idx, adj)
        logging.critical(err)
        raise ex
    
    return (idx,cargs["invariant_id"],result)

def insert_invariants(vals):
    cmd  = "INSERT or REPLACE INTO invariant_integer "
    cmd += "(graph_id, invariant_id, value) VALUES (?,?,?)"

    # Cast vals to ints, skip if Error was reached
    vals = [map(int, x) for x in vals]
    conn.executemany(cmd, vals)

    msg = "Inserting {} values into graph.{column}"
    msg = msg.format(len(vals), **cargs)
    logging.info(msg)
    conn.commit()

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
