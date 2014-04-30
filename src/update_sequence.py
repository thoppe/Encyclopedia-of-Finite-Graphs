import sqlite3, logging, argparse, os, collections
import itertools, hashlib
import numpy as np
from helper_functions import load_graph_database, grab_all, grab_scalar
from helper_functions import attach_ref_table, load_sql_script, grab_vector
from helper_functions import attach_table, generate_database_name

desc   = "Verify the sequences produced are the correct ones"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('n',type=int,default=5,
                    help="Maximum graph size n to compute sequences")
parser.add_argument('--non_zero_terms',type=int,default=4,
                    help="Min. number of terms needed to extend the seqeuence")
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())

excluded_terms = ["n_vertex","n_edge","n_endpoints",
                  "is_subgraph_free_C6","is_subgraph_free_C7",
                  "is_subgraph_free_C8","is_subgraph_free_C9",
                  "is_subgraph_free_C10","n_cycle_basis","radius"]

special_conditionals = {"vertex_connectivity":">"}

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
seq_conn = sqlite3.connect(f_seq_database, check_same_thread=False)
attach_ref_table(seq_conn)

# Load the template
f_sequence_template = "templates/sequence.sql"
load_sql_script(seq_conn, f_sequence_template)

# Attach the invariant database to the sequence database
# use only the n'th db for now
#f_db = generate_database_name(cargs["n"])
#attach_table(seq_conn, f_db, "graph{n}".format(**cargs))

# Load the invariant database files
graph_conn = collections.OrderedDict()
for n in range(1, cargs["n"]+1):
    graph_conn[n] = load_graph_database(n)
    attach_ref_table(graph_conn[n])

cmd_invar = '''SELECT invariant_id,function_name FROM ref_invariant_integer'''
invariant_dict = dict(grab_all(graph_conn[1],cmd_invar))

### FIX - remove old invariant_ids!

# Find out what has been computed
cmd_select_compute = '''SELECT * FROM computed'''
compute_dict = dict(grab_all(seq_conn, cmd_select_compute))
if cargs["force"]: compute_dict = {}

# Find and update the unique invariant values

cmd_find_unique = '''
SELECT invariant_id, value FROM invariant_integer
GROUP BY 1,2'''

cmd_insert_unique = '''
INSERT INTO unique_invariant_val(invariant_val_id, value)
VALUES (?,?)'''

cmd_mark_unique_computed = '''
INSERT OR REPLACE INTO computed VALUES 
("unique_invariant_val", "1")'''

name = "unique_invariant_val"

if (name not in compute_dict or 
    not compute_dict[name]):

    all_items = []

    for n,gc in graph_conn.items():
        msg = '''Updating {} for graph set {}'''
        logging.info(msg.format(name,n))
        items = grab_all(gc, cmd_find_unique)
        all_items.append(items)

    # Flatten the list
    flat_items = []
    map(flat_items.extend, all_items)
    # Remove duplicates
    flat_items = list(set(flat_items))
    # Sort for human readibility
    flat_items.sort()
    
    seq_conn.executemany(cmd_insert_unique, flat_items)
    seq_conn.execute(cmd_mark_unique_computed)
    seq_conn.commit()

# Clear the previous marked excluded terms
seq_conn.execute("DELETE FROM exclude_invariant_val")

# Attach the graph database to the sequence database
#f_db = generate_database_name(cargs["n"])
#attach_table(seq_conn, f_db, "graph")

# Mark the excluded terms
cmd_exclude = '''
INSERT INTO exclude_invariant_val
SELECT unique_invariant_id 
FROM unique_invariant_val as a
JOIN (
  SELECT invariant_id FROM ref_invariant_integer
  WHERE function_name IN ({})
  ) AS b
ON a.invariant_val_id = b.invariant_id;'''

excluded_string = str(excluded_terms)[1:-1]
logging.info("Ignoring invariants %s"%excluded_string)
seq_conn.execute(cmd_exclude.format(excluded_string))
seq_conn.commit()

# Get known lvl 1 sequences
cmd_select_known_lvl1 = '''
SELECT unique_invariant_id FROM ref_sequence
WHERE query_level = 1'''
known_lvl1 = set(grab_vector(seq_conn,cmd_select_known_lvl1))

cmd_select_lvl_1 = '''
SELECT unique_invariant_id, invariant_val_id, value
FROM unique_invariant_val
WHERE 
unique_invariant_id NOT IN
(SELECT unique_invariant_id FROM exclude_invariant_val)
ORDER BY invariant_val_id, value'''

# select invariant_val_id from unique_invariant_val 
# group by unique_invariant_val

seq_lvl1 = grab_all(seq_conn, cmd_select_lvl_1)
seq_lvl1 = [x for x in seq_lvl1 if x[0] not in known_lvl1]

msg = "Computing {} new level one sequences"
logging.info(msg.format(len(seq_lvl1)))

#exit()

# Compute these sequences

