import numpy as np
import logging, argparse, gc, inspect, os, csv
from helper_functions import load_graph_database, parallel_compute, select_itr
from helper_functions import grouper

desc   = "Updates the special invariants for fixed N"
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
    return (cargs["column"],idx,result)

def insert_invariants(vals):
    with open(cargs["f_landing_table"], 'a') as FOUT:
        for item in vals:
            FOUT.write("%s %s %s\n"%item)

#########################################################################

# Get the special column names
cmd = '''SELECT * from graph LIMIT 1'''
graph_args_names = zip(*conn.execute(cmd).description)[0]
special_functions = [x for x in graph_args_names if "special" in x]

for func in special_functions:

    cargs["column"] = func
    f_landing = "landing_{N}_{column}.txt".format(**cargs)
    cargs["f_landing_table"] = os.path.join("database",f_landing)

    logging.info("Starting calculation for {column}".format(**cargs))

    cmd = '''
      SELECT adj,graph_id FROM graph
      WHERE  {column} IS NULL'''

    cmd = cmd.format(**cargs)
    itr = select_itr(conn, cmd)

    success = parallel_compute(itr, compute_invariant, 
                               callback=insert_invariants, 
                               **cargs)

    # Once changes have been completed, 
    # mark the invariant as complete if successful
    #cmd_mark_success = '''
    #  UPDATE ref_invariant_special SET computed=1 
    #  WHERE invariant_special_id={invariant_special_id}'''

    cmd_insert = '''
      UPDATE graph SET {column}=(?) WHERE graph_id = (?)'''.format(**cargs)
      
    if success:
        #raw = np.loadtxt(cargs["f_landing_table"])
        raw = np.genfromtxt(cargs["f_landing_table"],dtype=str)
        if len(raw.shape)==1: raw = raw.reshape(1,-1)
        raw = raw[:,1:].T[::-1].T

        conn.executemany(cmd_insert.format(**cargs),raw.tolist())
        msg = "Saved {} to values to {column}"
        logging.info(msg.format(raw.shape[0],**cargs))
    else:
        err = "{column} calculation failed"
        logging.critical(err.format(**cargs))
     
    if os.path.exists(cargs["f_landing_table"]):
        os.remove(cargs["f_landing_table"])

    conn.commit()    
    gc.collect()

conn.close()
