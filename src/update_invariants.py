import logging
import argparse
import inspect
import itertools
import collections
from helper_functions import (load_graph_database, select_itr,
                              grab_vector, grab_all, grab_scalar,
                              import_csv_to_table, compute_parallel,
                              grab_col_names, load_options)

desc = "Updates the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('--chunksize', type=int,
                    help="Entries to compute before insert is called",
                    default=1000)

msg = "Runs the computation in debug mode [not parallel, no commit]"
parser.add_argument('--debug', default=False, action="store_true",
                    help=msg)

msg = "Runs the in serial mode [no parallel]"
parser.add_argument('--no_parallel', default=False, action="store_true",
                    help=msg)

cargs = vars(parser.parse_args())
N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the database
conn  = load_graph_database(cargs["N"])
sconn = load_graph_database(cargs["N"], special=True)

logging.info("Starting invariant calculation for {N}".format(**cargs))

options = load_options()
invariant_names = options["invariant_function_names"]

# Create a mapping to all the known invariant functions
import invariants
invariant_funcs = dict(inspect.getmembers(invariants,
                                          inspect.isfunction))

# Make sure all invariant functions are defined
for name in invariant_names:
    if name not in invariant_funcs:
        err = "Invariant function {} not defined".format(name)
        raise KeyError(err)

# Insert the list of invariants to compute, ignore if already done
cmd_insert_names = '''
INSERT OR IGNORE INTO invariant_integer_functions
(function_name) VALUES (?)
'''
name_ITR = zip(*[invariant_names])
conn.executemany(cmd_insert_names, name_ITR)
conn.commit()

# Get the invariant_ids
cmd_get_invariant_ids = '''
SELECT function_name, invariant_id FROM
invariant_integer_functions
'''
invariant_id_lookup = dict(grab_all(conn,cmd_get_invariant_ids))

# List any special rules for the invariants
special_invariants = {
    "n_cycle_basis": "cycle_basis",
    "is_tree": "cycle_basis",
    "girth": "cycle_basis",
    "circumference": "cycle_basis",
    "n_edge": "degree_sequence",
    "n_endpoints": "degree_sequence",
    "is_k_regular": "degree_sequence",
    "chromatic_number": "tutte_polynomial",
    "has_fractional_duality_gap_vertex_chromatic":
    "fractional_chromatic_number",
    "n_independent_vertex_sets": "independent_vertex_sets",
    "maximal_independent_vertex_set": "independent_vertex_sets",
    "n_independent_edge_sets": "independent_edge_sets",
    "maximal_independent_edge_set": "independent_edge_sets",
}

######################################################################

# Allocate the space for all the invariants
cmd_allocate = '''
INSERT INTO invariant_integer (graph_id, invariant_id)
VALUES (?,{})
'''

cmd_check_if_allocated = '''
SELECT COUNT(*) FROM invariant_integer
WHERE invariant_id=? LIMIT 1
'''
msg = "Allocating space for {}"

for name in invariant_names:
    idx = invariant_id_lookup[name]
    is_allocated = grab_scalar(conn, cmd_check_if_allocated, (idx,))

    if not is_allocated:
        logging.info(msg.format(name))
        cmd = cmd_allocate.format(idx)
        ITR = conn.execute("SELECT graph_id FROM graph")
        conn.executemany(cmd, ITR)

conn.commit()


######################################################################

def graph_target_iterator(func_name):

    idx = invariant_id_lookup[name]
    cmd_grab = '''
        SELECT A.graph_id, A.adj FROM graph AS A
        JOIN invariant_integer B ON A.graph_id=B.graph_id
        WHERE B.value IS NULL
        AND   B.invariant_id=?
    '''
    cursor = conn.execute(cmd_grab, (idx,))

    for g_id, adj in cursor:
        yield (g_id, adj, {"N": N})



