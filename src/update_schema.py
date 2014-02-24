import sqlite3, logging, argparse, os
from helper_functions import load_template

desc   = "Updates the column names for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

cargs["table_name"] = "graph{N}".format(**cargs)
f_database = 'database/{table_name}.db'.format(**cargs)
conn = sqlite3.connect(f_database)

# Check if database exists, if so exit!
if not os.path.exists(f_database):
    err = "Database %s does not exist. Run generate_db.py first."%f_database
    logging.critical(err)
    exit()

# Update the table based off of the columns in the invariants
# this should be done with a schema, but this works for now

f_graph_template = "templates/graph_invariants.txt"
template = load_template(f_graph_template)

# Add the ref table if it doesn't exist
cols = "invariant_id INTEGER PRIMARY KEY,name TEXT,dtype TEXT"
cmd = "CREATE TABLE IF NOT EXISTS invariant_ref (%s)"%cols
conn.execute(cmd)

# Add the integer invariant table if it doesn't exist
cols = "graph_id INTEGER,invariant_id INTEGER,value INTEGER"
cmd = "CREATE TABLE IF NOT EXISTS invariant_int (%s)"%cols
sol=conn.execute(cmd)
# Here we might add new tables for non integer dtypes
pass

# Add invariants to invariant_ref
for column_entry in template:
    name,dtype = column_entry.split()
    cmd = "INSERT INTO invariant_ref (name,dtype) VALUES (?,?)"
    conn.execute(cmd, (name,dtype))

conn.commit()

