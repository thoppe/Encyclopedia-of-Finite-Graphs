import sqlite3
import logging
import argparse
import os
import collections
import itertools
from helper_functions import (grab_vector, grab_all, grab_scalar,
                            load_graph_database, load_options)

desc = "Runs initial queries over the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--max_n', type=int, default=9,
                    help="Maximum graph size n to compute sequence over")
parser.add_argument('--force', default=False, action="store_true",
                    help="Recomputes the sequences.")
parser.add_argument('--commit_freq', default=25,
                    help="Sequences between database commit.")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

f_database = "database/sequence.db"
# If forced, delete the sequence database if it exists
if os.path.exists(f_database) and cargs["force"]:
    os.remove(f_database)

# Connect to the sequence database
seq_conn = sqlite3.connect(f_database, check_same_thread=False)

f_database_template = "templates/sequence.sql"
with open(f_database_template) as FIN:
    seq_conn.executescript(FIN.read())

# Load the search database
search_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"] + 1):
    search_conn[n] = load_graph_database(n)

# Get the invariant_ids
cmd_get_invariant_ids = '''
SELECT invariant_id, function_name  FROM
invariant_integer_functions
'''
invariant_func_lookup = dict(grab_all(search_conn[1],
                             cmd_get_invariant_ids))
invariant_id_lookup = dict((v, k) for k, v in
                           invariant_func_lookup.iteritems())

# Load the list of invariants to compute
options = load_options()
func_names = options["invariant_function_names"]

# These will use a different operator
special_conditionals = options["sequence_info"]["special_conditionals"]

# These variants will not be used in the powerset construction
excluded_terms = options["sequence_info"]["excluded_terms"]

# Look for missing values or errors in the database
cmd_find_NULL ='''
SELECT invariant_id FROM invariant_integer
WHERE value IS NULL
GROUP BY invariant_id
'''
for n, conn in search_conn.items():
    bad_idx = grab_vector(conn,cmd_find_NULL)
    for idx in bad_idx:
        msg = "invariant {} not completed for N={}"
        logging.error(msg.format(invariant_func_lookup[idx],n))
    if bad_idx:
        err = "Invariant calculation incomplete"
        raise ValueError(err)

# Add the known functions to the reference list
cmd_insert = '''
INSERT OR IGNORE INTO ref_invariant_integer
(invariant_id, function_name) VALUES (?,?)'''

cursor = search_conn[1].execute('''
    SELECT invariant_id, function_name FROM
    invariant_integer_functions''')
seq_conn.executemany(cmd_insert, cursor)
seq_conn.commit()

# Build the lookup table
cmd_lookup = '''
SELECT function_name,invariant_id
FROM ref_invariant_integer
ORDER BY invariant_id
'''

ref_lookup = dict(grab_all(seq_conn, cmd_lookup))
ref_lookup_inv = {v: k for k, v in ref_lookup.items()}
func_names = ref_lookup.keys()

# Find all the computed unique values
cmd = '''SELECT function_name FROM computed'''
unique_computed_functions = set(grab_vector(seq_conn, cmd))

# Find all the unique values for each invariant,
# skipping those that have been computed already
cmd_find = '''
SELECT DISTINCT value FROM invariant_integer
WHERE invariant_id=?
'''

cmd_save = '''
INSERT OR IGNORE INTO unique_invariant_val
(invariant_id, value) VALUES ({},?)
'''

cmd_mark_computed = '''
INSERT OR REPLACE INTO
computed(function_name) VALUES (?)
'''


remaining_compute_funcs = set(func_names).difference(unique_computed_functions)

for f in remaining_compute_funcs:
    logging.info("Computing unique values for {}".format(f))

    idx = invariant_id_lookup[f]

    for n in search_conn:
        cursor = search_conn[n].execute(cmd_find, (idx,))
        cmd    = cmd_save.format(idx)
        seq_conn.executemany(cmd, cursor)

    seq_conn.execute(cmd_mark_computed,(f,))
seq_conn.commit()


# Check unique values for consistancy
cmd_find = '''
SELECT invariant_id, value
FROM unique_invariant_val'''
warn_flag = False
for invar_id, val in grab_all(seq_conn, cmd_find):
    if not isinstance(val, int):
        func_name = ref_lookup_inv[invar_id]
        msg = "{} has non-integer value {}".format(func_name, val)
        logging.warning(msg)
        warn_flag = True
if warn_flag:
    msg = "Errors found in database. Exiting"
    raise ValueError(msg)

# Build a list of all level 1 sequences
cmd_find = '''
SELECT unique_invariant_id, invariant_id, value FROM
unique_invariant_val ORDER BY invariant_id,value'''
cmd_add = '''
INSERT OR IGNORE INTO ref_sequence_level1
(unique_invariant_id, invariant_id, conditional, value)
VALUES (?,?,?,?)'''

for uid, invar_id, value in grab_all(seq_conn, cmd_find):
    func_name = ref_lookup_inv[invar_id]

    if func_name in special_conditionals:
        conditional = special_conditionals[func_name]
    else:
        conditional = "="

    # If the function is not in the list of excluded terms
    # add it to the ref level 1
    if func_name not in excluded_terms:
        items = (uid, invar_id, conditional, value)
        seq_conn.execute(cmd_add, items)

seq_conn.commit()

