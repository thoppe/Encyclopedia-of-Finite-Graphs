import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from helper_functions import load_graph_database, grab_all
from helper_functions import attach_ref_table, load_sql_script
from helper_functions import attach_table, generate_database_name
import pyparsing as pypar

desc   = "Verify the sequences produced are the correct ones"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('n',type=int,default=5,
                    help="Maximum graph size n to compute sequences")
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())

excluded_terms = ["n_vertex","n_edge","n_endpoints",
                  "is_subgraph_free_C6","is_subgraph_free_C7",
                  "is_subgraph_free_C8","is_subgraph_free_C9",
                  "is_subgraph_free_C10",]

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)
attach_ref_table(conn)

# Load the template
f_sequence_template = "templates/sequence.sql"
load_sql_script(conn, f_sequence_template)

# Find out what has been computed
cmd_select_compute = '''SELECT * FROM computed'''
compute_dict = dict(grab_all(conn, cmd_select_compute))
if cargs["force"]: compute_dict = {}

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
INSERT OR REPLACE INTO unique_invariant_val(invariant_val_id, value)
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

# Clear the previous marked terms
conn.execute("DELETE FROM exclude_invariant_val")

# Mark the excluded terms
#INSERT OR REPLACE INTO exclude_invariant_val
cmd_exclude = '''
INSERT INTO exclude_invariant_val
SELECT invariant_val_id 
FROM unique_invariant_val as a
JOIN (
  SELECT invariant_id FROM ref_invariant_integer
  WHERE function_name IN ({})
  ) AS b
ON a.invariant_id = b.invariant_id;'''

excluded_string = str(excluded_terms)[1:-1]
logging.info("Ignoring invariants %s"%excluded_string)
conn.execute(cmd_exclude.format(excluded_string))


# Attach the invariant database to the sequence database
# use only the n'th db for now
f_db = generate_database_name(cargs["n"])
attach_table(conn, f_db, "graph{n}".format(**cargs))

# Fill up ref_query
cmd_push_into_ref_q = '''
INSERT INTO ref_query(query_level, invariant_val_id)
SELECT 1, invariant_id FROM invariant_integer
WHERE invariant_id NOT IN 
    (SELECT invariant_val_id FROM exclude_invariant_val)
GROUP BY 2; '''
conn.execute(cmd_push_into_ref_q)

conn.commit()


