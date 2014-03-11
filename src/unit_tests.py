import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
import helper_functions

desc   = "Verify the sequences produced are the correct ones"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--max_n',type=int,default=7,
                    help="Maximum graph size n to compute tests")
parser.add_argument('--min_n',type=int,default=3,
                    help="Minimum graph size n to match tests")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)

graph_conn = collections.OrderedDict()
for n in range(cargs["min_n"], cargs["max_n"]+1):
    graph_conn[n] = helper_functions.load_graph_database(n)


