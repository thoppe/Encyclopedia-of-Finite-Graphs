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
import collections
def count_cardinality(key, unique):

    UX = np.zeros(shape=(unique.shape[0],len(N_RANGE)),
                  dtype=np.uint32)
    
    for i,N in enumerate(N_RANGE):
        dset = H5[N][key][:]
        for j,val in enumerate(unique):
            seq_x = ((dset == val).sum(axis=1) == unique.shape[1]).sum()
            UX[j][i] = seq_x
    print unique
    print UX

    exit()

def cardinality_compute_keys():
    # Iterator over the keys to compute
    #cmd_import = "from invariants.{} import {} as _func\nfunc = _func()"
    for group in options["sequence_options"]["cardinality_sequence_groups"]:
        for key in options["invariant_calculations"][group]:
            #exec cmd_import.format(group,key)
            yield group,key


for group,key in cardinality_compute_keys():
    key = "automorphism_group_n"
    
    h5_group = h5_seq.require_group(key)
    unique   = find_unique_items(key)
    unique_dset = h5_group.create_dataset("unique", data=unique)

    count_cardinality(key, unique)
    #print group, key, unique_dset
             

key = "automorphism_group_n"

#print H5[7][key]==[8]
#exit()

#key = "fractional_chromatic_number"
#print find_unique_items(key)