# Compute all level 1 sequences
cmd_find_remaining = '''
SELECT
sequence_id,conditional,invariant_id,value
FROM ref_sequence_level1 WHERE sequence_id NOT IN
(SELECT sequence_id FROM sequence WHERE query_level=1)'''

remaining_seq_info = grab_all(seq_conn, cmd_find_remaining)
if remaining_seq_info:
    msg = "Starting {} level 1 sequences"
    logging.info(msg.format(len(remaining_seq_info)))

cmd_sequence = '''
SELECT COUNT(*) FROM invariant_integer
WHERE invariant_id=?
AND value{conditional}?
'''.strip()

cmd_save = '''INSERT INTO sequence({}) VALUES ({})'''
s_string = (["sequence_id", "query_level"] +
            ["s%i" % i for i in search_conn])
q_string = ["?"] * len(s_string)
cmd_save = cmd_save.format(','.join(s_string),
                           ','.join(q_string))

for k, item in enumerate(remaining_seq_info):
    (s_id, conditional, invar_id, value) = item
    func_name = ref_lookup_inv[invar_id]
    cmd = cmd_sequence.format(conditional=conditional)
    seq = [grab_scalar(search_conn[n], cmd, (invar_id,value))
           for n in search_conn]

    items = [s_id, 1] + seq
    seq_conn.execute(cmd_save, items)

    msg = "Level 1 seq: {} {} {}".format(func_name, value, seq)
    logging.info(msg)

    if k and k % cargs["commit_freq"] == 0:
        seq_conn.commit()

seq_conn.commit()

# Function to compute the number of non-zero terms in a seq and record it

def compute_non_zero_terms(level):
    cmd_find_missing = '''
    SELECT sequence_id FROM sequence
    WHERE query_level = {level} AND
    sequence_id NOT IN
     (SELECT sequence_id FROM stat_sequence WHERE query_level = {level})'''

    missing_seq = grab_vector(seq_conn, cmd_find_missing.format(level=level))

    cmd_grab = '''SELECT * FROM sequence
                  WHERE sequence_id={} AND query_level={}'''
    cmd_mark = '''INSERT OR IGNORE INTO stat_sequence
                  (non_zero_terms, sequence_id, query_level) VALUES
                  (?,?,?)'''
    for sid in missing_seq:
        vals = grab_all(seq_conn, cmd_grab.format(sid, level))
        seq = vals[0][2:]
        non_zero_n = sum([1 for x in seq if x > 0])
        seq_conn.execute(cmd_mark, (non_zero_n, sid, level))

compute_non_zero_terms(1)
seq_conn.commit()


# Build a list of all level 2 sequences
# They must have at least 4 non-zero terms in them


cmd_select_valid = '''
SELECT sequence_id FROM stat_sequence
WHERE non_zero_terms >= 4'''

valid_seqs = grab_vector(seq_conn, cmd_select_valid)

# Filter for those not valid
cmd_select = '''
SELECT sequence_id, invariant_id, conditional, value
FROM ref_sequence_level1'''

base_seq = [x for x in grab_all(seq_conn, cmd_select) if x[0] in valid_seqs]
pair_terms = itertools.combinations(base_seq, 2)

cmd_add = '''
INSERT OR IGNORE INTO ref_sequence_level2
(unique_invariant_id1, invariant_id1, conditional1, value1,
 unique_invariant_id2, invariant_id2, conditional2, value2)
VALUES (?,?,?,?, ?,?,?,?)'''

# Remove those that share an invariant_val_id
filtered_pair_terms = (s1 + s2 for s1, s2 in pair_terms if s1[1] != s2[1])

seq_conn.executemany(cmd_add, filtered_pair_terms)
seq_conn.commit()

# Compute all level 2 sequences
cmd_find_remaining = '''
SELECT
 sequence_id,
 invariant_id1, conditional1, value1,
 invariant_id2, conditional2, value2
 FROM ref_sequence_level2 WHERE sequence_id NOT IN
 (SELECT sequence_id FROM sequence WHERE query_level=2)'''

remaining_seq_info = grab_all(seq_conn, cmd_find_remaining)
if remaining_seq_info:
    msg = "Starting {} level 2 sequences".format(len(remaining_seq_info))
    logging.info(msg)

# Compute level 2 sequences

cmd_sequence = '''
SELECT COUNT(*) FROM invariant_integer AS A
JOIN invariant_integer AS B
ON A.graph_id=B.graph_id
WHERE
A.invariant_id=? AND A.value{conditional1}?
AND
B.invariant_id=? AND B.value{conditional2}?
'''

for k, (s_id, id1, c1, v1, id2, c2, v2) in enumerate(remaining_seq_info):
    func_name1 = ref_lookup_inv[id1]
    func_name2 = ref_lookup_inv[id2]

    cmd = cmd_sequence.format(conditional1=c1,conditional2=c2)
    seq = [grab_scalar(search_conn[n], cmd, (id1,v1,id2,v2))
           for n in search_conn]

    items = [s_id, 2] + seq
    seq_conn.execute(cmd_save, items)

    msg = "Level 2 seq: \n\t{}{}{} AND \n\t{}{}{}\n\t\t{}".format(func_name1, c1, v1,
                                                      func_name2, c2, v2,
                                                      seq)
    logging.info(msg)

    if k and k % cargs["commit_freq"] == 0:
        seq_conn.commit()

seq_conn.commit()

compute_non_zero_terms(2)
seq_conn.commit()

# Build a list of all level 3 sequences
# ...

# Compute all level 3 sequences
# ...
