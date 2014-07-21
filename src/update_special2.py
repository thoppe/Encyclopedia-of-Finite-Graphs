import numpy as np
import logging, argparse, gc, inspect, os, csv
import multiprocessing

from helper_functions import load_graph_database, parallel_compute, select_itr
from helper_functions import grouper, landing_table_itr
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
sconn = load_graph_database(N,check_exist=False, special=True)

# The normal database
conn = load_graph_database(N)

# Load the graph template
with open(f_graph_template) as FIN:
    script = FIN.read()
    sconn.executescript(script)

#########################################################################
# Count the total number of graphs
cmd_check = '''SELECT COUNT(*) FROM {}'''
gn = grab_scalar(conn,cmd_check.format("graph"))
logging.info("Total graphs found for N={}, {}".format(N,gn))

#########################################################################
# Helper commands

def run_compute(function_name, pfunc, cmd_insert):
    cmd_count = '''SELECT COUNT(DISTINCT graph_id) FROM {}'''
    g_inv_n = grab_scalar(sconn,cmd_count.format(function_name))

    if g_inv_n != gn:
        # Clear the table before starting to prevent dupes
        logging.info("Clearing {}".format(function_name))
        cmd_clear = '''DELETE FROM {}'''.format(function_name)
        logging.info("Computing {}".format(function_name))
        sconn.execute(cmd_clear)
        compute_parallel(function_name, pfunc, cmd_insert)

def compute_parallel(function_name, pfunc, cmd_insert):
    cmd_grab = '''SELECT graph_id,adj FROM graph'''
    g_itr    = select_itr(conn, cmd_grab)

    P = multiprocessing.Pool()
    sol = P.imap(pfunc,g_itr)

    for k, (g_id, terms) in enumerate(sol):
        cmd = cmd_insert.format(function_name, g_id)
        sconn.executemany(cmd, terms)

        if k and k%5000==0:
            msg ="Inserting {} graphs ({}/{})".format(function_name,k,gn)
            logging.info(msg)
            sconn.commit()
    sconn.commit()


#########################################################################
# First compute the degree sequence

def pfunc_degree((g_id,adj)):
    return g_id, invariants.special_degree_sequence(adj, N=N)    

cmd_insert = '''INSERT INTO {} (graph_id, degree) VALUES ({},?)'''
run_compute("degree_sequence", pfunc_degree, cmd_insert)

#########################################################################
# Now compute the fractional chromatic number

def pfunc_frac_chrom((g_id,adj)):
    return g_id, invariants.fractional_chromatic_number(adj, N=N)    

cmd_insert = '''INSERT INTO {} (graph_id, a, b) VALUES ({},?,?)'''
run_compute("fractional_chromatic_number", pfunc_frac_chrom, cmd_insert)

#########################################################################
# Now compute the Tutte polynomials

def pfunc_tutte((g_id,adj)):
    return g_id, invariants.special_polynomial_tutte(adj, N=N)    

cmd_insert    = '''INSERT INTO {} 
(graph_id, x_degree, y_degree, coeff) VALUES ({},?,?,?)'''

run_compute("tutte_polynomial", pfunc_tutte, cmd_insert)

#########################################################################
# Now compute the cycle basis

def pfunc_cycle_basis((g_id,adj)):
    return g_id, invariants.special_cycle_basis(adj, N=N)

cmd_insert    = '''INSERT INTO {} 
(graph_id, cycle_k, idx) VALUES ({},?,?)'''

run_compute("cycle_basis", pfunc_cycle_basis, cmd_insert)

#cmd_grab = '''SELECT graph_id,adj FROM graph'''
#g_itr    = select_itr(conn, cmd_grab)
#for g,adj in g_itr:
#    print pfunc_frac_chrom((g,adj))
