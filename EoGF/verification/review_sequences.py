import logging
import argparse
import json
import sqlite3

# Allow a local import to parent directory from a non-package
from os import sys, path
parent_dir = path.dirname(path.dirname(path.abspath(__file__)))
sys.path.append(parent_dir)

import helper_functions as helper

desc = "Views the sequences for submission to OEIS."
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-o', '--options',
                    default="options_simple_connected.json",
                    help="option file")

cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the options
options = helper.load_options(cargs["options"])
cargs.update(options)

f_seq_info = "sequence_info.sqlite"
conn = sqlite3.connect(f_seq_info)

columns = "graph_types","invariant_name","invariant_type","cardinality_value","computer_description","OEIS_ref","sequence","unprocessed_flag"

cmd_select_new = '''
SELECT {} FROM sequence_info
WHERE
graph_types=(:graph_types) AND
invariant_type=(:invariant_type) AND
unprocessed_flag=1
'''.format(','.join(columns))

query_args = cargs.copy()
query_args["invariant_type"] = "distinct"
cursor = conn.execute(cmd_select_new,query_args)

for data in cursor:
    item = dict(zip(columns,data))
    print json.dumps(item,indent=2)
    exit()
