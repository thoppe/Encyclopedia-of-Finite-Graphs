import logging
import argparse
import os
import helper_functions as helper
import h5py
import numpy as np

desc = "Updates the special invariants for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('-o', '--options',
                    default="options_simple_connected.json",
                    help="option file")
parser.add_argument('-d', '--debug',
                    default=False,action="store_true",
                    help="Turns off multiprocessing")
parser.add_argument('-v', '--verbose',
                    default=False,action="store_true",
                    help="Prints every output")
parser.add_argument('-i', '--invariant_type',
                    default="polynomial", help="Invariant type to compute")

parser.add_argument('-f', '--force', default=False, action='store_true')
cargs = vars(parser.parse_args())
N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Validate the invariant_type
if cargs["invariant_type"] not in ["integer","polynomial","fraction"]:
    msg = "Invariant type {invariant_type} not permitted yet".format(**cargs)
    raise KeyError(msg)

# Load the options
options = helper.load_options(cargs["options"])

# Determine the invariant names
invariant_names = options["invariant_calculations"][cargs["invariant_type"]]

# Import the right library
if cargs["invariant_type"] == "polynomial":
    import invariants.polynomial as INVLIB
elif cargs["invariant_type"] == "fraction":
    import invariants.fraction as INVLIB
elif cargs["invariant_type"] == "integer":
    import invariants.integer as INVLIB
else:
    raise NotImplemented

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

msg = "Starting calculation for ({graph_types}) ({invariant_type}) ({N})"
logging.info(msg.format(**cargs))

######################################################################
# Allocate space for all the data

msg = "Allocating space for {invariant_type} invariants {graph_types} ({N})"
logging.info(msg.format(**cargs))

h5args = {'compression':'gzip',
          'compression_opts':9}

datasets    = {}
functionals = {}

for key in invariant_names:

    functionals[key] = getattr(INVLIB, key)()
    size  = functionals[key].shape(N=N)
    shape = (gn, size)

    dset = h5s.require_dataset(key,shape=shape,
                               dtype=functionals[key].dtype,
                               **h5args)
    
    if "compute_start" not in dset.attrs:
        dset.attrs["compute_start"] = 0

    datasets[key] = dset

######################################################################

msg = "Allocating space for {invariant_type} invariants {graph_types} ({N})"
logging.info(msg.format(**cargs))

for key in invariant_names:

    func = functionals[key]
    dset = datasets[key]

    offset = dset.attrs["compute_start"]
    remaining_n = gn-offset

    print "{} left for {}".format(remaining_n,key)

    req_list = []

    GITR = helper.graph_iterator(graphs, N,
                                 requirement_db_list=req_list,
                                 offset=offset)

    # Used for caching the results
    result_save_size = 100
    result_shape = (result_save_size,func.shape(N=N))
    result_block = np.zeros(result_shape, dtype=func.dtype)
    rc = 0

    with helper.parallel_compute(GITR,func,cargs["debug"]) as ITR:
        for k,result in enumerate(ITR):

            idx = k+offset

            if cargs["verbose"]:
                print idx, result            

            if rc==result_save_size: 
                print "  status ({}/{}) {}, {}".format(idx+1, gn, key, result)
                dset[idx-rc:idx] = result_block
                dset.attrs["compute_start"] = idx+1
                rc = 0
    
            result_block[rc] = result
            rc += 1

        # Save the final cached results
        idx = gn
        result_block = result_block[:rc]
        dset[idx-rc:idx] = result_block
        dset.attrs["compute_start"] = idx

print "GET __MAIN__ tests working again!"
