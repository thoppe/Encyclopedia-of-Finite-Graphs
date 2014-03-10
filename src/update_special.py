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

def landing_table_itr(f_landing_table, max_iter):
    with open(f_landing_table,'r') as FIN:
        for group in grouper(FIN,max_iter):
            VALS = []
            for item in group:
                ix = item.strip().split()
                VALS.append( (ix[2], int(ix[1])) )
            yield VALS

def insert_from_landing_table(f_landing_table):

    cmd_insert = '''
      UPDATE graph SET {column}=(?) WHERE graph_id = (?)'''.format(**cargs)

    count = 0

    for raw in landing_table_itr(f_landing_table, max_iter=100000):
        msg = "Starting insert of {} values to {column}"
        logging.info(msg.format(len(raw),**cargs))  

        conn.executemany(cmd_insert.format(**cargs),raw)
        count += len(raw)


    msg = "Saved {} to values to {column}"
    logging.info(msg.format(count,**cargs))  

    os.remove(f_landing_table)
    #logging.info("Removing %s"%f_landing_table)

#########################################################################

# Get the special column names
cmd = '''SELECT * from graph LIMIT 1'''
graph_args_names = zip(*conn.execute(cmd).description)[0]
special_functions = [x for x in graph_args_names if "special" in x]

for func in special_functions:

    cargs["column"] = func
    f_landing = "landing_{N}_{column}.txt".format(**cargs)
    cargs["f_landing_table"] = os.path.join("database",f_landing)  
    f_land = cargs["f_landing_table"]

    # If computation exists from a previous run, add it in
    if os.path.exists(f_land):
        insert_from_landing_table(f_land)

    cmd_count = '''
      SELECT COUNT(*) FROM graph
      WHERE  {column} IS NULL'''
    counts = conn.execute(cmd_count.format(**cargs)).fetchone()[0]

    cmd_grab = '''
      SELECT adj,graph_id FROM graph
      WHERE  {column} IS NULL'''.format(**cargs)

    if not counts:
        msg = "Calculation previously completed for {column}"
        logging.info(msg.format(**cargs))

    else:
        logging.info("Starting calculation for {column}".format(**cargs))
        itr = select_itr(conn, cmd_grab)

        success = parallel_compute(itr, compute_invariant, 
                                   callback=insert_invariants, 
                                   **cargs)
        if success:
            insert_from_landing_table(f_land)       
        else:
            err = "{column} calculation failed"
            logging.critical(err.format(**cargs))

conn.commit()
    #gc.collect()
#conn.close()
