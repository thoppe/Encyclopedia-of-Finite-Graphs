import numpy as np
import logging, argparse, gc, inspect, os, csv
import multiprocessing, sys, json

from helper_functions import load_graph_database, select_itr
from helper_functions import attach_table, generate_special_database_name
from helper_functions import grab_scalar, grab_vector, grab_all
import invariants

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

# Load the list of invariants to compute
f_invariant_json = os.path.join("templates","ref_invariant_integer.json")
with open(f_invariant_json,'r') as FIN:
    js = json.loads(FIN.read())
    special_names = js["special_function_names"]
    ignored = js["ignored_special_function_names"]
    special_names = [x for x in special_names if x not in ignored]

# Find out which variables have been computed
cmd_check = '''SELECT function_name FROM computed'''
computed_functions = set( grab_vector(sconn,cmd_check) )

#logging.info("Previously computed special invariants {}".format(computed_functions))

#########################################################################
# Count the total number of graphs
#cmd_check = '''SELECT COUNT(graph_id) FROM graph'''
#gn = grab_scalar(conn,cmd_check)
#logging.info("Total graphs found for N={}, {}".format(N,gn))

#########################################################################
# Helper commands

def run_compute(function_name, pfunc, cmd_insert):

    cmd_insert = cmd_insert.format(function_name)

    #cmd_count = '''SELECT COUNT(DISTINCT graph_id) FROM {}'''
    #g_id_n = grab_scalar(sconn, cmd_count.format(function_name))
    #if g_id_n == gn: return True

    #msg = "Computing {} ({}/{})"
    #logging.info(msg.format(function_name, gn-g_id_n,gn))
    index_name = "idx_{}".format(function_name)

    cmd_grab_targets = '''SELECT graph_id,adj FROM graph
    WHERE graph_id NOT IN (SELECT graph_id FROM {})'''
    cmd = cmd_grab_targets.format(function_name)
    targets = select_itr(conn, cmd, chunksize=10000)

    # Drop an index if it exists
    cmd_drop = '''DROP INDEX IF EXISTS "{}";'''
    sconn.execute(cmd_drop.format(index_name))

    compute_parallel(function_name, sconn, pfunc, cmd_insert,targets,N)

    # Create an index once complete
    cmd_create = '''CREATE INDEX IF NOT EXISTS "{}" ON "{}" ("graph_id");'''
    sconn.execute(cmd_create.format(index_name,function_name))


def check_computed(target_function, pfunc, cmd_custom_insert):
    if (target_function not in computed_functions and 
        target_function in special_names):

        msg = "Computing {}"
        logging.info(msg.format(target_function))

        run_compute(target_function, pfunc, cmd_custom_insert)

        cmd_mark_computed= '''
        INSERT OR IGNORE INTO computed (function_name) VALUES (?);'''
        sconn.execute(cmd_mark_computed, (target_function,))
        sconn.commit()
    

from helper_functions import csv_validator, import_csv_to_table
from helper_functions import compute_parallel

#########################################################################
# First compute the degree sequence

target_function = "degree_sequence"

def pfunc_degree((g_id,adj)):
    return g_id, invariants.special_degree_sequence(adj, N=N)    

cmd_insert = '''INSERT INTO {} (graph_id, degree) VALUES (?,?)'''
check_computed(target_function, pfunc_degree, cmd_insert)

#########################################################################
# Now compute the fractional chromatic number

target_function = "fractional_chromatic_number"

def pfunc_frac_chrom((g_id,adj)):
    return g_id, invariants.fractional_chromatic_number(adj, N=N)    

cmd_insert = '''INSERT INTO {} (graph_id, a, b) VALUES (?,?,?)'''
check_computed(target_function, pfunc_frac_chrom, cmd_insert)

#########################################################################
# Now compute the Tutte polynomials

target_function = "tutte_polynomial"

def pfunc_tutte((g_id,adj)):
    return g_id, invariants.special_polynomial_tutte(adj, N=N)    

cmd_insert    = '''INSERT INTO {} 
(graph_id, x_degree, y_degree, coeff) VALUES (?,?,?,?)'''
check_computed(target_function, pfunc_tutte, cmd_insert)

#########################################################################
# Now compute the cycle basis

target_function = "cycle_basis"

def pfunc_cycle_basis((g_id,adj)):
    return g_id, invariants.special_cycle_basis(adj, N=N)

cmd_insert    = '''INSERT INTO {} 
(graph_id, cycle_k, idx) VALUES (?,?,?)'''
check_computed(target_function, pfunc_cycle_basis, cmd_insert)

#########################################################################
# Now compute the independent vertex sets

target_function = "independent_vertex_sets"

def pfunc_IVS((g_id,adj)):
    return g_id, invariants.special_independent_vertex_sets(adj, N=N)

cmd_insert    = '''INSERT INTO {} 
(graph_id, vertex_map) VALUES (?,?)'''
check_computed(target_function, pfunc_IVS, cmd_insert)

#########################################################################
# Now compute the independent edge sets

target_function = "independent_edge_sets"

def pfunc_IES((g_id,adj)):
    return g_id, invariants.special_independent_edge_sets(adj, N=N)

cmd_insert    = '''INSERT INTO {} 
(graph_id, edge_map) VALUES (?,?)'''
check_computed(target_function, pfunc_IES, cmd_insert)

#########################################################################
# Now compute the graph Laplacian

target_function = "laplacian_polynomial"

def pfunc_LAP((g_id,adj)):
    return g_id, invariants.special_laplacian_polynomial(adj, N=N)

cmd_insert    = '''INSERT INTO {} 
(graph_id, x_degree, coeff) VALUES (?,?,?)'''
check_computed(target_function, pfunc_LAP, cmd_insert)

# Debug code below
#cmd_grab = '''SELECT graph_id,adj FROM graph'''
#g_itr    = select_itr(conn, cmd_grab)
#for g,adj in g_itr:
#    print pfunc_LAP((g,adj))
