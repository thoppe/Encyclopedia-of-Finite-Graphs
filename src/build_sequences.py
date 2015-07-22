import logging
import argparse
import os
import helper_functions as helper
import h5py
import numpy as np

desc = "Builds the invariant tables"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-o', '--options',
                    default="options_simple_connected.json",
                    help="option file")
parser.add_argument('-d', '--debug',
                    default=False,action="store_true",
                    help="Turns off multiprocessing")
parser.add_argument('-v', '--verbose',
                    default=False,action="store_true",
                    help="Prints every output")
parser.add_argument('-f', '--force', default=False,
                    action='store_true')

cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

invariant_types = ["polynomial", "fraction",
                   "integer", "boolean", "subgraph"]

# Load the options
options = helper.load_options(cargs["options"])
cargs.update(options)

# Create the sequence storage file
f_database_sequence = helper.get_database_sequence(cargs)
if not os.path.exists(f_database_sequence) or cargs["force"]:
    h5py.File(f_database_sequence,'w').close()
else:
    msg = "Will not overwrite sequences information, exiting"
    logging.error(msg)
    exit()
h5_seq = h5py.File(f_database_sequence,'r+')

# Determine the span of N to compute
N_RANGE = range(options["sequence_options"]["min_N"],
                options["sequence_options"]["max_N"]+1)

# Load the database tables
H5 = dict()
for N in N_RANGE:
    item = options.copy()
    item["N"] = N
    f_h5 = helper.get_database_invariants(item)
    H5[N] = h5py.File(f_h5,'r')

########################################################################
# Find and mark the unique values

def numpy_unique_rows(A):
    # function from http://stackoverflow.com/a/16971324/249341
    b = A[np.lexsort(A.T)]
    b = b[np.concatenate(([True], np.any(b[1:] != b[:-1],axis=1)))]
    return b

def find_unique_items(key):
    # Finds values unique to all N
    unique_block = [numpy_unique_rows(H5[N][key][:]) for N in N_RANGE]
    return numpy_unique_rows(np.vstack(unique_block))

########################################################################
# Count cardinality

def count_cardinality(key, unique):

    UX = np.zeros(shape=(unique.shape[0],len(N_RANGE)),
                  dtype=np.uint32)
    
    for i,N in enumerate(N_RANGE):
        dset = H5[N][key][:]
        for j,val in enumerate(unique):
            seq_x = ((dset == val).sum(axis=1) == unique.shape[1]).sum()
            UX[j][i] = seq_x
            
    return UX

def cardinality_compute_keys():
    # Iterator over the keys to compute
    for group in options["sequence_options"]["cardinality_sequence_groups"]:
        for key in options["invariant_calculations"][group]:
            if key not in options["sequence_options"]["cardinality_ignored_invariants"]:
                yield group,key

########################################################################
# Determine which seqeuences are "interesting", at least 3 unique non zero terms
def compute_interesting_vector(sequences):
    seq_interest = np.zeros(sequences.shape[0],dtype=np.bool)
    for i,seq in enumerate(sequences):
        useq = np.unique(seq)
        useq = useq[useq > 0]
        seq_interest[i] = useq.size >= 3
    return seq_interest




for group,key in cardinality_compute_keys():
    
    h5_group = h5_seq.require_group(key)
    unique   = find_unique_items(key)
    h5_group.create_dataset("unique", data=unique)

    single_seq  = count_cardinality(key, unique)
    h5_group.create_dataset("sequences", data=single_seq)

    interest_vec = compute_interesting_vector(single_seq)
    h5_group.create_dataset("interesting", data=interest_vec)

    msg = "Completed sequence computation for {} {}".format(key,single_seq.shape)
    logging.info(msg)
