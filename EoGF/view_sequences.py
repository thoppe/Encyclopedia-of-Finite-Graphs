import logging
import argparse
import os
import json
import helper_functions as helper
import h5py
import sqlite3
import numpy as np

desc = "Views the sequences for submission to OEIS."
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

# Load the options
options = helper.load_options(cargs["options"])
cargs.update(options)

# Load the seqeunce file
f_database_sequence = helper.get_database_sequence(cargs)
h5 = h5py.File(f_database_sequence,'r+')

f_seq_info = "verification/sequence_info.sqlite"
conn = sqlite3.connect(f_seq_info)

schema = '''
CREATE TABLE IF NOT EXISTS sequence_info (
    graph_types STRING,
    invariant_name STRING,
    invariant_type STRING,
    cardinality_value INT,
    computer_description STRING,
    OEIS_ref STRING,
    submit_flag BOOL DEFAULT TRUE
);
'''
conn.executescript(schema)

def generate_description(item):
    if item["invariant_type"] == "distinct":
        msg = ("Number of distinct {invariant_name} for {graph_types} "
               "graphs on N nodes")
    return msg.format(**item)#.replace("_"," ")

def build_distinct(name):
    item = {}
    item["invariant_name"] = name
    item["graph_types"]    = options["graph_types"]
    item["invariant_type"] = "distinct"
    item["computer_description"] = generate_description(item)
    item["cardinality_value"] = None

    seq = h5[name]["distinct"][:]
    item["sequence"] = ','.join(map(str,seq.tolist()))
    return item



for key in h5:
    #if "distinct" in h5[key]:
    #    item = build_distinct(key)
    #    print json.dumps(item,indent=2)
    inv_type = [g for g in options["invariant_calculations"]
                if key in options["invariant_calculations"][g]][0]

    if "sequences" in h5[key] and inv_type not in ["boolean","subgraph"]:
        ivec   = h5[key]["interesting"][:]
        unique = h5[key]["unique"][:]
        print key, unique[ivec].T, inv_type



