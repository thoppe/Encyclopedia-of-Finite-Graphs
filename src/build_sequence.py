import sqlite3, logging, argparse, os, collections, ast, sys
import subprocess, itertools
import numpy as np
import helper_functions
from helper_functions import grab_vector, grab_all, grab_scalar

# These variants will not be used in the powerset construction
excluded_terms = ["n_vertex","n_edge","n_endpoints",
                  "n_cycle_basis","radius"]
# These will use a different operator
special_conditionals = {"vertex_connectivity":">"}

desc   = "Runs initial queries over the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--max_n',type=int,default=10,
                    help="Maximum graph size n to compute sequence over")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the sequence database
f_database = "database/sequence.db"
seq_conn = sqlite3.connect(f_database, check_same_thread=False)

f_database_template = "templates/sequence.sql"
with open(f_database_template) as FIN:
    seq_conn.executescript(FIN.read())

# Load the search database
search_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"]+1):
    f_database = helper_functions.generate_database_name(n)
    f_search_database = f_database.replace('.db','_search.db')
    search_conn[n] = sqlite3.connect(f_search_database, check_same_thread=False)
    helper_functions.attach_ref_table(search_conn[n])

# Build the lookup table
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer 
ORDER BY invariant_id'''
ref_lookup = dict( helper_functions.grab_all(search_conn[1],cmd) )
ref_lookup_inv = {v:k for k, v in ref_lookup.items()}
func_names = ref_lookup.keys()

# Find all the computed unique values
cmd = '''SELECT function_name FROM computed 
WHERE has_computed=1 
AND compute_type="unique"
'''
unique_computed_functions = set(grab_vector(seq_conn, cmd))

# Find all the unique values for each invariant, 
# skipping those that have been computed already
cmd_find = '''SELECT DISTINCT {} FROM graph_search'''
cmd_save = '''INSERT INTO unique_invariant_val(invariant_val_id, value) 
VALUES (?,?)'''
cmd_mark_computed = '''INSERT OR REPLACE INTO 
computed(function_name,compute_type,has_computed) VALUES ("{}","unique",1)'''

for f in set(func_names).difference(unique_computed_functions):
    logging.info("Computing unique values for {}".format(f))

    unique_vals = set()
    for n in search_conn:
        vals = grab_vector(search_conn[n],cmd_find.format(f))
        unique_vals.update(vals)

    invar_id = ref_lookup[f]
        
    for x in unique_vals:
        seq_conn.execute(cmd_save, (invar_id, x))

    seq_conn.execute(cmd_mark_computed.format(f))
    seq_conn.commit()

# Build a list of all level 1 sequences
cmd_find = '''
SELECT unique_invariant_id, invariant_val_id, value FROM
unique_invariant_val ORDER BY invariant_val_id,value'''
cmd_add = '''
INSERT OR IGNORE INTO ref_sequence_level1
(unique_invariant_id, invariant_val_id, conditional, value)
VALUES (?,?,?,?)'''

for uid, invar_id, value in helper_functions.grab_all(seq_conn, cmd_find):
    func_name = ref_lookup_inv[invar_id]

    if func_name in special_conditionals:
        conditional = special_conditionals[func_name]
    else: conditional = "="

    # If the function is not in the list of excluded terms
    # add it to the ref level 1
    if func_name not in excluded_terms:
        items = (uid, invar_id, conditional, value)
        seq_conn.execute(cmd_add, items)

seq_conn.commit()

# Compute all level 1 sequences
cmd_find_remaining = '''
SELECT 
sequence_id,conditional,invariant_val_id,value 
FROM ref_sequence_level1 WHERE sequence_id NOT IN 
(SELECT sequence_id FROM sequence WHERE query_level=1)'''

remaining_seq_info = grab_all(seq_conn,cmd_find_remaining)
if remaining_seq_info:
    msg = "Starting {} level 1 sequences".format(len(remaining_seq_info))
    logging.info(msg)

cmd_sequence = '''
SELECT COUNT(*) FROM graph_search WHERE {} {} {}'''

cmd_save = '''INSERT INTO sequence({}) VALUES ({})'''
s_string = ["sequence_id","query_level"] + ["s%i"%i for i in search_conn]
q_string = ["?"]*len(s_string)
cmd_save = cmd_save.format(','.join(s_string),
                           ','.join(q_string))

for s_id,conditional,invar_id,value in remaining_seq_info:
    func_name = ref_lookup_inv[invar_id]
    cmd = cmd_sequence.format(func_name, conditional,value)
    seq = [grab_scalar(search_conn[n],cmd) for n in search_conn]

    items = [s_id,1] + seq
    seq_conn.execute(cmd_save, items)

    msg = "Level 1 seq: {} {} {}".format(func_name, value,seq)
    logging.info(msg)

    seq_conn.commit()

# Function to compute the number of non-zero terms in a seq and record it

def compute_non_zero_terms(level):
    cmd_find_missing = '''
    SELECT sequence_id FROM sequence
    WHERE query_level = {level} AND
    sequence_id NOT IN 
     (SELECT sequence_id FROM stat_sequence WHERE query_level = {level})'''

    missing_seq = grab_vector(seq_conn,cmd_find_missing.format(level=level))

    cmd_grab = '''SELECT * FROM sequence 
                  WHERE sequence_id={} AND query_level={}'''
    cmd_mark = '''INSERT OR IGNORE INTO stat_sequence 
                  (non_zero_terms, sequence_id, query_level) VALUES
                  (?,?,?)'''
    for sid in missing_seq:
        vals = grab_all(seq_conn,cmd_grab.format(sid,level))
        seq  = vals[0][2:]
        non_zero_n = sum([1 for x in seq if x>0])
        seq_conn.execute(cmd_mark, (non_zero_n, sid, level))
            
    
compute_non_zero_terms(1)
seq_conn.commit()
   
# Build a list of all level 2 sequences
# They must have at least 4 non-zero terms in them

logging.info("Starting level 2 sequences")

cmd_select_valid = '''
SELECT sequence_id FROM stat_sequence 
WHERE non_zero_terms >= 4'''

valid_seqs = grab_vector(seq_conn, cmd_select_valid)

# Filter for those not valid
cmd_select = '''
SELECT sequence_id, invariant_val_id, conditional, value
FROM ref_sequence_level1'''

base_seq = [x for x in grab_all(seq_conn,cmd_select) if x[0] in valid_seqs]
pair_terms = itertools.combinations(base_seq, 2)

cmd_add = '''
INSERT OR IGNORE INTO ref_sequence_level2
(unique_invariant_id1, invariant_val_id1, conditional1, value1,
 unique_invariant_id2, invariant_val_id2, conditional2, value2)
