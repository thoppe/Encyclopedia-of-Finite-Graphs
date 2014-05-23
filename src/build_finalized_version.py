import numpy as np
import logging, argparse, gc, inspect, os, csv
import helper_functions, sqlite3
from helper_functions import load_graph_database, parallel_compute, select_itr
from helper_functions import grab_vector, landing_table_itr, attach_ref_table

desc   = "Builds a finalized version for a fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the database
graph_conn = load_graph_database(cargs["N"])
attach_ref_table(graph_conn)

# Create a new database
f_database = helper_functions.generate_database_name(cargs["N"])
f_search_database = f_database.replace('.db','_search.db')
search_conn = sqlite3.connect(f_search_database, check_same_thread=False)

f_search_template = "templates/searchable_graph.sql"
helper_functions.load_sql_script(search_conn, f_search_template)

# Get the names of all the invariants
cmd  = '''SELECT function_name FROM ref_invariant_integer'''
names= helper_functions.grab_vector(graph_conn,cmd)

# Get the column names in the search_conn database
cmd = '''SELECT * FROM graph_search LIMIT 1'''
cursor = search_conn.execute(cmd)
search_names = map(lambda x: x[0], cursor.description)

# Add the columns if they don't exist
cmd = '''ALTER TABLE graph_search ADD COLUMN {} INTEGER'''
new_cols = set(names).difference(search_names)
for name in new_cols:
    logging.info("Adding column {}".format(name))
    search_conn.execute(cmd.format(name))
    
# Add the entry to computed if it doesn't exist
cmd = '''INSERT OR IGNORE INTO computed(function_name) VALUES (?)'''
search_conn.executemany(cmd, [[x,] for x in names])
search_conn.commit()

# Link the databases together
helper_functions.attach_table(search_conn, f_database, "graphs")

# Check if the graphs have been added
cmd   = '''SELECT graph_id FROM graph_search LIMIT 1'''
check = helper_functions.grab_vector(search_conn, cmd)

# If not add the graph_ids into search database
cmd = '''INSERT INTO graph_search (graph_id) SELECT graph_id FROM graph'''
if not check:
    logging.info("Adding graphs from n={N}".format(**cargs))
    search_conn.execute(cmd)
    search_conn.commit()

# Build the lookup table
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer'''
ref_lookup = dict( helper_functions.grab_all(graph_conn,cmd) )

# Find the uncomputed functions
cmd = '''SELECT function_name FROM computed WHERE NOT is_computed'''
uncomputed_names = helper_functions.grab_vector(search_conn, cmd)

# For each uncomputed function, add the invariant values in
# and once finshed add an index and mark computed!
cmd_insert = '''
UPDATE graph_search
SET {}=(SELECT value FROM invariant_integer 
WHERE 
graph_search.graph_id=invariant_integer.graph_id 
AND 
invariant_integer.invariant_id={})'''

cmd_new_index = '''
CREATE INDEX IF NOT EXISTS "idx_{name}" 
ON "graph_search" ("{name}" ASC);'''

cmd_mark_complete = '''
UPDATE computed SET is_computed=1 
WHERE function_name="{}"'''

for name in uncomputed_names:
    logging.info("Inserting column: {}".format(name))

    idx = ref_lookup[name]
    search_conn.execute(cmd_insert.format(name,idx))

    logging.info("Creating index for column: {}".format(name))
    search_conn.execute(cmd_new_index.format(name=name))

    search_conn.execute(cmd_mark_complete.format(name))

    search_conn.commit()


    

