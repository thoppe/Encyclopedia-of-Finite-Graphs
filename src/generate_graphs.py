import logging
import argparse
import os
import subprocess
import itertools
import numpy as np
import h5py
import json

import helper_functions as helper

_max_uint_size = 18446744073709551615
_nauty_geng_exec = 'src/nauty/geng'
_nauty_showg_exec = 'src/nauty/showg'

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

f_database = helper.get_database_graph(cargs)

if os.path.exists(f_database) and not cargs["force"]:
    err = "Database {N} has been created. Skipping generation."
    logging.info(err.format(**cargs))
    exit()

if os.path.exists(f_database):
    logging.warning("Removing database {}".format(f_database))

######################################################################

def nauty_simple_graph_itr(**args):
    ''' Creates a generator for all simple graphs using nauty '''

    cmd = "{geng} {N} -cq | {showg} -eq -l0"
    cmd = cmd.format(geng=_nauty_geng_exec,
                     showg=_nauty_showg_exec,
                     **args)

    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    while True:
        header_line = proc.stdout.readline()
        edge_line = proc.stdout.readline()
        if not header_line:
            break
        yield edge_line.strip()

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
logging.info("Generating graphs in parallel from nauty")

all_graph_ITR = nauty_simple_graph_itr(**cargs)

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