cmd_count = '''
SELECT adj FROM invariant_integer as a 
LEFT JOIN ref_invariant_integer as b
ON  a.invariant_id  = b.invariant_id 
LEFT JOIN graph AS c
ON  a.graph_id = c.graph_id
WHERE b.function_name = "{function_name}" 
AND a.value {conditional} {value}
ORDER BY adj
'''

def grab_sequence(**args):
    cmd = cmd_count.format(**args)

    C,H = [], []
    h_final = hashlib.md5()

    for n in graph_conn:
        h = hashlib.md5()
        count = 0
        cursor = graph_conn[n].execute(cmd)
        while True:
            results = cursor.fetchmany(1000)
            if not results:
                break
            for item in results:
                count += 1
                h.update(str(item[0]))

        C.append(count)
        h_final.update( h.hexdigest() )

    return C, h_final.hexdigest()

insert_text = ','.join(["s%i"%n for n in graph_conn])
cmd_insert_sequence = '''
INSERT INTO sequence (sequence_id, hash, %s) 
VALUES ({seq_id}, "{total_hash}", {seq})'''%insert_text

cmd_insert_ref_sequence = '''
INSERT INTO ref_sequence 
(query_level, unique_invariant_id, conditional, value, non_zero_terms) 
VALUES (1, {unique_id}, "{conditional}", {value}, {non_zero})'''

for unique_id, invariant_id, value in seq_lvl1:

    name = invariant_dict[invariant_id]

    if name in special_conditionals:
        conditional = special_conditionals[name]
    else:
        conditional = "="

    args = {
        "unique_id":unique_id,
        "conditional":conditional,
        "function_name":invariant_dict[invariant_id],
        "value":value}

    seq, args["total_hash"] = grab_sequence(**args)

    args["non_zero"] = len([1 for x in seq if x])

    cursor = seq_conn.execute(cmd_insert_ref_sequence.format(**args))

    args["seq_id"] = cursor.lastrowid
    args["seq"] = str(seq)[1:-1]

    seq_conn.execute(cmd_insert_sequence.format(**args))
    
    msg  = "New sequence id({seq_id:d}), "
    msg += "{function_name}{conditional}{value}, ({seq})"
    logging.info(msg.format(**args))

    seq_conn.commit()


# WORKING HERE

# Filter based off hash
#cmd_find_unique_hash = '''SELECT * FROM sequence GROUP BY HASH'''
#print len(grab_all(seq_conn, cmd_find_unique_hash))

# Build the unique_invariant_list, this won't change after level 1
cmd_find_unique_mapping = '''
SELECT unique_invariant_id, invariant_val_id 
FROM unique_invariant_val
GROUP BY 1,2;'''
unique_mapping = dict(grab_all(seq_conn, cmd_find_unique_mapping))

# Find all the valid terms to be up from
cmd_select_base = '''
SELECT unique_invariant_id, invariant_val_id, value
FROM unique_invariant_val
WHERE 
unique_invariant_id NOT IN
(SELECT unique_invariant_id FROM exclude_invariant_val);'''
viable_base_terms = grab_all(seq_conn, cmd_select_base)

# Get all level n>1 sequences that need to be computed
cmd_select_nlvl_sequence = '''
SELECT a.sequence_id FROM ref_sequence as a
JOIN sequence as b ON a.sequence_id = b.sequence_id
WHERE query_level={} AND non_zero_terms>={} GROUP BY hash'''

cmd_create_tmp_table = '''
DROP TABLE IF EXISTS tmp_invariants;
CREATE TABLE tmp_invariants (
    n INTEGER,
    adj INTEGER
);
'''

cmd_insert_into_tmp_table = '''
SELECT adj FROM invariant_integer as a 
LEFT JOIN ref_invariant_integer as b
ON  a.invariant_id  = b.invariant_id 
LEFT JOIN graph AS c
ON  a.graph_id = c.graph_id
WHERE b.function_name = "{function_name}" 
AND a.value {conditional} {value}
'''

print cargs
k = 2
cmd = cmd_select_nlvl_sequence.format(k-1, cargs["non_zero_terms"])

for v1_seq_id in grab_vector(seq_conn, cmd):

    # At the start of each invariant, create a new tmp table
    seq_conn.executescript(cmd_create_tmp_table)


    v1_val_id = unique_mapping[v1_seq_id]
    print v1_seq_id, v1_val_id
    
    print "***", v1_seq_id, v1_val_id
    for term in viable_base_terms:
        v2_seq_id, v2_val_id, v2_val = term
        # New term must be strictly larger than the last one
        if v2_val_id > v1_val_id:
            print (v1_seq_id,v2_seq_id), (v1_val_id, v2_val_id), v2_val

#select count(*),* from sequence group by s1,s2,s3,s4,s5,s6,s7,s8,s9,s10 order by count(*)

#valid_invariant_id = [unique_mapping[x] for x in valid_previous]
#print valid_previous
#print valid_invariant_id

exit()
