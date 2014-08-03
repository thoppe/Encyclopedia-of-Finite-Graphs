import sqlite3, logging, argparse, os, collections, json
import numpy as np
from src.helper_functions import grab_vector, grab_all, grab_scalar

desc   = "Make a report of the distinct sequences"
parser = argparse.ArgumentParser(description=desc)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database
f_distinct_database = "database/distinct_seq.db"
conn = sqlite3.connect(f_distinct_database)

# Load the list of distinct invariants
f_invariant_json = os.path.join("templates","ref_invariant_integer.json")
with open(f_invariant_json,'r') as FIN:
    distinct_seq_names = json.loads(FIN.read())["distinct_sequences"]


cmd_build_seq = '''
SELECT N,coeff FROM distinct_sequence 
WHERE function_name = "{}" ORDER BY N
'''

for name in distinct_seq_names:
    cmd = cmd_build_seq.format(name)
    n_val, seq = zip(*grab_all(conn, cmd))
    if n_val != tuple(range(1,len(n_val)+1)):
        logging.warning("N values are not sequential")
    seq = str(seq).replace('(','').replace(')','').replace(' ','')

    key = "+ `[{}]` `{}`".format(name,seq)
    print key
