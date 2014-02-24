import sqlite3, logging, argparse, os
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
    result = eval(func)(adj,N = cargs["N"])
    return (idx,cargs["invariant_id"],result)

def insert_invariants(vals):
    msg = "Inserting {} values into graph.{column}"
    msg = msg.format(len(vals), **cargs)
    logging.info(msg)
    cmd  = "INSERT or REPLACE INTO invariant_integer "
    cmd += "(graph_id, invariant_id, value) VALUES (?,?,?)"
    conn.executemany(cmd, vals)

#########################################################################

for func in func_found:

    cargs["column"] = func

    # First get the invariant_id
    cmd  = "SELECT (invariant_id) from ref_invariant_integer "
    cmd += "WHERE function_name='{column}'"
    cmd = cmd.format(**cargs)
    cargs["invariant_id"] = conn.execute(cmd).fetchone()[0]

    cmd  = "SELECT a.adj,a.graph_id FROM graph as a "
    cmd += "LEFT JOIN invariant_integer as b "
    cmd += "ON a.graph_id = b.graph_id AND b.invariant_id={invariant_id} "
    cmd += "WHERE b.value IS NULL"
    cmd = cmd.format(**cargs)

    # Note, we are passing cargs globally, only do one at a time
    itr = select_itr(conn, cmd)

    parallel_compute(itr, 
                     compute_invariant, 
                     callback=insert_invariants, **cargs)

    logging.info("Completed calculation for {column}".format(**cargs))
    conn.commit()
