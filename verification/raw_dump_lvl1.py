import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from src.helper_functions import grab_vector, grab_all, grab_scalar

desc   = "Make a report of level 1 sequences"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
seq_conn = sqlite3.connect(f_seq_database, check_same_thread=False)

# Find the level 1 sequence_ids with at least 4 terms
cmd_search = '''SELECT sequence_id FROM stat_sequence
WHERE query_level=1 AND non_zero_terms>=4'''
SID = grab_vector(seq_conn, cmd_search)

# Build the lookup table
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer 
ORDER BY invariant_id'''
ref_lookup = dict( grab_all(seq_conn,cmd) )
ref_lookup_inv = {v:k for k, v in ref_lookup.items()}
func_names = ref_lookup.keys()

logging.info("Loading level 1 sequences")

cmd_select_interesting = '''
SELECT sequence_id FROM stat_sequence
WHERE query_level=1 AND non_zero_terms>4'''

cmd_grab_all = '''
SELECT * FROM sequence AS a
JOIN ref_sequence_level1 AS b
ON a.sequence_id = b.sequence_id
WHERE query_level = 1
ORDER BY a.sequence_id
'''

def is_trivial(seq):
    # Check if seq is all ones or zeros
    return len(set(seq)) <= 2

SEQS = collections.OrderedDict()
for items in grab_all(seq_conn, cmd_grab_all):
    s_id = items[0]
    q_level = items[1]
    seq = items[2:12]

    
    if s_id in SID and not is_trivial(seq):
        conditional, invar_val, value = items[-3:]
        function_name = ref_lookup_inv[invar_val]
        key = "{}{}{}".format(function_name,conditional,value)
        SEQS[key] = seq
        print key, seq