VALUES (?,?,?,?, ?,?,?,?)'''

# Remove those that share an invariant_val_id
filtered_pair_terms = (s1+s2 for s1,s2 in pair_terms if s1[1]!=s2[1])

seq_conn.executemany(cmd_add, filtered_pair_terms)
seq_conn.commit()

# Compute all level 2 sequences
cmd_find_remaining = '''
SELECT 
 sequence_id,
 invariant_val_id1, conditional1, value1,
 invariant_val_id2, conditional2, value2
 FROM ref_sequence_level2 WHERE sequence_id NOT IN 
 (SELECT sequence_id FROM sequence WHERE query_level=2)'''

remaining_seq_info = grab_all(seq_conn,cmd_find_remaining)
if remaining_seq_info:
    msg = "Starting {} level 2 sequences".format(len(remaining_seq_info))
    logging.info(msg)

# Compute level 2 sequences

cmd_sequence = '''
SELECT COUNT(*) FROM graph_search WHERE {} {} {} AND {} {} {}'''

#cmd_save = '''INSERT INTO sequence({}) VALUES ({})'''
#s_string = ["sequence_id","query_level"] + ["s%i"%i for i in search_conn]
#q_string = ["?"]*len(s_string)
#cmd_save = cmd_save.format(','.join(s_string),
#                           ','.join(q_string))

for s_id,id1,c1,v1,id2,c2,v2 in remaining_seq_info:
    func_name1 = ref_lookup_inv[id1]
    func_name2 = ref_lookup_inv[id2]

    cmd = cmd_sequence.format(func_name1,c1,v1, func_name2, c2, v2)
    seq = [grab_scalar(search_conn[n],cmd) for n in search_conn]

    items = [s_id,2] + seq
    seq_conn.execute(cmd_save, items)
    
    msg = "Level 2 seq: {} {} {} AND {} {} {}\n{}".format(func_name1,c1,v1, 
                                                           func_name2, c2, v2, 
                                                           seq)
    logging.info(msg)
    seq_conn.commit()

# Build a list of all level 3 sequences
# ...

# Compute all level 3 sequences
# ...
