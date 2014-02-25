import sqlite3, logging, argparse, os
import subprocess, itertools
import numpy as np
import helper_functions

desc   = "Runs initial queries over the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=10000)
parser.add_argument('--max_N',type=int,default=7,
                    help="Maximum N to compute sequence over")
parser.add_argument('--skip_unique',default=False,
                    action="store_true",
                    help="Skip the unique calculation")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)

f_database_template = "templates/sequence.sql"
with open(f_database_template) as FIN:
    conn.executescript(FIN.read())


graph_conn = {}
for n in range(1, cargs["max_N"]+1):
    graph_conn[n] = helper_functions.load_graph_database(n)

# Assume that ref's are the same for all DB's
cmd = '''SELECT invariant_id,function_name FROM ref_invariant_integer'''
invariant_list = graph_conn[1].execute(cmd).fetchall()


# Find the unique values for each invariant and save them

cmd_unique = '''
SELECT DISTINCT value FROM invariant_integer WHERE invariant_id={}'''

cmd_insert = '''
INSERT or REPLACE INTO invariant_integer_unique (invariant_id, unique_value)
VALUES (?,?) 
'''

if not cargs["skip_unique"]:

    for idx, function_name in invariant_list:
        unique_vals = set()
        for n in graph_conn:
            q = graph_conn[n].execute(cmd_unique.format(idx))        
            q = [x[0] for x in q.fetchall()]
            unique_vals.update( q )

        insert_vals = zip(itertools.cycle([idx]), unique_vals)
        conn.executemany(cmd_insert, insert_vals)
        
    conn.commit()

# First steps...
# Run a basic query over each invariant matching an exact value

cmd_find_unique = '''
SELECT unique_value FROM invariant_integer_unique WHERE invariant_id={}'''

cmd_count = '''
SELECT COUNT(*) FROM invariant_integer 
WHERE invariant_id={} AND value={}'''

for idx, function_name in invariant_list:
    unique_vals = conn.execute(cmd_find_unique.format(idx)).fetchall()
    for x in unique_vals:

        seq = []
        for n in graph_conn:
            cmd = cmd_count.format(idx, x[0])
            s = graph_conn[n].execute(cmd).fetchone()[0]
            seq.append(s)
        print function_name, x, seq



