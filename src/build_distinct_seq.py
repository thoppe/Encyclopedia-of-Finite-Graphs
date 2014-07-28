import sqlite3, logging, argparse, os, collections
import subprocess, itertools, multiprocessing, json
import numpy as np
import helper_functions
from helper_functions import load_graph_database, load_distinct_database
from helper_functions import load_sql_script, select_itr
from helper_functions import attach_table, generate_database_name
from helper_functions import grab_vector, grab_all, grab_scalar

desc   = "Build sequences from distinct counts (e.g. number of automorhism groups for a given size n."
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
#parser.add_argument('--max_n',type=int,default=10,
#                    help="Only compare graph of this order and smaller")
cargs = vars(parser.parse_args())
N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the list of invariants to compute
f_invariant_json = os.path.join("templates","ref_invariant_integer.json")
with open(f_invariant_json,'r') as FIN:
    distinct_seq_names = json.loads(FIN.read())["distinct_sequences"]

##########################################################################

# Load the special database
sconn = load_graph_database(N,check_exist=True, special=True)
cmd_get_id = '''SELECT DISTINCT(graph_id) FROM {}'''

dconn = load_distinct_database(check_exist=False)
load_sql_script(dconn, "templates/distinct.sql")

# Skip terms that have already been computed
cmd_computed = '''SELECT function_name FROM distinct_sequence WHERE N=(?)'''
known_terms = set(grab_vector(dconn, cmd_computed, (N,)))

for term in known_terms.intersection(distinct_seq_names):
    del distinct_seq_names[term]

##########################################################################

def build_collection(target_function, target_columns):
    g_id_itr = select_itr(sconn,cmd_get_id.format(target_function))

    cmd_get_seq = '''
    SELECT {cols} FROM {func} WHERE graph_id=(?) ORDER BY {cols}'''
    cmd_get_seq = cmd_get_seq.format(cols=target_columns, func=target_function)
    C = collections.Counter()

    def format_collection_query(g):
        vals = grab_all(sconn,cmd_get_seq,g)
        return tuple(vals)

    for g in g_id_itr:
        vals = format_collection_query(g)
        C[vals] += 1
    return C


for target_function, target_columns in distinct_seq_names.items():

    msg = "Computing distinct terms in {} ({})".format(target_function,N)
    logging.info(msg)

    C = build_collection(target_function, target_columns)
    cmd_insert = '''INSERT INTO distinct_sequence 
    (function_name, N, coeff) VALUES ("{}",{},{})'''
    cmd = cmd_insert.format(target_function, N, len(C))
    dconn.execute(cmd)
    dconn.commit()
        
