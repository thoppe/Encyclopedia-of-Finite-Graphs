import sqlite3, logging, argparse, os, multiprocessing
from helper_functions import select_itr
from calc_invariants import *

desc   = "Updates the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

logging.info("Starting invariant calculation for {N}".format(**cargs))

cargs["table_name"] = "graph{N}".format(**cargs)
f_database = 'database/{table_name}.db'.format(**cargs)
conn = sqlite3.connect(f_database)

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

for func in func_found:
    cargs["column"] = func
    cmd = "SELECT id,adj FROM {table_name} WHERE {column} IS NULL"
    cmd = cmd.format(**cargs)

    itr = select_itr(cmd)

    update_cmd = "UPDATE {table_name} SET {column}={val} WHERE id={idx}"
    update_count = 0

    for (idx,adj) in itr:
        val = eval(func)(adj,**cargs)
        cmd = update_cmd.format(val=val, idx=idx, **cargs)
        conn.execute(cmd)
        update_count += 1

        if update_count and not (update_count%100): 
            msg = "Updated {n} entries in {table_name}.{column}"
            logging.info(msg.format(n=update_count, **cargs))           
            conn.commit()

conn.commit()
