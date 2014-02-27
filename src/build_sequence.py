import sqlite3, logging, argparse, os, collections
import subprocess, itertools
import numpy as np
import helper_functions

desc   = "Runs initial queries over the databases"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=10000)
parser.add_argument('--max_n',type=int,default=7,
                    help="Maximum graph size n to compute sequence over")
parser.add_argument('--skip_table_build',default=False,
                    action="store_true",
                    help="Skip the unique calculation")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)

f_database_template = "templates/sequence.sql"
with open(f_database_template) as FIN:
    conn.executescript(FIN.read())

graph_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"]+1):
    graph_conn[n] = helper_functions.load_graph_database(n)

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

def grab_vector(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()]

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

cmd_count = '''
SELECT COUNT(*) FROM invariant_integer 
WHERE invariant_id={} AND value={}'''.strip()

cmd_insert_new_sequence = '''INSERT or IGNORE INTO 
invariant_integer_sequence (query) VALUES (?)'''

TERM_LIST = []
for idx, function_name in invariant_list:
    for x in grab_vector(conn, cmd_find_unique.format(idx)):
        TERM_LIST.append((function_name,idx,x))

# Make this a numpy array so we can easily index it
#TERM_LIST = np.array(TERM_LIST)

#conn.executemany(cmd_insert_new_sequence, Q_LIST)
#conn.commit()
#print TERM_LIST
#exit()

# Find the missing sequences that have max_n < the current max_n

cmd_union_search = '''
  SELECT graph_id, 
  SUM(CASE WHEN {structured_terms} THEN 1 ELSE 0 END) 
  AS match_count
  FROM invariant_integer AS a JOIN ref_invariant_integer AS b
  ON a.invariant_id = b.invariant_id
  GROUP BY graph_id 
  HAVING match_count={num_terms}'''

def build_structured_terms(terms):
    base_term = '(function_name="%s" AND value=%s)'    
    return  ' OR '.join([base_term%(x[0],x[2]) for x in terms])

def build_union_search(terms):
    sterms = build_structured_terms(terms)
    return cmd_union_search.format(structured_terms=sterms,
                             num_terms= len(terms))

def sequence_search(cmd_query):
    vec = []
    for n in graph_conn:
        sol = grab_vector(graph_conn[n], cmd_query)
        vec.append(len(sol))
    return vec      

def is_interesting(seq):
    seq = np.array(seq)
    if sum(seq>0) > 3: return True
    return False
def is_empty(seq):
    seq = np.array(seq)
    if (seq==0).all(): return True
    return False
def sequence_text(seq):
    return str(seq)[1:-1].replace(' ','')    

cmd_record_seq = '''
INSERT INTO invariant_integer_sequence
(seq,terms,term_n,is_interesting,is_empty) VALUES (?,?,?,?,?)'''

# First run through the inital list of invariant terms,
# do not compute these terms if they have already been found
cmd_find_terms = '''
SELECT terms FROM invariant_integer_sequence WHERE term_n={}'''
known_inital_terms = set(grab_vector(conn, cmd_find_terms.format(1)))

ENTRY_VALS = []
for terms in itertools.combinations(TERM_LIST,1):
    term_text = build_structured_terms(terms)
    if term_text not in known_inital_terms:

        cmd_query = build_union_search(terms)
        seq = sequence_search(cmd_query)
        seq_text = sequence_text(seq)
        vals = (seq_text, term_text, len(terms),
                is_interesting(seq), is_empty(seq))
        ENTRY_VALS.append(vals)

        if is_interesting(seq):
            sval = "%s %s"%(seq_text,term_text)
            print "Sequence: ", sval

conn.executemany(cmd_record_seq, ENTRY_VALS)
conn.commit()
logging.info("Initial base invariant sequences %i"%len(ENTRY_VALS))


def check_multi(query):
    ''' Check if a query calls the same functions multiple times,
        if so, forbid this query as it's most likely a waste of time'''

    names = [x.split("function_name=")[1].split()[0][1:-1] for x in query]
    return len(names) == len(set(names))


cmd_find_next_interesting_terms = '''
SELECT terms FROM invariant_integer_sequence 
WHERE term_n={} AND is_interesting=1'''

for comb_n in xrange(1,5):
    cmd_builder = cmd_find_next_interesting_terms.format(1)
    cmd_next    = cmd_find_next_interesting_terms.format(comb_n)
    next_terms = grab_vector(conn, cmd_next)
    builder_terms = grab_vector(conn, cmd_builder)

    ENTRY_VALS = []
    interesting_count = 0

    for items in itertools.product(next_terms, builder_terms):

        if check_multi(items):

            term_text = ' OR '.join(items)
            cmd_query = cmd_union_search.format(structured_terms=term_text,
                                                num_terms=comb_n)

            seq = sequence_search(cmd_query)
            seq_text = sequence_text(seq)

            vals = (seq_text, term_text, comb_n+1,
                    is_interesting(seq), is_empty(seq))

            ENTRY_VALS.append(vals)

        if is_interesting(seq):
            interesting_count += 1
        #    sval = "%s %s"%(seq_text,term_text)
        #    print "Sequence: ", sval

    logging.info("Level %i new interesting sequences %i"%
                 (comb_n,interesting_count))
    conn.executemany(cmd_record_seq, ENTRY_VALS)
    conn.commit()


exit()


cmd_search = '''
SELECT seq_id,query FROM invariant_integer_sequence 
WHERE max_n < {max_n} OR seq IS NULL
'''




    

for seq_id,q_text in conn.execute(cmd_search.format(**cargs)):
    seq = [grab_vector(graph_conn[n], q_text)[0] for n in graph_conn]
    seq_text = str(seq)[1:-1].replace(' ','')
    c1 = is_interesting(seq)
    c2 = is_empty(seq)

    vals = (cargs["max_n"], seq_text, 
            c1,c2,seq_id)

    conn.execute(cmd_record_seq, vals)
    if(c1):
        func = int(q_text.split("id=")[1].split(' ')[0])
        val = int(q_text.split("value=")[1].split(' ')[0])
        print seq, invariant_dict[func], val

    #logging.info("New sequence %s"%seq)

conn.commit()
