import sqlite3, logging, argparse, os, collections
import subprocess, itertools
import numpy as np
import helper_functions

desc   = "Runs initial queries over the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=10000)
parser.add_argument('--max_n',type=int,default=9,
                    help="Maximum graph size n to compute sequence over")
parser.add_argument('--skip_table_build',default=False,
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

graph_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"]+1):
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

def grab_vector(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()]

cmd_check_unique = '''SELECT max_n FROM ref_invariant_integer_unique'''
unique_max_n = max(grab_vector(conn, cmd_check_unique))

cmd_insert_new_ref = '''
INSERT INTO ref_invariant_integer_unique (max_n) VALUES (?)'''

if unique_max_n < cargs["max_n"]:

    for idx, function_name in invariant_list:
        logging.info("Building unique list for %s"%function_name)
        unique_vals = set()
        for gc in graph_conn.values():
            q = grab_vector(gc, cmd_unique.format(idx))
            unique_vals.update( q )

        insert_vals = zip(itertools.cycle([idx]), unique_vals)
        conn.executemany(cmd_insert, insert_vals)

    conn.execute(cmd_insert_new_ref, (cargs["max_n"],))       
    conn.commit()


# First steps...
# Build a list of possible queries and find out which haven't been done
# Run a basic query over each invariant matching an exact value

cmd_find_unique = '''
SELECT unique_value FROM invariant_integer_unique WHERE invariant_id={}'''

cmd_count = '''
SELECT COUNT(*) FROM invariant_integer 
WHERE invariant_id={} AND value={}'''.strip()

cmd_insert_new_sequence = '''INSERT or IGNORE INTO 
invariant_integer_sequence (query) VALUES (?)'''

Q_LIST = []
for idx, function_name in invariant_list:
    for x in grab_vector(conn, cmd_find_unique.format(idx)):
        q = cmd_count.format(idx, x)
        Q_LIST.append((q,))

conn.executemany(cmd_insert_new_sequence, Q_LIST)
conn.commit()

# Find the missing sequences that have max_n < the current max_n

cmd_search = '''
SELECT seq_id,query FROM invariant_integer_sequence 
WHERE max_n < {max_n} OR seq IS NULL
'''

cmd_record_seq = '''
UPDATE invariant_integer_sequence
SET max_n=(?), seq=(?) WHERE seq_id=(?)'''

for seq_id,q_text in conn.execute(cmd_search.format(**cargs)):
    seq = [grab_vector(graph_conn[n], q_text)[0] for n in graph_conn]
    seq_text = str(seq)[1:-1].replace(' ','')
    vals = (cargs["max_n"], seq_text, seq_id)
    conn.execute(cmd_record_seq, vals)
    print vals, q_text, seq

conn.commit()
