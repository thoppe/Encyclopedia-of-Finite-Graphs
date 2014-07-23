import numpy as np
import logging, argparse, gc, inspect, os, csv
import multiprocessing, sys

from helper_functions import load_graph_database, select_itr
from helper_functions import attach_table, generate_special_database_name
from helper_functions import grab_scalar, grab_vector, grab_all

desc   = "Updates the special invariants for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
cargs = vars(parser.parse_args())
N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the database
conn = load_graph_database(N)
logging.info("Starting special invariant calculation for {N}".format(**cargs))

# Create a mapping to all the known invariant functions
import invariants
#invariant_funcs = dict(inspect.getmembers(invariants,inspect.isfunction))

special_invariants = ["degree_sequence",]

#########################################################################

# Create the special invariant table 
f_graph_template = "templates/special_invariants.sql"
logging.info("Templating database via %s"%f_graph_template)

# The special database
sconn = load_graph_database(N,check_exist=False, special=True,timeout=20)

# The normal database
conn = load_graph_database(N)

# Load the graph template
with open(f_graph_template) as FIN:
    script = FIN.read()
    sconn.executescript(script)

attach_table(conn, generate_special_database_name(N),"sconn")

#########################################################################
# Count the total number of graphs
cmd_check = '''SELECT COUNT(*) FROM {}'''
gn = grab_scalar(conn,cmd_check.format("graph"))
logging.info("Total graphs found for N={}, {}".format(N,gn))

#########################################################################
# Helper commands

def run_compute(function_name, pfunc, cmd_insert):

    cmd_count = '''SELECT COUNT(DISTINCT graph_id) FROM {}'''
    g_id_n = grab_scalar(sconn, cmd_count.format(function_name))
    if g_id_n == gn: return True

    msg = "Computing {} ({}/{})"
    logging.info(msg.format(function_name, gn-g_id_n,gn))

    cmd_grab_targets = '''SELECT graph_id,adj FROM graph
    WHERE graph_id NOT IN (SELECT graph_id FROM {})'''
    cmd = cmd_grab_targets.format(function_name)
    targets = select_itr(conn, cmd, chunksize=10000)
    compute_parallel(function_name, sconn, pfunc, cmd_insert,targets,N)

from helper_functions import csv_validator, import_csv_to_table
from helper_functions import compute_parallel

#########################################################################
# First compute the degree sequence

def pfunc_degree((g_id,adj)):
    return g_id, invariants.special_degree_sequence(adj, N=N)    

cmd_insert = '''INSERT INTO {} (graph_id, degree) VALUES (?,?)'''
run_compute("degree_sequence", pfunc_degree, cmd_insert)

#########################################################################
# Now compute the fractional chromatic number

def pfunc_frac_chrom((g_id,adj)):
    return g_id, invariants.fractional_chromatic_number(adj, N=N)    

cmd_insert = '''INSERT INTO {} (graph_id, a, b) VALUES (?,?,?)'''
run_compute("fractional_chromatic_number", pfunc_frac_chrom, cmd_insert)

#########################################################################
# Now compute the Tutte polynomials

def pfunc_tutte((g_id,adj)):
    return g_id, invariants.special_polynomial_tutte(adj, N=N)    

cmd_insert    = '''INSERT INTO {} 
(graph_id, x_degree, y_degree, coeff) VALUES (?,?,?,?)'''

run_compute("tutte_polynomial", pfunc_tutte, cmd_insert)

#########################################################################
# Now compute the cycle basis

def pfunc_cycle_basis((g_id,adj)):
    return g_id, invariants.special_cycle_basis(adj, N=N)

cmd_insert    = '''INSERT INTO {} 
(graph_id, cycle_k, idx) VALUES (?,?,?)'''

run_compute("cycle_basis", pfunc_cycle_basis, cmd_insert)

#cmd_grab = '''SELECT graph_id,adj FROM graph'''
#g_itr    = select_itr(conn, cmd_grab)
#for g,adj in g_itr:
#    print pfunc_frac_chrom((g,adj))
