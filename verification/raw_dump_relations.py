import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from src.helper_functions import load_graph_database
from src.helper_functions import attach_ref_table, load_sql_script
from src.helper_functions import attach_table, generate_database_name
from src.helper_functions import grab_vector, grab_all, grab_scalar

desc   = "Output the computed relations between the invariant sequences"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())

ignored_functions = set([
    "automorphism_group_n",
    "chromatic_number",
])

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
conn = sqlite3.connect(f_seq_database, check_same_thread=False)
attach_ref_table(conn)

# Build the lookup table
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer 
ORDER BY invariant_id'''
ref_lookup = dict(grab_all(conn,cmd) )
ref_lookup_inv = {v:k for k, v in ref_lookup.items()}
func_names = ref_lookup.keys()

# Grab the ref_sequence_level1 data
cmd = '''
SELECT sequence_id,invariant_val_id,conditional,value 
FROM ref_sequence_level1'''
SEQ_QUERY = {}
for item in grab_all(conn,cmd):
    SEQ_QUERY[item[0]] = item[1:]

def info(seq_id):
    i_id, conditional, value = SEQ_QUERY[seq_id]
    func_name = ref_lookup_inv[i_id]
    return func_name, conditional, value

f_output = "verification/relations.md"
FOUT = open(f_output,'w')

#######################################################################

# Find the relations with equality
cmd = '''
SELECT relation_id, s1_id,s2_id FROM relations 
WHERE equal=1'''
relations_eq = grab_all(conn,cmd)

line = "# Equality relations (converse is true)\n"
msg = "`+ {}{}{}` <-> `{}{}{}`\n"

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

# Find the relations that are exclusive
cmd = '''
SELECT relation_id, s1_id,s2_id FROM relations 
WHERE exclusive=1'''
relations_ex = grab_all(conn,cmd)

line = "\n# Exclusive relations\n"
msg = "+ `{}{}{}` intersect `{}{}{}` = 0\n"
FOUT.write(line)

for ridx, s1, s2 in relations_ex:
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
relations_subset = grab_all(conn,cmd)

line = "\n# Subset relations (converse is not true)\n"
FOUT.write(line)

msg = "`+ {}{}{}` -> `{}{}{}`\n"
for ridx, s1, s2 in relations_subset:

    # FLIP THE ORDER FOR SUBSETS
    f1, c1, v1 = info(s2)
    f2, c2, v2 = info(s1)

    vals = (f1, c1,v1, f2, c2, v2)
    if f1 not in ignored_functions and f2 not in ignored_functions:

        if (s1,s2) not in EQ_SET:
            FOUT.write( msg.format(*vals) )

   


