from fabric.api import *

import logging
import argparse
import helper_functions as helper

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

min_N = options["sequence_options"]["min_N"]
max_N = options["sequence_options"]["max_N"]

for N in xrange(min_N, max_N+1):
    args = cargs.copy()
    args["N"] = N
    local("python src/update_graphs.py {N} -o {options}".format(**args))
    
    for inv in invariant_types:
        args["inv"] = inv
        cmd = "python src/update_invariants.py {N} -o {options} -i {inv}"
        local(cmd.format(**args))


    
    print N
