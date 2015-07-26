import logging
import argparse
import os
import itertools
import helper_functions as helper
import h5py
import numpy as np

_interesting_values_required = 3

desc = "Builds the sequences from the invariant tables."
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-o', '--options',
                    default="options_simple_connected.json",
                    help="option file")
parser.add_argument('-f', '--force', default=False,
                    action='store_true')

cargs = vars(parser.parse_args())

# Start the logger
#logging.root.setLevel(logging.INFO)

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
    raise IOError

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
    return unique_block

########################################################################
# Count cardinality

def invariant_mask(key, unique):
    # For each unique value of invariant name "key", for each N, create a T/F mask

    unique_n = unique.shape[0]
    MASK = {}

    for N in N_RANGE:
        dset = H5[N][key][:]
        mask = np.zeros(shape=(unique_n,dset.shape[0]), dtype=np.bool)
        for j,val in enumerate(unique):
            mask[j] = ((dset == val).sum(axis=1) == unique.shape[1])
        MASK[N] = mask
    return MASK

def cardinality_compute_keys():
    # Iterator over the keys to compute cardinality sequences
    for group in options["sequence_options"]["cardinality_sequence_groups"]:
        for key in options["invariant_calculations"][group]:
            if key not in options["sequence_options"]["cardinality_ignored_invariants"]:
                yield str(key)

def distinct_compute_keys():
    # Iterator over the keys to compute distinct sequences
    for group in options["sequence_options"]["distinct_sequence_groups"]:
        for key in options["invariant_calculations"][group]:
            if key not in options["sequence_options"]["distinct_ignored_invariants"]:
                yield str(key)

########################################################################
# Determine which seqeuences are "interesting", at least 3 unique non zero terms
def compute_interesting_vector(sequences):
    seq_interest = np.zeros(sequences.shape[0],dtype=np.bool)
    for i,seq in enumerate(sequences):
        useq = np.unique(seq)
        useq = useq[useq > 0]
        seq_interest[i] = useq.size >= _interesting_values_required
    return seq_interest

########################################################################
# First build the sequence names for distinct and cardinality

distinct_names    = list(set(distinct_compute_keys()))
cardinality_names = list(set(cardinality_compute_keys()))

compress_args = {'compression':'gzip','compression_opts':9}
h5_string_dt  = h5py.special_dtype(vlen=bytes)

group_distinct = h5_seq.require_group("distinct")
group_distinct.create_dataset("names", dtype=h5_string_dt,
                              data=distinct_names, **compress_args)

group_cardinality = h5_seq.require_group("cardinality")
group_cardinality.create_dataset("names", dtype=h5_string_dt,
                                 data=cardinality_names, **compress_args)

# Next build the masks and distinct sequences requested
dset_distinct  = group_distinct.create_dataset("sequences",
                                               dtype=np.int32,
                                               shape=(len(distinct_names),len(N_RANGE)))

group_unique  = group_cardinality.create_group("unique")
group_mask    = group_cardinality.create_group("mask")

MASKS = {}

for key in set(distinct_names).union(cardinality_names):
    msg = "Starting sequence data for {}".format(key)
    logging.info(msg)

    h5_group = h5_seq.require_group(key)
    unique_per_N   = find_unique_items(key)

    if key in distinct_names:
        idx = distinct_names.index(key)
        seq = map(lambda x:x.shape[0], unique_per_N)
        dset_distinct[idx] = seq
    
    if key in cardinality_names:
        #msg = "Computing mask data {}".format(key)
        idx = cardinality_names.index(key)
        
        # Save the unique values for lookup
        unique = numpy_unique_rows(np.vstack(unique_per_N))
        group_unique.create_dataset(key, data=unique)

        # Save the masks in memory for later computation
        MASKS[key] = {}

        for N,mask in invariant_mask(key, unique).items():
            MASKS[key][N] = mask

########################################################################
# Now build the first order sequences

