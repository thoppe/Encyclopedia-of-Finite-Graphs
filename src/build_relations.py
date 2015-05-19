import sqlite3
import logging
import argparse
import collections
import itertools
from helper_functions import load_graph_database
from helper_functions import grab_vector, grab_all
import numpy as np

desc = "Determine the relations between the invariant sequences"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f', '--force', default=False, action='store_true')
parser.add_argument('--min_n', type=int, default=3,
                    help="Only compare graph of this order and larger")
parser.add_argument('--max_n', type=int, default=10,
                    help="Only compare graph of this order and smaller")
parser.add_argument('--commit_freq', default=25,
                    help="Sequences between database commit.")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the search database
search_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"] + 1):
    search_conn[n] = load_graph_database(n)

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
conn = sqlite3.connect(f_seq_database, check_same_thread=False)

f_database_template = "templates/sequence.sql"
with open(f_database_template) as FIN:
    conn.executescript(FIN.read())

# Find all sequences that have at least four known terms
cmd = '''
SELECT sequence_id FROM stat_sequence
WHERE query_level=1 AND non_zero_terms >= 4'''
full_seq = set(grab_vector(conn, cmd))

# Build the lookup table
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer
ORDER BY invariant_id'''
ref_lookup = dict(grab_all(conn, cmd))
ref_lookup_inv = {v: k for k, v in ref_lookup.items()}
func_names = ref_lookup.keys()

# Iterate over the pairs that have different invariant_ids
cmd = '''
SELECT sequence_id, invariant_id FROM ref_sequence_level1'''
choices = grab_all(conn, cmd)

possible_pairs = []
for p1, p2 in itertools.product(choices, repeat=2):

    if p1[1] != p2[1] and p1[0] in full_seq and p2[0] in full_seq:
        possible_pairs.append([p1[0], p2[0]])

# Add these pairs into the relation database
cmd_add = '''
INSERT OR IGNORE INTO relations (s1_id,s2_id) VALUES (?,?)'''
if possible_pairs:
    conn.executemany(cmd_add, possible_pairs)
    conn.commit()

# Grab all the sequence data as a dictionary
cmd = '''SELECT sequence_id,{} FROM sequence WHERE query_level=1'''
s_list = ["s%i" % k for k in xrange(cargs["min_n"], cargs["max_n"] + 1)]
cmd = cmd.format(','.join(s_list))
SEQ = {}

for item in grab_all(conn, cmd):
    SEQ[item[0]] = np.array(item[1:], dtype=int)

# Grab the ref_sequence_level1 data
cmd = '''
SELECT sequence_id,invariant_id,conditional,value
FROM ref_sequence_level1'''
SEQ_QUERY = {}
for item in grab_all(conn, cmd):
    SEQ_QUERY[item[0]] = item[1:]

# Find the relations where we don't know the subset
cmd = '''SELECT relation_id, s1_id,s2_id FROM relations WHERE subset IS NULL'''
missing_subset = grab_all(conn, cmd)

msg = "There are {} unknown subset relations"
logging.info(msg.format(len(missing_subset)))

# Identify the sequence which CAN'T be subset
# (e.g. one is strictly larger than the other)
cmd = '''UPDATE relations SET subset=0 WHERE relation_id={}'''

for ridx, s1, s2 in missing_subset:
    condition = SEQ[s1] >= SEQ[s2]
    if not condition.all():
        conn.execute(cmd.format(ridx))


# Find the relations where we don't know the subset (again)
cmd = '''SELECT relation_id, s1_id,s2_id FROM relations WHERE subset IS NULL'''
missing_subset = grab_all(conn, cmd)

msg = "After cardinality pass {} unknown subset relations remaining"
logging.info(msg.format(len(missing_subset)))
if missing_subset:
    conn.commit()


def check_subset(s1, s2):
    cmd_find = '''
    SELECT graph_id FROM invariant_integer
    WHERE invariant_id={}
    AND value {} {}
    '''

    invar_id1, c1, v1 = SEQ_QUERY[s1]
    invar_id2, c2, v2 = SEQ_QUERY[s2]

    func_name1 = ref_lookup_inv[invar_id1]
    func_name2 = ref_lookup_inv[invar_id2]

    cmd1 = cmd_find.format(invar_id1, c1, v1)
    cmd2 = cmd_find.format(invar_id2, c2, v2)

    for n in range(cargs["min_n"], cargs["max_n"] + 1):

        GID1 = set(grab_vector(search_conn[n], cmd1))
        GID2 = set(grab_vector(search_conn[n], cmd2))

        if not GID2.issubset(GID1):
            return 0, ""

    msg = "Subset found {}{}{} -> {}{}{}"
    msg = msg.format(func_name2, c2, v2, func_name1, c1, v1)

    return 1, msg

for k, (ridx, s1, s2) in enumerate(missing_subset):
    valid_subset, msg = check_subset(s1, s2)
    cmd = '''UPDATE relations SET subset={} WHERE relation_id={}'''
    conn.execute(cmd.format(int(valid_subset), ridx))
    if msg:
        logging.info(msg)

    if k and k % cargs["commit_freq"] == 0:
        conn.commit()
        msg = "Remaining calculations {}/{}".format(len(missing_subset) - k,
                                                    len(missing_subset))
        logging.info(msg)

conn.commit()

# Find the relations where we don't know equality
cmd = '''SELECT relation_id, s1_id,s2_id FROM relations WHERE equal IS NULL'''
missing_eq = grab_all(conn, cmd)
msg = "There are {} unknown equality relations remaining"
logging.info(msg.format(len(missing_eq)))

# Grab the known relations bewteen the subsets (now complete)
cmd = '''SELECT s1_id,s2_id FROM relations WHERE subset=1'''
known_subsets = set(grab_all(conn, cmd))
for item in missing_eq:
    ridx, p1, p2 = item
    equality_value = (p1, p2) in known_subsets and (p2, p1) in known_subsets
    cmd = '''UPDATE relations SET equal={} WHERE relation_id={}'''
    conn.execute(cmd.format(int(equality_value), ridx))

if missing_eq:
    conn.commit()

# Find the relations where we don't know the exclusive relation
cmd = '''SELECT relation_id, s1_id,s2_id FROM relations WHERE exclusive IS NULL'''
missing_ex = grab_all(conn, cmd)
msg = "There are {} unknown exclusive relations remaining"
logging.info(msg.format(len(missing_ex)))

max_cardinality = np.array([1, 1, 1, 2, 6, 21, 112, 853, 11117, 261080, 11716571])
max_cardinality = max_cardinality[cargs["min_n"]:cargs["max_n"] + 1]

# Check for exclusive relations that are not possible, i.e. those pairs
# that whose union exceeds the total number of graphs
cmd_mark = '''UPDATE relations SET exclusive=0 WHERE relation_id={}'''
for ridx, s1, s2 in missing_ex:
    condition = (SEQ[s1] + SEQ[s2]) <= max_cardinality
    if not condition.all():
        conn.execute(cmd_mark.format(ridx))
conn.commit()

# Find the relations where we don't know the exclusive relation (again)
cmd = '''SELECT relation_id, s1_id,s2_id FROM relations WHERE exclusive IS NULL'''
missing_ex = grab_all(conn, cmd)
msg = "There are {} unknown exclusive relations remaining after cardinality tests"
logging.info(msg.format(len(missing_ex)))


def check_exclusive(s1, s2):
    cmd_find = '''
    SELECT graph_id FROM invariant_integer
    WHERE invariant_id={}
    AND value {} {}
    '''

    invar_id1, c1, v1 = SEQ_QUERY[s1]
    invar_id2, c2, v2 = SEQ_QUERY[s2]

    func_name1 = ref_lookup_inv[invar_id1]
    func_name2 = ref_lookup_inv[invar_id2]

    cmd1 = cmd_find.format(invar_id1, c1, v1)
    cmd2 = cmd_find.format(invar_id2, c2, v2)

    for n in range(cargs["min_n"], cargs["max_n"] + 1):
        GID1 = set(grab_vector(search_conn[n], cmd1))
        GID2 = set(grab_vector(search_conn[n], cmd2))
        if GID1.intersection(GID2):
            return False, ""

    msg = "Checking {}{}{} exclusive of {}{}{}"
    msg = msg.format(func_name1, c1, v1, func_name2, c2, v2)

    return True, msg

for k, (ridx, s1, s2) in enumerate(missing_ex):
    valid_exclusive, msg = check_exclusive(s1, s2)

    cmd = '''UPDATE relations SET exclusive={} WHERE relation_id={}'''
    conn.execute(cmd.format(int(valid_exclusive), ridx))
    if msg:
        logging.info(msg)

    if k and k % cargs["commit_freq"] == 0:
        conn.commit()
        msg = "Remaining calculations {}/{}".format(len(missing_ex) - k,
                                                    len(missing_ex))
        logging.info(msg)

conn.commit()