def iterator_degree_sequence(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT degree FROM degree_sequence WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["degree_sequence"] = grab_vector(sconn, cmd, (g_id,))
        yield (g_id, adj, args)


def iterator_cycle_basis(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT cycle_k,idx FROM cycle_basis WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        cycle_basis = grab_all(sconn, cmd, (g_id,))
        if cycle_basis[0][0] == u"None":
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
        args["tutte_polynomial"] = grab_all(sconn, cmd, (g_id,))
        yield (g_id, adj, args)


def iterator_fractional_chromatic_number(func_name):
    itr = graph_target_iterator(func_name)
    cmd_f = '''SELECT a,b FROM fractional_chromatic_number WHERE graph_id=(?) LIMIT 1'''
    cmd_t = '''SELECT x_degree,y_degree,coeff FROM tutte_polynomial WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["fractional_chromatic_number"] = grab_all(sconn, cmd_f, (g_id,))[0]
        args["tutte_polynomial"] = grab_all(sconn, cmd_t, (g_id,))
        yield (g_id, adj, args)


def iterator_IVS(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT vertex_map FROM independent_vertex_sets WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["independent_vertex_sets"] = grab_all(sconn, cmd, (g_id,))
        yield (g_id, adj, args)


def iterator_IES(func_name):
    itr = graph_target_iterator(func_name)
    cmd = '''SELECT edge_map FROM independent_edge_sets WHERE graph_id=(?)'''

    for g_id, adj, args in itr:
        args["independent_edge_sets"] = grab_all(sconn, cmd, (g_id,))
        yield (g_id, adj, args)

######################################################################

# Identify the invariants yet to be computed
cmd_find_remaining = '''
SELECT function_name FROM invariant_integer_functions
WHERE is_computed=0
'''
remaining_invariant_functions = grab_vector(conn,cmd_find_remaining)
ignored_invariants = []

cmd_mark_success = '''
UPDATE invariant_integer_functions SET
is_computed=1
WHERE function_name = ?
'''

compute_invariant_functions = [x for x in remaining_invariant_functions
                               if x not in ignored_invariants]

special_iterator_mapping = {
    "degree_sequence": iterator_degree_sequence,
    "cycle_basis": iterator_cycle_basis,
    "tutte_polynomial": iterator_tutte_polynomial,
    "fractional_chromatic_number": iterator_fractional_chromatic_number,
    "independent_vertex_sets": iterator_IVS,
    "independent_edge_sets": iterator_IES,
}

#if compute_invariant_functions:
#    msg = "Remaining invariants to compute {}"
#    logging.info(msg.format(compute_invariant_functions))


for func_name in compute_invariant_functions:

    msg = "Starting calculation for {name}"
    logging.info(msg.format(name=func_name))

    function_idx = invariant_id_lookup[func_name]
    
    cmd_insert = '''
      UPDATE invariant_integer
      SET value=?
      WHERE graph_id=?
      AND   invariant_id={}
      '''.format(function_idx)

    import_csv_to_table(func_name, N, conn, cmd_insert)

    if func_name not in special_invariants:
        itr = graph_target_iterator(func_name)
        
    elif special_invariants[func_name] in special_iterator_mapping:
        special_name = special_invariants[func_name]
        itr = special_iterator_mapping[special_name](func_name)
    else:
        err_msg = "Invariant {} unknown! Skipping.".format(func_name)
        print special_invariants
        raise SyntaxError(err_msg)

    func = invariant_funcs[func_name]
    targets = itr

    def pfunc(items):
        (g_id, adj, args) = items
        result = int(func(adj, **args))

        msg = "Computing {} for graph_id {}".format(func_name, g_id)
        if (g_id-1)%1000==0:
            logging.info(msg)
        
        return result, g_id

    logging.info("Computing N={}, {} ".format(N, func_name))

    if not cargs["debug"]:

        if not cargs["no_parallel"]:
            import multiprocessing
            P = multiprocessing.Pool()
            P_ITR = P.imap(pfunc, targets)
        else:
            P_ITR = itertools.imap(pfunc, targets)
            
        conn.executemany(cmd_insert, P_ITR)
        conn.execute(cmd_mark_success, (func_name,))
        conn.commit()
        logging.info("Completed {}".format(func_name))

        if not cargs["no_parallel"]:
            P.close()
            P.join()
            P.terminate()
            del P
            
        

    else:
        print func_name
        for (g_id, adj, args) in itr:
            result = func(adj, **args)
            print g_id, adj, result


# Create any missing indicies
cmd_index = '''
CREATE INDEX IF NOT EXISTS
idx_invariant_id ON
invariant_integer (invariant_id ASC)'''
logging.info("Creating indices {N}".format(N=N))

conn.executescript(cmd_index.format(name=name))
conn.commit()
conn.close()