for key in cardinality_names:

    # Compute the sequences
    seq  = np.vstack([MASK[N].sum(axis=1) for N in N_RANGE]).T

    print MASKS[key]
    exit()

    #gC = h5_seq["cardinality"]
    #seq_group = gC.require_group("sequences")



    # Sanity check
    unique = gC["unique"][key]
    assert(seq.shape[0] == unique.shape[0])

    seq_group[key] = seq
    
    print key
    print seq
        

exit()


cardinality_group.create_dataset("sequence_names",dtype=dt,
                                 data=higher_order_sequence_names,
                                 **compress_args)

'''

    #single_seq  = count_cardinality(key, unique)
    #h5_group.create_dataset("sequences", data=single_seq)

    
    print single_seq
    exit()

    if key in cardinality_set:
        unique = numpy_unique_rows(np.vstack(unique_per_N))
        h5_group.create_dataset("unique", data=unique)
        
        msg = "Computing cardinality search for {} {}"
        logging.info(msg.format(key, unique.shape))

        single_seq  = count_cardinality(key, unique)
        h5_group.create_dataset("sequences", data=single_seq)

        interest_vec = compute_interesting_vector(single_seq)
        h5_group.create_dataset("interesting", data=interest_vec)
'''

########################################################################
# Build second-order+ sequences, these look different

def is_true_false_invariant(name):
    # Checks if an invariant is only True or False by it's type
    
    groups = options["invariant_calculations"]
    if name in groups["subgraph"]:
        return True
    elif name in groups["boolean"]:
        return True
    else:
        return False
    

def cardinality_higher_order_compute_keys(n=2):
    # Iterator over the keys to compute interesting cardinality sequences

    # Find potential candidates
    candidates = []
    for key in h5_seq:        
        # Only pull out first-order interesting sequences
        group = h5_seq[key]
        if key in cardinality_set and "interesting" in group:            

            interesting_idx = np.where(group['interesting'][:])[0]
            unique = group["unique"][:]

            # If a T/F invariant only choose the true option
            if is_true_false_invariant(key):
                interesting_idx = np.where(unique.T[0])[0]
            
            for idx in interesting_idx:
                value = tuple(unique[idx].tolist())
                candidates.append((key, idx, value))

    for items in itertools.combinations(candidates, r=n):
        unique_names = set([x[0] for x in items])
        if len(unique_names) != n:
            continue
        yield items



for N_cardinality in [2,3]:

    local_seq_N = len(list(cardinality_higher_order_compute_keys(N_cardinality)))
    UX   = np.zeros(shape=(local_seq_N,len(N_RANGE)), dtype=np.uint32)
    IVEC = np.zeros(shape=(local_seq_N,), dtype=np.bool)
    higher_order_sequence_names = []

    for k,item in enumerate(cardinality_higher_order_compute_keys(N_cardinality)):

        names, IDXS, values = zip(*item)
        str_vals = [str(x)[1:-1].strip(',').replace(', ','_') for x in values]

        conjoined_name = ["{}_IS_{}".format(name,val) for name,val in zip(names, str_vals)]
        conjoined_name = "_AND_".join(conjoined_name)

        msg = "Starting ({}/{}) sequence data for {}"
        msg = msg.format(k,local_seq_N,conjoined_name)
        logging.info(msg)

        higher_order_sequence_names.append(conjoined_name)

        conjoined_seq = []
        for N in N_RANGE:
            counts = np.hstack([H5[N][name][:]==x for name,x in zip(names,values)]).sum(axis=1)
            total = (counts==N_cardinality).sum()
            conjoined_seq.append(total)

        UX[k] = conjoined_seq
        
    IVEC = compute_interesting_vector(UX)

    msg = "Found {} interesting {}-order sequences".format(IVEC.sum(), N_cardinality)
    logging.info(msg)

    compress_args = {'compression':'gzip','compression_opts':9}
    
    cardinality_group = h5_seq.require_group("_higher_order_{}".format(N_cardinality))
    cardinality_group.create_dataset("sequences",data=UX,**compress_args)
    cardinality_group.create_dataset("interesting_idx",data=IVEC,**compress_args)

    dt = h5py.special_dtype(vlen=bytes)
    cardinality_group.create_dataset("sequence_names",dtype=dt,
                                     data=higher_order_sequence_names,
                                     **compress_args)

    

        
