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

for column_entry in template:

    # Add the column if it is missing
    cmd = "ALTER TABLE {table_name} ADD COLUMN {column_entry}"
    cmd = cmd.format(column_entry=column_entry, **cargs)
    try:
        conn.execute(cmd)
        #logging.info(cmd)
    except Exception as E:
        if "duplicate column name" in E.message:
            pass
        else:
            print E
            exit()



