import numpy as np
import logging, argparse, inspect, os, collections, json
from helper_functions import load_graph_database, select_itr
from helper_functions import grab_vector, grab_all
from helper_functions import compute_parallel, grab_col_names

desc   = "Updates the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=1000)
help_msg = "Runs the computation in debug mode [not parallel, no commit]"
parser.add_argument('--debug',default=False,action="store_true",
                    help=help_msg)

cargs = vars(parser.parse_args())
N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the database
conn  = load_graph_database(cargs["N"])
sconn = load_graph_database(cargs["N"], special=True)

logging.info("Starting invariant calculation for {N}".format(**cargs))

# Load the list of invariants to compute
f_invariant_json = os.path.join("templates","ref_invariant_integer.json")
with open(f_invariant_json,'r') as FIN:
    invariant_names = json.loads(FIN.read())["invariant_function_names"]

# Create a mapping to all the known invariant functions
import invariants
invariant_funcs = dict(inspect.getmembers(invariants,inspect.isfunction))

# Make sure all invariant functions are defined
for name in invariant_names:
    if name not in invariant_funcs:
        err = "Invariant function {} not defined".format(name)
        raise KeyError(err)

# Get a list of the column names
col_names = grab_col_names(conn,"invariant_integer")

# Add any columns that do not exist yet
cmd_insert = '''
ALTER TABLE invariant_integer ADD COLUMN {name} INTEGER;
CREATE INDEX IF NOT EXISTS "idx_{name}" ON "invariant_integer" ("{name}" ASC);
'''
for name in invariant_names:
    if name not in col_names:
        logging.info("Adding column {name}".format(name=name))
        conn.executescript(cmd_insert.format(name=name))

# List any special rules for the invariants
special_invariants = {
    "n_cycle_basis" : "cycle_basis",
    "is_tree"       : "cycle_basis",
    "girth"         : "cycle_basis",
    "circumference" : "cycle_basis",
    "n_edge"       : "degree_sequence",
    "n_endpoints"  : "degree_sequence",
    "is_k_regular" : "degree_sequence",
    "chromatic_number" : "tutte_polynomial",
    "has_fractional_duality_gap_vertex_chromatic" : "fractional_chromatic_number",
    "n_independent_vertex_sets"      : "independent_vertex_sets",
    "maximal_independent_vertex_set" : "independent_vertex_sets",
    "n_independent_edge_sets"      : "independent_edge_sets",
    "maximal_independent_edge_set" : "independent_edge_sets",
}

#########################################################################

def graph_target_iterator(func_name):

    cmd_grab = '''
      SELECT a.graph_id, a.adj FROM graph AS a
      LEFT JOIN invariant_integer AS b
      ON a.graph_id = b.graph_id AND b.{} IS NULL
      '''.format(func_name)

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
    cmd_f = '''SELECT a,b FROM fractional_chromatic_number WHERE graph_id=(?) LIMIT 1'''
    cmd_t = '''SELECT x_degree,y_degree,coeff FROM tutte_polynomial WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["fractional_chromatic_number"] = grab_all(sconn,cmd_f,(g_id,))[0]
        args["tutte_polynomial"] = grab_all(sconn,cmd_t,(g_id,))
        yield (g_id, adj, args)

def iterator_IVS(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT vertex_map FROM independent_vertex_sets WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["independent_vertex_sets"] = grab_all(sconn,cmd,(g_id,))
        yield (g_id, adj, args)

def iterator_IES(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT edge_map FROM independent_edge_sets WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["independent_edge_sets"] = grab_all(sconn,cmd,(g_id,))
        yield (g_id, adj, args)

#########################################################################

# Identify the invariants that have been computed
cmd = '''SELECT function_name FROM computed'''
computed_invariant_functions = grab_vector(conn,cmd)
remaining_invariant_functions = [x for x in invariant_names 
                                 if x not in computed_invariant_functions]

ignored_invariants = []

cmd_mark_success = '''INSERT OR IGNORE INTO computed (function_name) VALUES (?)'''

compute_invariant_functions = [x for x in remaining_invariant_functions
                               if x not in ignored_invariants]

special_iterator_mapping = {
    "degree_sequence"  : iterator_degree_sequence,
    "cycle_basis"      : iterator_cycle_basis,
    "tutte_polynomial" : iterator_tutte_polynomial,  
    "fractional_chromatic_number" : iterator_fractional_chromatic_number,
    "independent_vertex_sets" : iterator_IVS,
    "independent_edge_sets"   : iterator_IES,
 }

if compute_invariant_functions:
    msg = "Remaining invariants to compute {}"
    #logging.info(msg.format(compute_invariant_functions))

for func_name in compute_invariant_functions:

    msg = "Starting calculation for {name}"
    logging.info(msg.format(name=name))

    if func_name not in special_invariants:
        itr = graph_target_iterator(func_name)
    elif special_invariants[func_name] in special_iterator_mapping:
        special_name = special_invariants[func_name]
        itr = special_iterator_mapping[special_name](func_name)
    else: 
        err_msg = "Invariant {} unknown! Skipping.".format(func_name)
        print special_invariants
        raise SyntaxError(err_msg)

    func    = invariant_funcs[func_name] 
    targets = itr        

    def pfunc((g_id,adj,args)):
        result = int(func(adj,**args))
        return result, ((g_id,),)
        #return g_id, ((result,),)

    cmd_insert = '''
      UPDATE invariant_integer SET {} = (?)
      WHERE  graph_id=(?)'''.format(func_name)

    logging.info("Computing N={}, {} ".format(N, func_name))

    if not cargs["debug"]:
        compute_parallel(func_name, conn, pfunc, cmd_insert,targets,N)
        conn.execute(cmd_mark_success, (func_name,)) 
        logging.info("Commiting changes")
        conn.commit()

    #else:
    #    for (g_id,adj,args) in itr:
    #        result = func(adj,**args)
    #        print g_id, adj, result


