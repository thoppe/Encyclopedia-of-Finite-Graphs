import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from src.helper_functions import load_graph_database, grab_all
from src.helper_functions import attach_ref_table, load_sql_script
from src.helper_functions import attach_table, generate_database_name

desc   = "Make a report of level 1 sequences"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
seq_conn = sqlite3.connect(f_seq_database, check_same_thread=False)
attach_ref_table(seq_conn)

# Load the entire stripped file as raw text
logging.info("Loading stripped OEIS")
f_strip_OEIS = os.path.join("database","stripped_OEIS.txt")
with open(f_strip_OEIS) as FIN:
    OEIS = FIN.read()

# Build an indexer

from acora import AcoraBuilder

def match_lines(s, *keywords):
     builder = AcoraBuilder('\r', '\n', *keywords)
     ac = builder.build()

     line_start = 0
     matches = False
     for kw, pos in ac.finditer(s):
         if kw in '\r\n':
             if matches:
                  yield s[line_start:pos]
                  matches = False
             line_start = pos + 1
         else:
             matches = True
     if matches:
         yield s[line_start:]

cmd_find_all = '''
SELECT hash, function_name, conditional, C.value, * FROM sequence as A
JOIN ref_sequence as B
ON A.sequence_id = B.sequence_id
JOIN unique_invariant_val as C
ON B.unique_invariant_id = C.unique_invariant_id
JOIN ref_invariant_integer AS D
ON C.invariant_val_id = D.invariant_id
WHERE non_zero_terms>=4
'''

logging.info("Loading level 1 sequences")

SEQ = collections.defaultdict(list)
for item in grab_all(seq_conn,cmd_find_all):
    hash_val = item[0]
    remaining_data = item[1:]
    SEQ[hash_val].append(remaining_data)

SEQ_TEXT = {}

for key in SEQ:
    results = SEQ[key]
    S = []
    for item in results:
        name, conditional, value = item[:3]
        s = "{}{}{}".format(name,conditional,value)
        S.append(s)

    output_key = "[%s]"%','.join(S)

    low_n = 1
    high_n = 10
    seq_nums = item[3+low_n:3+high_n+1]   

    if (np.array(seq_nums)>1).any():
        SEQ_TEXT[output_key] = seq_nums


logging.info("Checking level 1 sequences against OEIS")

url = "https://oeis.org/{}"
output_str = "[{seq_name}]({url}) {seq_text}"

def subfinder(mylist, pattern):
    pattern = set(pattern)
    return [x for x in mylist if x in pattern]

for key in sorted(SEQ_TEXT.keys()):

    seq_nums = SEQ_TEXT[key]
    seq_str = ','.join(str(seq_nums)[1:-1].replace(',','').split())

    print "---------------------------"
    s = "**`{}`**, `{}`".format(key,seq_str)
    print s
    logging.info(s)

    z = str(seq_nums[-5:]).replace(' ','')[1:-1]
    for line in match_lines(OEIS,z):
        name, seq = None, []
        line = line.split()
        name = line[0]
        seq = line[1][1:-1].split(',')
        url_text = url.format(name)

        s = output_str.format(seq_name = name, 
                              seq_text = ','.join(seq[:15]),
                              url = url_text)
        print s
        logging.info(s)

    





