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


logging.info("Loading stripped OEIS")
f_strip_OEIS = os.path.join("database","stripped_OEIS.txt")
'''
OEIS = {}
with open(f_strip_OEIS) as FIN:
    for line in FIN:
        name, seq = None, []
        line = line.split()
        name = line[0]
        seq = line[1][1:-1].split(',')
        if len(seq)>2:
            seq  = map(int,seq)
            # Only keep positive seqeuences
            if len([x for x in seq if x>=0]) == len(seq):
                OEIS[name] = seq
'''        
with open(f_strip_OEIS) as FIN:
    OEIS = FIN.read()

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

#kwds = ['A015273', '136586400868021924']
#for x in match_lines(OEIS, 'A015273'):
#    print x
#exit()


# Build the mapping for unique_invariant_val
unique_dict = dict(grab_all(seq_conn, '''
SELECT unique_invariant_id, invariant_val_id from unique_invariant_val'''))

# Build the mapping for ref_invariants
ref_invariant_dict = dict(grab_all(seq_conn, '''
SELECT invariant_id, function_name from ref_invariant_integer'''))

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

def subfinder(mylist, pattern):
    pattern = set(pattern)
    return [x for x in mylist if x in pattern]

for key in sorted(SEQ_TEXT.keys()):

    seq_nums = SEQ_TEXT[key]
    seq_str = ','.join(str(seq_nums)[1:-1].replace(',','').split())

    print "******************************"
    print key, seq_str
    z = str(seq_nums[-5:]).replace(' ','')[1:-1]
    for line in match_lines(OEIS,z):
        name, seq = None, []
        line = line.split()
        name = line[0]
        seq = line[1][1:-1].split(',')
        print url.format(name), ','.join(seq[:15])

    





