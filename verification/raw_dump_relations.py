import sqlite3, logging, argparse, os, collections
import subprocess, itertools, json
import numpy as np
from src.helper_functions import grab_vector, grab_all, grab_scalar

desc   = "Output the computed relations between the invariant sequences"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

ignored_functions = []

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
seq_conn = sqlite3.connect(f_seq_database, check_same_thread=False)

# Load the list of invariants to compute
f_invariant_json = os.path.join("templates","ref_invariant_integer.json")
with open(f_invariant_json,'r') as FIN:
    js = json.loads(FIN.read())
    func_names = js["invariant_function_names"]

    # These will use a different operator
    special_conditionals = js["sequence_info"]["special_conditionals"]

    # These variants will not be used in the powerset construction
    excluded_terms = js["sequence_info"]["excluded_terms"]

# Build the lookup table
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer 
ORDER BY invariant_id'''
ref_lookup = dict(grab_all(seq_conn,cmd) )
ref_lookup_inv = {v:k for k, v in ref_lookup.items()}
func_names = ref_lookup.keys()

# Grab the ref_sequence_level1 data
cmd = '''
SELECT sequence_id,invariant_val_id,conditional,value 
FROM ref_sequence_level1'''
SEQ_QUERY = {}
for item in grab_all(seq_conn,cmd):
    SEQ_QUERY[item[0]] = item[1:]

def info(seq_id):
    i_id, conditional, value = SEQ_QUERY[seq_id]
    func_name = ref_lookup_inv[i_id]
    return func_name, conditional, value

f_output = "verification/relations.md"
FOUT = open(f_output,'w')

logging.info("Saving relation information to {}".format(f_output))

#######################################################################

# Find the relations with equality
cmd = '''
SELECT relation_id, s1_id,s2_id FROM relations 
WHERE equal=1'''
relations_eq = grab_all(seq_conn,cmd)

line = "# Equality relations (converse holds)\n"
msg = "+ `{}{}{}` <-> `{}{}{}`\n"

FOUT.write(line)
EQ_SET = set()

for ridx, s1, s2 in relations_eq:
    EQ_SET.add((s1,s2))
    EQ_SET.add((s2,s1))

    f1, c1, v1 = info(s1)
    f2, c2, v2 = info(s2)

    vals = (f1, c1,v1, f2, c2, v2)
    if f1 not in ignored_functions and f2 not in ignored_functions:
        FOUT.write( msg.format(*vals) )

#######################################################################

# Find the relations that are subsets (and not equalities)
cmd = '''
SELECT relation_id, s1_id,s2_id FROM relations 
WHERE subset=1'''
relations_subset = grab_all(seq_conn,cmd)

line = "\n# Subset relations (converse is not true)\n"
FOUT.write(line)

msg = "+ `{}{}{}` -> `{}{}{}`\n"
for ridx, s1, s2 in relations_subset:

    # FLIP THE ORDER FOR SUBSETS
    f1, c1, v1 = info(s2)
    f2, c2, v2 = info(s1)

    vals = (f1, c1,v1, f2, c2, v2)
    if f1 not in ignored_functions and f2 not in ignored_functions:

        if (s1,s2) not in EQ_SET:
            FOUT.write( msg.format(*vals) )

#######################################################################

# Find the relations that are exclusive
cmd = '''
SELECT relation_id, s1_id,s2_id FROM relations 
WHERE exclusive=1'''
relations_ex = grab_all(seq_conn,cmd)

line = "\n# Exclusive relations\n"
msg = "+ `{}{}{}` intersect `{}{}{}` = 0\n"
FOUT.write(line)

for ridx, s1, s2 in relations_ex:
    f1, c1, v1 = info(s1)
    f2, c2, v2 = info(s2)

    vals = (f1, c1,v1, f2, c2, v2)
    if f1 not in ignored_functions and f2 not in ignored_functions:
        FOUT.write( msg.format(*vals) )   


