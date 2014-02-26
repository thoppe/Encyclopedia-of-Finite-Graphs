import numpy as np
import logging, argparse, gc, inspect, os, csv
from helper_functions import load_graph_database, parallel_compute, select_itr
from helper_functions import grouper

desc   = "Updates the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=200)
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
        result = func(adj,**cargs)
    except Exception as ex:
        err = "{}:{} idx:{} adj:{}".format(func_name, ex, idx, adj)
        logging.critical(err)
        raise ex
    
    return (idx,cargs["invariant_id"],result)

def insert_invariants(vals):

    with open(cargs["f_landing_table"], 'wa') as FOUT:
        for item in vals:
            # Cast vals to ints
            FOUT.write("%i %i %i\n"%item)

#########################################################################

# Identify the invariants that have not been computed
cmd = '''
SELECT invariant_id, function_name 
FROM ref_invariant_integer WHERE NOT computed'''
compute_invariant_ids = conn.execute(cmd).fetchall()

for invariant_id,func in compute_invariant_ids:
    cargs["column"] = func
    cargs["invariant_id"] = invariant_id

    f_landing = "landing_{N}_{invariant_id}.txt".format(**cargs)
    cargs["f_landing_table"] = os.path.join("database",f_landing)

    logging.info("Starting calculation for {column}".format(**cargs))

    cmd = '''
      SELECT a.adj,a.graph_id FROM graph as a
      LEFT JOIN invariant_integer as b
      ON a.graph_id = b.graph_id AND b.invariant_id={invariant_id}
      WHERE b.value IS NULL '''

    cmd = cmd.format(**cargs)
    itr = select_itr(conn, cmd)

    success = parallel_compute(itr, compute_invariant, 
                               callback=insert_invariants, 
                               **cargs)

    # Once changes have been completed, 
    # mark the invariant as complete if successful
    cmd_mark_success = '''
      UPDATE ref_invariant_integer SET computed=1 
      WHERE invariant_id={invariant_id}'''

    cmd_insert = '''
      INSERT or IGNORE INTO invariant_integer
      (graph_id, invariant_id, value) VALUES (?,?,?)'''
      
    if success:
        raw = np.loadtxt(cargs["f_landing_table"],dtype=int)
        if len(raw.shape)==1: raw = raw.reshape(1,-1)
        conn.executemany(cmd_insert.format(**cargs),raw)
        conn.executescript(cmd_mark_success.format(**cargs))
        conn.commit()
        msg = "Saved {} to values to {column}"
        logging.info(msg.format(raw.shape[0],**cargs))
    else:
        err = "{column} calculation failed"
        logging.critical(err.format(**cargs))
     
    if os.path.exists(cargs["f_landing_table"]):
        os.remove(cargs["f_landing_table"])

    gc.collect()

conn.commit()    
conn.close()
