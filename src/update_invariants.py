import numpy as np
import logging, argparse, gc, inspect, os, csv
from helper_functions import load_graph_database, parallel_compute, select_itr
from helper_functions import grab_vector, landing_table_itr, attach_ref_table

desc   = "Updates the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=1000)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the database
conn = load_graph_database(cargs["N"])
attach_ref_table(conn)

logging.info("Starting invariant calculation for {N}".format(**cargs))

# Create a mapping to all the known invariant functions
import invariants
invariant_funcs = dict(inspect.getmembers(invariants,inspect.isfunction))

# Get the special column names
cmd = '''SELECT * from graph LIMIT 1'''
graph_args_names = zip(*conn.execute(cmd).description)[0]

#########################################################################

def compute_invariant(terms):
    func_name = cargs["column"]
    idx,adj   = terms[0], terms[1]

    graph_args = cargs.copy()
    for k,name in enumerate(graph_args_names[2:]):
        graph_args[name] = terms[k+2]

    try:
        func   = invariant_funcs[func_name] 
        result = func(adj,**graph_args)
    except Exception as ex:
        err = "{}:{} idx:{} adj:{}".format(func_name, ex, idx, adj)
        logging.critical(err)
        raise ex

    return (idx,cargs["invariant_id"],result)

def insert_invariants(vals):
    with open(cargs["f_landing_table"], 'a') as FOUT:
        for item in vals:
            # Cast vals to ints
            FOUT.write("%i %i %i\n"%item)

def insert_from_landing_table(f_landing_table):

    cmd_insert = '''
      INSERT or IGNORE INTO invariant_integer
      (graph_id, invariant_id, value) VALUES (?,?,?)'''

    count = 0
    non_zero_terms = 0
    for raw in landing_table_itr(f_landing_table, (0,1,2)):
        msg = "Starting insert of {} values to {column}"
        logging.info(msg.format(len(raw),**cargs))  
        conn.executemany(cmd_insert.format(**cargs),raw)
        count += len(raw)
        
        non_zero_terms += sum(int(x[2])>0 for x in raw)

    conn.commit()

    msg = "Saved {} to values to {column}"
    logging.info(msg.format(count,**cargs))  

    msg = "Count of {column} nonzero terms {}"
    logging.info(msg.format(non_zero_terms,**cargs))  
    
    os.remove(f_landing_table)
    gc.collect()

    #logging.info("Removing %s"%f_landing_table)

#########################################################################

# Identify the invariants that have not been computed
cmd = '''
SELECT function_name FROM ref_invariant_integer 
EXCEPT SELECT function_name FROM computed
'''

compute_invariant_functions = grab_vector(conn,cmd)

cmd = "SELECT function_name,invariant_id FROM ref_invariant_integer"
ref_invariant_lookup = dict(conn.execute(cmd).fetchall())

cmd_mark_success = '''
INSERT OR IGNORE INTO computed (function_name) VALUES (?)'''

if compute_invariant_functions:
    msg = "Remaining invariants to compute {}"
    logging.info(msg.format(compute_invariant_functions))

for func in compute_invariant_functions:
    cargs["column"] = func
    cargs["invariant_id"] = ref_invariant_lookup[func]

    f_landing = "landing_{N}_{column}.txt".format(**cargs)
    f_landing = os.path.join("database",f_landing)  
    cargs["f_landing_table"] = f_landing

    # If computation exists from a previous run, add it in
    if os.path.exists(f_landing):
        insert_from_landing_table(f_landing)

    cmd_grab = '''
      SELECT a.* FROM graph as a
      LEFT JOIN invariant_integer as b
      ON a.graph_id = b.graph_id AND b.invariant_id={invariant_id}
      WHERE b.value IS NULL '''.format(**cargs)

    msg = "Starting calculation for {column}"
    logging.info(msg.format(**cargs))  

    itr = select_itr(conn, cmd_grab) 

    success = parallel_compute(itr, compute_invariant, 
                               callback=insert_invariants, 
                               **cargs)

    # Once changes have been completed, 
    # mark the invariant as complete if successful

    if success:
        insert_from_landing_table(f_landing)    
        conn.execute(cmd_mark_success, (func,))
    else:
        err = "{column} calculation failed"
        logging.critical(err.format(**cargs))

    conn.commit()    
    gc.collect()


conn.close()
