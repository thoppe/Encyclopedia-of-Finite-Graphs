import logging
import argparse
import os
import json
import helper_functions as helper
import h5py
import sqlite3
import numpy as np

f_seq_info = "sequence_info.sqlite"

desc = "Build a sequence database that is easily parsed. Stores in sequence_info.sqlite"

parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-o', '--options',
                    default="options_simple_connected.json",
                    help="option file")
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

conn = sqlite3.connect(f_seq_info)

schema = '''
CREATE TABLE IF NOT EXISTS sequence_info (
    graph_types STRING,
    invariant_name STRING,
    invariant_type STRING,
    cardinality_value INT,
    computer_description STRING,
    OEIS_ref STRING,
    sequence STRING,
    unprocessed_flag BOOL DEFAULT TRUE,
    UNIQUE (graph_types, invariant_name, invariant_type, cardinality_value)
);
'''
conn.executescript(schema)

cmd_insert = '''INSERT OR IGNORE INTO sequence_info VALUES (
:graph_types,
:invariant_name,
:invariant_type,
:cardinality_value,
:computer_description,
:OEIS_ref,
:sequence,
:unprocessed_flag)'''


def generate_description(item):
    if item["invariant_type"] == "distinct":
        desc = ("Number of distinct {invariant_name} for {graph_types} "
                "graphs with n vertices.")
        
    elif "order_1" in item["invariant_type"]:
        desc = ("Number of {graph_types} graphs with n vertices where "
                "{name1}={val1}")
        item["name1"],item["val1"] = item["invariant_name"].split("_IS_")
        
    elif "order_2" in item["invariant_type"]:
        desc = ("Number of {graph_types} graphs with n vertices where "
                "{name1}={val1} and {name2}={val2}.")
        split = item["invariant_name"].split("_AND_")        
        item["name1"],item["val1"] = split[0].split("_IS_")
        item["name2"],item["val2"] = split[1].split("_IS_")
    else:
        raise KeyError
    item["computer_description"] = desc.format(**item)


def build_distinct(name,seq):
    item = {}
    item["invariant_name"] = name
    item["graph_types"]    = options["graph_types"]
    item["invariant_type"] = "distinct"
    item["cardinality_value"] = 0
    item["sequence"] = ','.join(map(str,seq.tolist()))
    item["OEIS_ref"] = None
    item["unprocessed_flag"] = True
    generate_description(item)
    return item

def build_cardinality(name,seq,order_name):
    item = {}
    item["invariant_name"] = name
    item["graph_types"]    = options["graph_types"]
    item["invariant_type"] = order_name
    item["cardinality_value"] = 0
    item["sequence"] = ','.join(map(str,seq.tolist()))
    item["OEIS_ref"] = None
    item["unprocessed_flag"] = True
    generate_description(item)
    return item

def distinct_item_itr():
    gd = h5["distinct"]

    for name,seq in zip(gd["names"], gd["sequences"]):
        item = build_distinct(name,seq)        
        print json.dumps(item,indent=2)
        yield item


def cardinality_item_itr():
    group_cardinality = h5["cardinality"]
    order_list = sorted([x for x in group_cardinality.keys() if "order_"
                         in x])
    for order_n in order_list:
        gd = group_cardinality[order_n]

        for name,seq,ivec in zip(gd["names"], gd["sequences"],gd["interesting"]):
            if ivec:
                item = build_cardinality(name,seq,order_n)        
                print json.dumps(item,indent=2)
                yield item



cursor = conn.executemany(cmd_insert, distinct_item_itr())
conn.commit()
msg = "Added {} new distinct sequences to the database"
logging.info(msg.format(cursor.rowcount))


cursor = conn.executemany(cmd_insert, cardinality_item_itr())
conn.commit()
msg = "Added {} new cardinality sequences to the database"
logging.info(msg.format(cursor.rowcount))






