import logging
import argparse
import os
import helper_functions as helper
import h5py

desc = "Updates the special invariants for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('-o', '--options',
                    default="options_simple_connected.json",
                    help="option file")
parser.add_argument('-d', '--debug',
                    default=False,action="store_true",
                    help="Turns off multiprocessing")
parser.add_argument('-f', '--force', default=False, action='store_true')
cargs = vars(parser.parse_args())
N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the options
options = helper.load_options(cargs["options"])

# Combine the options together with cargs
cargs.update(options)

f_database = helper.get_database_graph(cargs)
h5_graphs = h5py.File(f_database,'r')
graphs = h5_graphs["graphs"]

# Count the number of graphs
gn = graphs.shape[0]

f_database_special = helper.get_database_special(cargs)
if not os.path.exists(f_database_special) or cargs["force"]:
    h5py.File(f_database_special,'w').close()

h5s = h5py.File(f_database_special,'r+')

######################################################################
# Allocate space for all the data
msg = "Allocating space for special invariants {graph_types} ({N})"
logging.info(msg.format(**cargs))

h5args = {'dtype':'int32',
          'compression':'gzip',
          'compression_opts':9}

datashapes = {
    "degree_sequence" :N,
    "characteristic_polynomial":N+1,
    "laplacian_polynomial":N+1,    
    "fractional_chromatic_number":2,
    "chromatic_polynomial":N+1,
}

datasets = {}

for key in options["special_function_names"]:

    shape = (gn, datashapes[key])
    dset = h5s.require_dataset(key,shape=shape,**h5args)
    
    if "compute_start" not in dset.attrs:
        dset.attrs["compute_start"] = 0

    datasets[key] = dset
  

###################################################################

import invariants

# Load the requirements
INV_REQ = invariants.invariant_requirements

###################################################################

thing = [
    "degree_sequence",
    "characteristic_polynomial",
    "laplacian_polynomial",   
    "fractional_chromatic_number",
    "chromatic_polynomial",
    ]
#thing = [thing,]

for key in thing:

    dset = datasets[key]
    remaining_n = gn-dset.attrs["compute_start"]

    print "{} left for {}".format(remaining_n,key)
    func = getattr(invariants, "special_{}".format(key))

    offset = dset.attrs["compute_start"]
    

    req_list = [(req, h5s[req]) for req in INV_REQ[key]]
    GITR = helper.graph_iterator(graphs, N,
                                 requirement_db_list=req_list,
                                 offset=offset)

    with helper.parallel_compute(GITR,func,cargs["debug"]) as ITR:
        for k,result in enumerate(ITR):
            idx = k+offset

            #print "Computing {}, {}".format(key, idx)
            
            dset[idx] = result
            dset.attrs["compute_start"] = idx+1
            

print "CLEANUP FROM HERE!"
print "ALLOW SAFE EXITS FROM MULTIPROCESSING!"
print "GET __MAIN__ tests working again!

exit()

######################################################################
# Helper commands




def run_compute(function_name, pfunc, cmd_insert, targets=None):

    cmd_insert = cmd_insert.format(function_name)
    #cmd_count = '''SELECT COUNT(DISTINCT graph_id) FROM {}'''
    #g_id_n = grab_scalar(sconn, cmd_count.format(function_name))
    # if g_id_n == gn: return True

    #msg = "Computing {} ({}/{})"
    #logging.info(msg.format(function_name, gn-g_id_n,gn))
    index_name = "idx_{}".format(function_name)

    cmd_grab_targets = '''
    SELECT graph_id,adj FROM graph
    WHERE graph_id NOT IN (SELECT graph_id FROM {})
    '''
    
    cmd = cmd_grab_targets.format(function_name)
    if targets is None:
        targets = select_itr(conn, cmd, chunksize=10000)

    # Drop an index if it exists
    cmd_drop = '''DROP INDEX IF EXISTS "{}"'''
    sconn.execute(cmd_drop.format(index_name,))

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

######################################################################
# First compute the degree sequence

target_function = "degree_sequence"

def pfunc_degree(item):
    (g_id, adj) = item
    return g_id, invariants.special_degree_sequence(adj, N=N)

cmd_insert = '''INSERT INTO {} (graph_id, degree) VALUES (?,?)'''
check_computed(target_function, pfunc_degree, cmd_insert)

######################################################################
# Now compute the fractional chromatic number

target_function = "fractional_chromatic_number"


def pfunc_frac_chrom(item):
    (g_id, adj) = item
    return g_id, invariants.fractional_chromatic_number(adj, N=N)

cmd_insert = '''INSERT INTO {} (graph_id, a, b) VALUES (?,?,?)'''
check_computed(target_function, pfunc_frac_chrom, cmd_insert)

######################################################################
# Now compute the Tutte polynomials

target_function = "tutte_polynomial"


def pfunc_tutte(item):
    (g_id, adj) = item
    return g_id, invariants.special_polynomial_tutte(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, x_degree, y_degree, coeff) VALUES (?,?,?,?)'''
check_computed(target_function, pfunc_tutte, cmd_insert)

######################################################################
# Now compute the cycle basis

target_function = "cycle_basis"


def pfunc_cycle_basis(item):
    (g_id, adj) = item
    return g_id, invariants.special_cycle_basis(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, cycle_k, idx) VALUES (?,?,?)'''
check_computed(target_function, pfunc_cycle_basis, cmd_insert)

######################################################################
# Now compute the independent vertex sets

target_function = "independent_vertex_sets"


def pfunc_IVS(item):
    (g_id, adj) = item
    return g_id, invariants.special_independent_vertex_sets(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, vertex_map) VALUES (?,?)'''
check_computed(target_function, pfunc_IVS, cmd_insert)

######################################################################
# Now compute the independent edge sets

target_function = "independent_edge_sets"


def pfunc_IES(item):
    (g_id, adj) = item
    return g_id, invariants.special_independent_edge_sets(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, edge_map) VALUES (?,?)'''
check_computed(target_function, pfunc_IES, cmd_insert)

######################################################################
# Now compute the graph Laplacian

target_function = "laplacian_polynomial"


def pfunc_LAP(item):
    (g_id, adj) = item
    return g_id, invariants.special_laplacian_polynomial(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, x_degree, coeff) VALUES (?,?,?)'''
check_computed(target_function, pfunc_LAP, cmd_insert)

######################################################################
# Now compute the characteristic polynomial of the adj matrix

target_function = "characteristic_polynomial"


def pfunc_CHARPOLY(item):
    (g_id, adj) = item
    return g_id, invariants.special_characteristic_polynomial(adj, N=N)

cmd_insert    = '''INSERT INTO {}
(graph_id, x_degree, coeff) VALUES (?,?,?)'''
check_computed(target_function, pfunc_CHARPOLY, cmd_insert)

######################################################################
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


def pfunc_CHROMPOLY(item):
    (g_id, adj, args) = item
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
