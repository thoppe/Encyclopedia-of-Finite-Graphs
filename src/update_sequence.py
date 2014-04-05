import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from helper_functions import load_graph_database, grab_all
from helper_functions import attach_ref_table, load_sql_script
import pyparsing as pypar

desc   = "Verify the sequences produced are the correct ones"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('n',type=int,default=5,
                    help="Maximum graph size n to compute sequences")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)

# Load the template
f_sequence_template = "templates/sequence.sql"
load_sql_script(conn, f_sequence_template)

# Find out what has been computed
cmd_select_compute = '''SELECT * FROM computed'''
compute_dict = dict(grab_all(conn, cmd_select_compute))

# Load the invariant database files
graph_conn = collections.OrderedDict()
for n in range(1, cargs["n"]+1):
    graph_conn[n] = load_graph_database(n)
    attach_ref_table(graph_conn[n])

# Find and update the unique invariant values

cmd_find_unique = '''
SELECT invariant_id, value FROM invariant_integer
GROUP BY 1,2;'''

cmd_insert_unique = '''
INSERT OR REPLACE INTO unique_invariant_val(invariant_id, value)
VALUES (?,?)'''

cmd_mark_unique_computed = '''
INSERT OR REPLACE INTO computed VALUES 
("unique_invariant_val", "1")'''

name = "unique_invariant_val"

if (name not in compute_dict or 
    not compute_dict[name]):
    
    for n in graph_conn:
        msg = '''Updating {} for graph set {}'''
        logging.info(msg.format(name,n))
        items = grab_all(graph_conn[n], cmd_find_unique)
        conn.executemany(cmd_insert_unique, items)

    conn.execute(cmd_mark_unique_computed)
    conn.commit()
