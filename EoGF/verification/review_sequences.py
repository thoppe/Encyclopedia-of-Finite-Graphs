import logging
import argparse
import json
import sqlite3
import requests
import bs4
import webbrowser

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

columns = ("graph_types","invariant_name","invariant_type","cardinality_value",
           "computer_description","OEIS_ref","sequence","unprocessed_flag")

cmd_select_new = '''
SELECT {} FROM sequence_info
WHERE
graph_types=(:graph_types) AND
invariant_type=(:invariant_type) AND
unprocessed_flag=1
'''.format(','.join(columns))

cmd_ignore = '''
UPDATE sequence_info
SET unprocessed_flag=0
WHERE
graph_types=(:graph_types) AND
invariant_type=(:invariant_type) AND
invariant_name=(:invariant_name) AND
cardinality_value=(:cardinality_value)
'''

cmd_save = '''
UPDATE sequence_info
SET
unprocessed_flag=0,
OEIS_ref=(:OEIS_ref)
WHERE
graph_types=(:graph_types) AND
invariant_type=(:invariant_type) AND
invariant_name=(:invariant_name) AND
cardinality_value=(:cardinality_value)
'''


def query_OEIS(sequence):
    url = "http://oeis.org/search"
    params = {"q":sequence,"fmt":""}
    r = requests.get(url,params=params)
    webbrowser.open(r.url,new=0)
    
    soup = bs4.BeautifulSoup(r.text)
    
    OEIS_ref = ""
    for link in soup.findAll("a"):
        if link["href"][:2] == "/A" and link.text.strip()[0] == "A":
            OEIS_ref = link.text.strip()

    print "Press ENTER for yes, i for ignore, s for skip."
    msg = "Tag sequence found in OEIS as [{}]?\n".format(OEIS_ref)
    response = raw_input(msg).lower().strip()

    if not response:
        item["OEIS_ref"] = OEIS_ref

    return response


query_args = cargs.copy()
query_args["invariant_type"] = "distinct"
cursor = conn.execute(cmd_select_new,query_args)

for data in cursor:
    item = dict(zip(columns,data))
    print json.dumps(item,indent=2)
    q = query_OEIS(item["sequence"]) 
    if q == "i":
        print "Marking ignored"
        conn.execute(cmd_ignore, item)
    elif q == "s":
        print "Skipping sequence"
    elif not q and item["OEIS_ref"]:
        print "SAVE"
        conn.execute(cmd_save, item)
    else:
        print "Invalid option, skipping anyways!"

    conn.commit()

