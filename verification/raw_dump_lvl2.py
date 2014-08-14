import sqlite3, logging, argparse, collections
from src.helper_functions import grab_vector, grab_all

desc   = "Make a report of level 2 sequences"
parser = argparse.ArgumentParser(description=desc)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
seq_conn = sqlite3.connect(f_seq_database)

# Build the lookup table
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer 
ORDER BY invariant_id'''
ref_lookup = dict( grab_all(seq_conn,cmd) )
ref_lookup_inv = {v:k for k, v in ref_lookup.items()}
func_names = ref_lookup.keys()

logging.info("Loading level 2 sequences")

cmd_select_interesting = '''
SELECT sequence_id FROM stat_sequence
WHERE query_level=2 AND non_zero_terms>4'''

interesting_idx = set(grab_vector(seq_conn, cmd_select_interesting))

cmd_grab_all = '''
SELECT * FROM sequence AS a
JOIN ref_sequence_level2 AS b
ON a.sequence_id = b.sequence_id
WHERE query_level = 2
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
    
    if s_id in interesting_idx and not is_trivial(seq):
        uid1,c1,ival1,v1 = items[-4:]
        uid2,c2,ival2,v2 = items[-8:-4]
        f1 = ref_lookup_inv[ival1]
        f2 = ref_lookup_inv[ival2]
        key1 = "{}{}{}".format(f1,c1,v1)
        key2 = "{}{}{}".format(f2,c2,v2)
        key = ' AND '.join([key1,key2])

        print key, seq
