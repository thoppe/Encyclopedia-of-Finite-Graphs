import sqlite3, logging, argparse, os, collections, ast, sys
import subprocess, itertools
import numpy as np
import helper_functions
from helper_functions import grab_vector

# These variants will not be used in the powerset construction
#__ignored_invariants = ["n_vertex", "n_edge"]

desc   = "Runs initial queries over the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--max_n',type=int,default=8,
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
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer'''
ref_lookup = dict( helper_functions.grab_all(search_conn[1],cmd) )
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
cmd_save = '''INSERT INTO unique_invariant_val(invariant_val_id, value) VALUES (?,?)'''
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
# Build a list of all level 2 sequences
# Build a list of all level 3 sequences
# ...

# Compute all level 1 sequences
# Compute all level 2 sequences
# Compute all level 2 sequences
# ...



exit()

# OLD CODE BELOW


# Assume that ref's are the same for all DB's
cmd = '''SELECT invariant_id,function_name FROM ref_invariant_integer'''
invariant_list = graph_conn[1].execute(cmd).fetchall()
invariant_dict = dict(invariant_list)

# Find the unique values for each invariant and save them

cmd_unique = '''
SELECT DISTINCT value FROM invariant_integer WHERE invariant_id={}'''

cmd_insert = '''
INSERT or REPLACE INTO invariant_integer_unique (invariant_id, unique_value)
VALUES (?,?) 
'''

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

cmd_insert_new_sequence = '''INSERT or IGNORE INTO 
invariant_integer_sequence (query) VALUES (?)'''

UNIQUE_TERMS = {}
for idx, function_name in invariant_list:
    if function_name not in __ignored_invariants:
        cmd = cmd_find_unique.format(idx)
        UNIQUE_TERMS[idx] = grab_vector(conn,cmd)

###########################################################################

def build_structured_terms(terms):
    base_term = '(a.invariant_id=%s AND value=%s)'    
    s = map(lambda x: base_term%x, terms.items())   
    return  ' OR '.join(s)

def build_union_search(terms):
    sterms = build_structured_terms(terms)
    s = cmd_union_search.format(structured_terms=sterms,
                                num_terms= len(terms))
    return s

def sequence_search(cmd_query):
    vec = []
    for n in graph_conn:
        sol = grab_vector(graph_conn[n], cmd_query)
        vec.append(len(sol))
    return vec      

def is_interesting(seq):
    seq = np.array(seq)
    unique_numbers = len(np.unique(seq[seq>0]))
    if sum(seq>0) < 4 or unique_numbers < 2:
        return False
    return True

def is_empty(seq):
    seq = np.array(seq)
    if (seq==0).all(): return True
    return False

def sequence_text(seq):
    return str(seq)[1:-1].replace(' ','')    

def term_text(items):
    return str(items).replace(' ','')

def human_text(items):
    names = ["%s=%s"%(invariant_dict[k],v) for k,v in items.items()]
    return ' AND '.join(names)    

def query_vals(items):
    cmd_query = build_union_search(items)
    seq = sequence_search(cmd_query)
    seq_text = sequence_text(seq)
    t_text   = term_text(items)

    #print cmd_query, seq

    if is_interesting(seq):
        sval = "%s %s"%(seq_text,human_text(items))
        #print ".",
        sys.stdout.flush()
        print "Sequence:", sval

    return (seq_text, t_text, len(items),
            is_interesting(seq), is_empty(seq),
            human_text(items))

###########################################################################

cmd_union_search = '''
  SELECT graph_id, 
  SUM(CASE WHEN {structured_terms} THEN 1 ELSE 0 END) 
  AS match_count
  FROM invariant_integer AS a
  GROUP BY graph_id 
  HAVING match_count={num_terms}'''

cmd_record_seq = '''
  INSERT INTO invariant_integer_sequence
  (seq,terms,term_n,is_interesting,is_empty,human_text) VALUES (?,?,?,?,?,?)'''

# First run through the inital list of invariant terms,
# do not compute these terms if they have already been found
cmd_find_terms = '''
  SELECT terms FROM invariant_integer_sequence WHERE term_n={}'''
known_inital_terms = set(grab_vector(conn, cmd_find_terms.format(1)))

ENTRY_VALS = []

for invariant_id in UNIQUE_TERMS:
    for x in UNIQUE_TERMS[invariant_id]:
        items = {invariant_id:x}
        if not term_text(items) in known_inital_terms:
            vals  = query_vals(items)
            ENTRY_VALS.append(vals)

conn.executemany(cmd_record_seq, ENTRY_VALS)
conn.commit()
logging.info("Initial base invariant sequences %i"%len(ENTRY_VALS))

def check_multi(A,B):
    ''' Check if a query calls the same functions multiple times,
        if so, forbid this query as it's most likely a waste of time'''
    return len(dict(t0,**t1)) == len(A)+len(B)

cmd_find_next_interesting_terms = '''
SELECT terms FROM invariant_integer_sequence 
WHERE term_n={} AND is_interesting=1'''

for comb_n in xrange(1,len(invariant_dict)+1):
    cmd_builder = cmd_find_next_interesting_terms.format(1)
    builder_terms = grab_vector(conn, cmd_builder)

    cmd_next   = cmd_find_next_interesting_terms.format(comb_n)
    next_terms = grab_vector(conn, cmd_next)

    cmd_computed = cmd_find_terms.format(comb_n+1)
    computed_terms = set(grab_vector(conn, cmd_computed))

    ENTRY_VALS = []
    interesting_count = 0

    CHECK_TERMS = []
    for (t0,t1) in itertools.product(builder_terms,next_terms):
        t0,t1 = map(ast.literal_eval,(t0,t1))
        if check_multi(t0,t1):
            items = dict(t0,**t1)
            name  = term_text(items)
            if name not in computed_terms:
                CHECK_TERMS.append(items)

    # Inefficent but functioning way to checking for multiple items
    CHECK_TERMS = map(dict, set(tuple(sorted(d.items())) for d in CHECK_TERMS))

    # Find out which terms have been done before

    for items in CHECK_TERMS:
        vals = query_vals( items )
        ENTRY_VALS.append(vals)
        if vals[3]: interesting_count += 1

    logging.info("Level %i new interesting sequences %i"%
                 (comb_n,interesting_count))
    conn.executemany(cmd_record_seq, ENTRY_VALS)
    conn.commit()

###########################################################################


import time,json
from OEIS_pull import pull_OEIS_seq

# Find all sequences missing OEIS search
cmd_search = '''
SELECT seq,seq_id FROM invariant_integer_sequence
WHERE is_interesting=1 AND OEIS_search IS NULL '''
cmd_insert = '''
UPDATE invariant_integer_sequence SET
OEIS_search=?, OEIS_search_n=?
WHERE seq_id=(?)'''

for seq,idx in conn.execute(cmd_search).fetchall():
    # strip the inital results
    while seq[0] in ["0",","]: seq = seq[1:]

    results = pull_OEIS_seq(seq)
    n = len(results)
    logging.info("Pulled %s, result count %i"%(seq,n))
    formated_results = json.dumps(results,indent=2)
    conn.execute(cmd_insert, (formated_results, n, idx))
    conn.commit()
    time.sleep(.5)
    


