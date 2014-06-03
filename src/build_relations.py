import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from helper_functions import load_graph_database
from helper_functions import attach_ref_table, load_sql_script
from helper_functions import attach_table, generate_database_name
from helper_functions import grab_vector, grab_all, grab_scalar

desc   = "Determine the relations between the invariant sequences"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
conn = sqlite3.connect(f_seq_database, check_same_thread=False)
attach_ref_table(conn)

f_database_template = "templates/sequence.sql"
with open(f_database_template) as FIN:
    conn.executescript(FIN.read())


# Find all sequences that have at least four known terms
cmd = '''
SELECT sequence_id FROM stat_sequence 
WHERE query_level=1 AND non_zero_terms >= 4'''
full_seq = set(grab_vector(conn, cmd))

# Iterate over the pairs that have different invariant_val_ids
cmd = '''
SELECT sequence_id, invariant_val_id FROM ref_sequence_level1'''
choices = grab_all(conn,cmd)

possible_pairs = []
for p1,p2 in itertools.combinations(choices,2):
    if p1[1] != p2[1] and p1[1] in full_seq and p2[1] in full_seq:
        possible_pairs.append([p1[0], p2[0]])

# Add these pairs into the relation database
cmd_add = '''
INSERT OR IGNORE INTO relations (s1_id,s2_id) VALUES (?,?)'''
conn.executemany(cmd_add, possible_pairs)
conn.commit()


