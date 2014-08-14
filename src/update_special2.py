import logging
import argparse

from helper_functions import load_graph_database, select_itr, load_options
from helper_functions import attach_table, generate_special_database_name
from helper_functions import grab_vector, grab_all
from helper_functions import compute_parallel
import invariants

desc = "Updates the special invariants for fixed N"
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
logging.info("Templating database via %s" % f_graph_template)

# The special database
sconn = load_graph_database(N, check_exist=False, special=True, timeout=20)

# The normal database
conn = load_graph_database(N)

# Load the graph template
with open(f_graph_template) as FIN:
    script = FIN.read()
    sconn.executescript(script)

attach_table(conn, generate_special_database_name(N), "sconn")

# Load the list of invariants to compute
options = load_options()
special_names = options["special_function_names"]
ignored = options["ignored_special_function_names"]
special_names = [x for x in special_names if x not in ignored]

# Find out which variables have been computed
cmd_check = '''SELECT function_name FROM computed'''
computed_functions = set(grab_vector(sconn, cmd_check))

#########################################################################
# Count the total number of graphs
#cmd_check = '''SELECT COUNT(graph_id) FROM graph'''
#gn = grab_scalar(conn,cmd_check)
#logging.info("Total graphs found for N={}, {}".format(N,gn))

#########################################################################
# Helper commands


def run_compute(function_name, pfunc, cmd_insert, targets=None):

    cmd_insert = cmd_insert.format(function_name)
    #cmd_count = '''SELECT COUNT(DISTINCT graph_id) FROM {}'''
    #g_id_n = grab_scalar(sconn, cmd_count.format(function_name))
    # if g_id_n == gn: return True

    #msg = "Computing {} ({}/{})"
    #logging.info(msg.format(function_name, gn-g_id_n,gn))
    index_name = "idx_{}".format(function_name)

    cmd_grab_targets = '''SELECT graph_id,adj FROM graph
    WHERE graph_id NOT IN (SELECT graph_id FROM {})'''
    cmd = cmd_grab_targets.format(function_name)
    if targets is None:
        targets = select_itr(conn, cmd, chunksize=10000)

    # Drop an index if it exists
    cmd_drop = '''DROP INDEX IF EXISTS "{}";'''
    sconn.execute(cmd_drop.format(index_name))

    compute_parallel(function_name, sconn, pfunc, cmd_insert, targets, N)

    # Create an index once complete
    cmd_create = '''CREATE INDEX IF NOT EXISTS "{}" ON "{}" ("graph_id");'''
    sconn.execute(cmd_create.format(index_name, function_name))


def check_computed(target_function, pfunc, cmd_custom_insert):
    if (target_function not in computed_functions and
            target_function in special_names):

        msg = "Computing {}"
        logging.info(msg.format(target_function))

        run_compute(target_function, pfunc, cmd_custom_insert)

        cmd_mark_computed = '''
        INSERT OR IGNORE INTO computed (function_name) VALUES (?);'''
        sconn.execute(cmd_mark_computed, (target_function,))
        sconn.commit()

#########################################################################
# First compute the degree sequence

target_function = "degree_sequence"


def pfunc_degree(xxx_todo_changeme):
    (g_id, adj) = xxx_todo_changeme
    return g_id, invariants.special_degree_sequence(adj, N=N)

cmd_insert = '''INSERT INTO {} (graph_id, degree) VALUES (?,?)'''
check_computed(target_function, pfunc_degree, cmd_insert)

#########################################################################
# Now compute the fractional chromatic number

target_function = "fractional_chromatic_number"


def pfunc_frac_chrom(xxx_todo_changeme1):
    (g_id, adj) = xxx_todo_changeme1
    return g_id, invariants.fractional_chromatic_number(adj, N=N)

cmd_insert = '''INSERT INTO {} (graph_id, a, b) VALUES (?,?,?)'''
check_computed(target_function, pfunc_frac_chrom, cmd_insert)

#########################################################################
# Now compute the Tutte polynomials

target_function = "tutte_polynomial"


