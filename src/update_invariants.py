import numpy as np
import logging, argparse, inspect, os, csv, collections
from helper_functions import load_graph_database, select_itr
from helper_functions import grab_vector, grab_all, attach_ref_table
from helper_functions import compute_parallel

desc   = "Updates the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=1000)
cargs = vars(parser.parse_args())

N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the database
conn  = load_graph_database(cargs["N"])
sconn = load_graph_database(cargs["N"], special=True)
attach_ref_table(conn)

logging.info("Starting invariant calculation for {N}".format(**cargs))

# Create a mapping to all the known invariant functions
import invariants
invariant_funcs = dict(inspect.getmembers(invariants,inspect.isfunction))

# Get the special column names
cmd = '''SELECT * from graph LIMIT 1'''
graph_args_names = zip(*conn.execute(cmd).description)[0]

ignored_invariants = [
    "n_independent_vertex_sets", 
    "maximal_independent_vertex_set",
    "n_independent_edge_sets", 
    "maximal_independent_edge_set",
    "has_fractional_duality_gap_vertex_chromatic",
]

special_invariants = {
    "n_cycle_basis" : "cycle_basis",
    "is_tree"       : "cycle_basis",
    "girth"         : "cycle_basis",
    "circumference" : "cycle_basis",
    "n_edge"       : "degree_sequence",
    "n_endpoints"  : "degree_sequence",
    "is_k_regular" : "degree_sequence",
    "chromatic_number" : "tutte_polynomial"
}

#########################################################################

def graph_target_iterator(func_name):
    invariant_id = ref_invariant_lookup[func_name]

    cmd_grab = '''
      SELECT a.* FROM graph as a
      LEFT JOIN invariant_integer as b
      ON a.graph_id = b.graph_id AND b.invariant_id={}
      WHERE b.value IS NULL '''.format(invariant_id)

    for g_id, adj in select_itr(conn, cmd_grab) :
        yield (g_id,adj,{"N":N})

def iterator_degree_sequence(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT degree FROM degree_sequence WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["degree_sequence"] = grab_vector(sconn,cmd,(g_id,))
        yield (g_id, adj, args)

def iterator_cycle_basis(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT cycle_k,idx FROM cycle_basis WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        cycle_basis = grab_all(sconn,cmd,(g_id,))
        if cycle_basis[0][0]==u"None":
            cycle_basis = []
        else:
            # Convert the flat representation to a nested list
            cb = collections.defaultdict(list)
            for cycle_k, idx in cycle_basis:
                cb[cycle_k].append(idx)
            cycle_basis = cb.values()

        args["cycle_basis"] = cycle_basis
        yield (g_id, adj, args)

def iterator_tutte_polynomial(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT x_degree,y_degree,coeff FROM tutte_polynomial WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["tutte_polynomial"] = grab_all(sconn,cmd,(g_id,))
        yield (g_id, adj, args)

def iterator_fractional_chromatic_number(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT a,b FROM tutte_polynomial WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["fractional_chromatic_number"] = grab_all(sconn,cmd,(g_id,))
        yield (g_id, adj, args)

#########################################################################

# Identify the invariants that have not been computed
cmd = '''
SELECT function_name FROM ref_invariant_integer 
EXCEPT SELECT function_name FROM computed
'''

compute_invariant_functions = grab_vector(conn,cmd)

cmd = "SELECT function_name,invariant_id FROM ref_invariant_integer"
ref_invariant_lookup = dict(conn.execute(cmd).fetchall())

cmd_mark_success = '''
INSERT OR IGNORE INTO computed (function_name) VALUES (?)'''

compute_invariant_functions = [x for x in compute_invariant_functions 
                               if x not in ignored_invariants]

special_iterator_mapping = {
    "degree_sequence"  : iterator_degree_sequence,
    "cycle_basis"      : iterator_cycle_basis,
    "tutte_polynomial" : iterator_tutte_polynomial,  
    "fractional_chromatic_number" : iterator_fractional_chromatic_number,
 }

if compute_invariant_functions:
    msg = "Remaining invariants to compute {}"
    #logging.info(msg.format(compute_invariant_functions))


for func_name in compute_invariant_functions:

    msg = "Starting calculation for {name}"

    if func_name not in special_invariants:
        itr = graph_target_iterator(func_name)
    elif special_invariants[func_name] in special_iterator_mapping:
        special_name = special_invariants[func_name]
        itr = special_iterator_mapping[special_name](func_name)
    else: 
        err_msg = "Invariant {} unknown! Skipping.".format(func_name)
        raise SyntaxError(err_msg)

    func    = invariant_funcs[func_name] 
    targets = itr        
    invariant_id = ref_invariant_lookup[func_name]

    def pfunc((g_id,adj,args)):
        return g_id, ((invariant_id, int(func(adj,**args)), ),)

    cmd_insert = '''
      INSERT or IGNORE INTO invariant_integer
      (graph_id, invariant_id, value) VALUES (?,?,?)'''

    logging.info("Computing N={}, {} ".format(N, func_name))
    
    compute_parallel(func_name, conn, pfunc, cmd_insert,targets,N)
    conn.execute(cmd_mark_success, (func_name,)) 
    conn.commit()

    # Debugging code
    #func   = invariant_funcs[func_name] 
    #if itr != None:
    #    print func_name
    #    for (g_id, adj, args) in itr:
    #        args["N"] = N
    #        result = func(adj,**args)
    #        print g_id, adj, result


