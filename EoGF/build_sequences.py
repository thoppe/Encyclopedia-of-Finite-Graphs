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
parser.add_argument('-2', '--dont_build_second_order', default=False,
                    help="Stops building the second-order sequences",
                    action='store_true')
parser.add_argument('-3', '--dont_build_third_order', default=False,
                    help="Stops building the third-order sequences",
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
    raise IOError(msg)

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

# Next build the masks and distinct sequences requested
dset_distinct  = group_distinct.create_dataset("sequences",
                                               dtype=np.int32,
                                               shape=(len(distinct_names),
                                                      len(N_RANGE)))

group_unique  = group_cardinality.create_group("unique")

MASKS = {}

for key in set(distinct_names).union(cardinality_names):
    msg = "Computing masking data for {}".format(key)
    logging.info(msg)

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

def format_sequence_name(name, val):
    val = str(val)[1:-1].replace(',','').replace(' ','_')
    val = val.replace('__','_').strip('_').strip()
    return '{}_IS_{}'.format(name, val)

def get_first_order_mask(name,val):
    unique = group_unique[name][:]
    idx = unique.tolist().index(val.tolist())
    return dict(zip(N_RANGE,[MASKS[name][N][idx] for N in N_RANGE]))
    
first_order_data = []

for name in cardinality_names:
    for val in group_unique[name][:]:
        sname = format_sequence_name(name, val)
        first_order_data.append((sname,name, val))

first_order_desc = zip(*first_order_data)[0]

group_C1 = group_cardinality.require_group("order_1")
group_C1.create_dataset("names", dtype=h5_string_dt,
                                 data=first_order_desc, **compress_args)

UX = np.zeros(shape=(len(first_order_desc),len(N_RANGE)),
              dtype=np.int32)

for i,(_,name,val) in enumerate(first_order_data):
    M   = get_first_order_mask(name,val)
    seq = [M[N].sum() for N in N_RANGE]
    UX[i] = seq

# Find out which ones are interesting
interest_vec = compute_interesting_vector(UX)

group_C1.create_dataset("interesting", data=interest_vec)
group_C1.create_dataset("sequences", data=UX)

msg = "Found {} interesting first-order seqeuences".format(interest_vec.sum())
logging.warning(msg)


########################################################################
# Build second-order+ sequences if requested

def is_true_false_invariant(name):
    # Checks if an invariant is only True or False by it's type
    
    groups = options["invariant_calculations"]
    if name in groups["subgraph"]:
        return True
    elif name in groups["boolean"]:
        return True
    else:
        return False
    

def higher_order_compute_keys(n=2):
    # Iterator over the keys to compute interesting cardinality sequences

    # Find potential candidates
    candidates = []

    for i,(_,name,val) in enumerate(first_order_data):
        
        if interest_vec[i]:
            
            # If a T/F invariant only choose the true option
            if is_true_false_invariant(name):
                if sum(val)==0:
                    continue

            candidates.append((name,i,val))

    for items in itertools.combinations(candidates, r=n):
        unique_names = set([x[0] for x in items])
        if len(unique_names) != n:
            continue
        yield items



N_cardinality_order = []

if not cargs["dont_build_second_order"]:
    N_cardinality_order.append(2)

if not cargs["dont_build_third_order"]:
    N_cardinality_order.append(3)
    
for N_cardinality in N_cardinality_order:

    print N_cardinality
    local_seq_N = len(list(higher_order_compute_keys(N_cardinality)))
    UX   = np.zeros(shape=(local_seq_N,len(N_RANGE)), dtype=np.uint32)
    IVEC = np.zeros(shape=(local_seq_N,), dtype=np.bool)
    
    higher_order_sequence_names = []

    for k,item in enumerate(higher_order_compute_keys(N_cardinality)):
        
        names, IDXS, values = zip(*item)
        snames = [format_sequence_name(name,val) for name,_,val in item]
        sname  = '_AND_'.join(snames)

        if k and k%100==0:
            msg = "Starting ({}/{}) sequence data for {}"
            msg = msg.format(k,local_seq_N-1,sname)
            logging.warning(msg)

        higher_order_sequence_names.append(sname)

        # Build mask block
        mask_block = [get_first_order_mask(name,val) for name,_,val in item]

        mul = lambda x,y: x*y
        seq = [reduce(mul, [M[N] for M in mask_block]).sum()
               for N in N_RANGE]
        UX[k] = seq


    IVEC_K = compute_interesting_vector(UX)
    msg = "Found {} interesting {}-order sequences"
    logging.info(msg.format(IVEC_K.sum(), N_cardinality))

    group_CK = group_cardinality.require_group("order_{}".format(N_cardinality))
    group_CK.create_dataset("names", dtype=h5_string_dt,
                            data=higher_order_sequence_names, **compress_args)

    group_CK.create_dataset("interesting", data=IVEC_K)
    group_CK.create_dataset("sequences", data=UX)
