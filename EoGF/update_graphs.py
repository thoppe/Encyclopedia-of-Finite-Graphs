import logging
import argparse
import os
import h5py
import numpy as np

import helper_functions as helper
import graph_generators

_max_uint_size = 18446744073709551615

desc = "Builds the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('-o', '--options',
                    default="options_simple_connected.json",
                    help="option file")
parser.add_argument('-f', '--force', default=False, action='store_true')
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the options
options = helper.load_options(cargs["options"])

# Combine the options together with cargs
cargs.update(options)

# Create database directory if missing
helper.mkdir_p("database")

f_database = helper.get_database_graph(cargs)

if os.path.exists(f_database) and not cargs["force"]:
    err = "Database {N} has been created. Skipping generation."
    logging.info(err.format(**cargs))
    exit()

if os.path.exists(f_database):
    logging.warning("Removing database {}".format(f_database))

# Try to load the update function
generator_func_name = cargs["graph_generator_function"]

try:
    generator_func = getattr(graph_generators,generator_func_name)    
except:
    err = "{} is not defined in graph_generators"
    raise SyntaxError(err.format(generator_func_name))

######################################################################

__upper_matrix_index = np.triu_indices(cargs["N"])

def convert_edge_to_adj(edges):

    # Map the edge list into an index list
    edges = map(int, edges.split())
    idx = zip((edges[::2], edges[1::2]))

    # Since graph in undirected assign both sides
    A = np.zeros((cargs["N"], cargs["N"]), dtype=int)
    A[idx[0], idx[1]] = 1

    # The string representation of the upper triangular adj matrix
    au = ''.join(map(str, A[__upper_matrix_index]))

    # Convert the binary string to an int
    int_index = int(au, 2)

    assert(int_index < _max_uint_size)

    return int_index

######################################################################

# Process input in parallel
logging.info("Generating graphs from {}".format(generator_func_name))

all_graph_ITR = generator_func(**cargs)

import multiprocessing
P = multiprocessing.Pool()
ITR = P.imap(convert_edge_to_adj, all_graph_ITR)

# Convert the data to a list before storage, we must know the size beforehand
data = list(ITR)

h5   = h5py.File(f_database, 'w')
dset = h5.create_dataset("graphs",data=data,
                        dtype='uint64', compression="gzip")

actually_present = dset.shape[0]
logging.info("Database reports {} entries.".format(actually_present))

h5.close()