def pfunc_tutte(xxx_todo_changeme2):
    (g_id, adj) = xxx_todo_changeme2
    return g_id, invariants.special_polynomial_tutte(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, x_degree, y_degree, coeff) VALUES (?,?,?,?)'''
check_computed(target_function, pfunc_tutte, cmd_insert)

#########################################################################
# Now compute the cycle basis

target_function = "cycle_basis"


def pfunc_cycle_basis(xxx_todo_changeme3):
    (g_id, adj) = xxx_todo_changeme3
    return g_id, invariants.special_cycle_basis(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, cycle_k, idx) VALUES (?,?,?)'''
check_computed(target_function, pfunc_cycle_basis, cmd_insert)

#########################################################################
# Now compute the independent vertex sets

target_function = "independent_vertex_sets"


def pfunc_IVS(xxx_todo_changeme4):
    (g_id, adj) = xxx_todo_changeme4
    return g_id, invariants.special_independent_vertex_sets(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, vertex_map) VALUES (?,?)'''
check_computed(target_function, pfunc_IVS, cmd_insert)

#########################################################################
# Now compute the independent edge sets

target_function = "independent_edge_sets"


def pfunc_IES(xxx_todo_changeme5):
    (g_id, adj) = xxx_todo_changeme5
    return g_id, invariants.special_independent_edge_sets(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, edge_map) VALUES (?,?)'''
check_computed(target_function, pfunc_IES, cmd_insert)

#########################################################################
# Now compute the graph Laplacian

target_function = "laplacian_polynomial"


def pfunc_LAP(xxx_todo_changeme6):
    (g_id, adj) = xxx_todo_changeme6
    return g_id, invariants.special_laplacian_polynomial(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, x_degree, coeff) VALUES (?,?,?)'''
check_computed(target_function, pfunc_LAP, cmd_insert)

#########################################################################
# Now compute the characteristic polynomial of the adj matrix

target_function = "characteristic_polynomial"


def pfunc_CHARPOLY(xxx_todo_changeme7):
    (g_id, adj) = xxx_todo_changeme7
    return g_id, invariants.special_characteristic_polynomial(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, x_degree, coeff) VALUES (?,?,?)'''
check_computed(target_function, pfunc_CHARPOLY, cmd_insert)

#########################################################################
# Now compute the chromatic polynomial, this is special since it needs
# the previously computed Tutte polynomial as input

target_function = "chromatic_polynomial"


def iterator_tutte_polynomial(func_name):

    cmd_grab_targets = '''SELECT graph_id,adj FROM graph
    WHERE graph_id NOT IN (SELECT graph_id FROM {})'''.format(func_name)

    g_itr = select_itr(conn, cmd_grab_targets)
    cmd = '''SELECT x_degree,y_degree,coeff FROM tutte_polynomial WHERE graph_id=(?)'''

    for g_id, adj, in g_itr:
        args = {"N": N}
        args["tutte_polynomial"] = grab_all(sconn, cmd, (g_id,))
        yield (g_id, adj, args)


def pfunc_CHROMPOLY(xxx_todo_changeme8):
    (g_id, adj, args) = xxx_todo_changeme8
    return g_id, invariants.special_chromatic_polynomial(adj, **args)

cmd_insert    = '''INSERT INTO {}
(graph_id, x_degree, coeff) VALUES (?,?,?)'''

targets = iterator_tutte_polynomial(target_function)

if (target_function not in computed_functions and
        target_function in special_names):
    run_compute(target_function, pfunc_CHROMPOLY, cmd_insert, targets=targets)

    cmd_mark_computed = '''
    INSERT OR IGNORE INTO computed (function_name) VALUES (?);'''
    sconn.execute(cmd_mark_computed, (target_function,))
    sconn.commit()

# Debug code below
# for g_id,adj,args in
#    print g_id, pfunc_CHROMPOLY((g_id,adj,args))
#
#g_itr    = select_itr(conn, cmd_grab)
# for g,adj in g_itr:
#    print pfunc_LAP((g,adj))
