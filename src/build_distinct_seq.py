import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
import helper_functions
from helper_functions import load_graph_database
from helper_functions import attach_ref_table, load_sql_script
from helper_functions import attach_table, generate_database_name
from helper_functions import grab_vector, grab_all, grab_scalar

desc   = "Build sequences from distinct counts (e.g. number of automorhism groups for a given size n."
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f','--force',default=False,action='store_true')
parser.add_argument('--min_n',type=int,default=1,
                    help="Only compare graph of this order and larger")
parser.add_argument('--max_n',type=int,default=10,
                    help="Only compare graph of this order and smaller")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# These terms are not considered
ignored_terms = []

##########################################################################

# Load the standard search database
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

# Build the distinct searches

def compute_distinct_seq(func):
    cmd_search = '''SELECT DISTINCT {} FROM graph_search'''
    seq = []
    for n in range(cargs["min_n"],cargs["max_n"]+1):
        cmd   = cmd_search.format(func)
        items = grab_vector(search_conn[n], cmd)
        seq.append(len(items))
    return seq

print "## Interesting distinct sequences (e.g. non-binary):"
output_msg = "+ `{}` `{}`"
for func in func_names:
    if func not in ignored_terms:
        seq = compute_distinct_seq(func)
        check_seq = np.array(seq,dtype=int)
        if (check_seq>2).any():
            print output_msg.format(func, seq)
print

###########################################################################

# Build the "special" searches

def compute_distinct_special_seq(func):
    cmd_search = '''SELECT DISTINCT {} FROM graph'''
    seq = []
    for n in range(cargs["min_n"],cargs["max_n"]+1):
        conn = load_graph_database(n)
        cmd   = cmd_search.format(func)
        items = grab_vector(conn, cmd)
        seq.append(len(items))
    return seq

special_names = ("special_cycle_basis", 
                 "special_degree_sequence",
                 "special_polynomial_tutte")
print "# Special searches:"
for func in special_names:
    if func not in ignored_terms:
        seq = compute_distinct_special_seq(func)
        check_seq = np.array(seq,dtype=int)
        if (check_seq>2).any():
            print output_msg.format(func, seq)

