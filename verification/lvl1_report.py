import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from src.helper_functions import load_graph_database
from src.helper_functions import attach_ref_table, load_sql_script
from src.helper_functions import attach_table, generate_database_name
from src.helper_functions import grab_vector, grab_all, grab_scalar

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

# Build the lookup table
cmd = '''SELECT function_name,invariant_id FROM ref_invariant_integer 
ORDER BY invariant_id'''
ref_lookup = dict( grab_all(seq_conn,cmd) )
ref_lookup_inv = {v:k for k, v in ref_lookup.items()}
func_names = ref_lookup.keys()

logging.info("Loading level 1 sequences")

cmd_select_interesting = '''
SELECT sequence_id FROM stat_sequence
WHERE query_level=1 AND non_zero_terms>4'''

interesting_idx = set(grab_vector(seq_conn, cmd_select_interesting))

cmd_grab_all = '''
SELECT * FROM sequence AS a
JOIN ref_sequence_level1 AS b
ON a.sequence_id = b.sequence_id
WHERE query_level = 1
ORDER BY a.sequence_id
'''

def is_trivial(seq):
    # Check if seq is all ones or zeros
    return len(set(seq)) <= 2

SEQS = collections.OrderedDict()
for items in grab_all(seq_conn, cmd_grab_all):
    s_id = items[0]
    q_level = items[1]
    seq = items[2:12]
    
    if s_id in interesting_idx and not is_trivial(seq):
        conditional, invar_val, value = items[-3:]
        function_name = ref_lookup_inv[invar_val]
        key = "{}{}{}".format(function_name,conditional,value)
        SEQS[key] = seq
        print key, seq
exit()


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
        
logging.info("Checking level 1 sequences against OEIS")

f_output = "verification/raw_lvl1.md"
FOUT    = open(f_output,'w')

url = "https://oeis.org/{}"
output_str = "+ [`{seq_name}`]({url}) `{seq_text}`"

for key in SEQS:
    seq_nums = SEQS[key]
    z = str(seq_nums[-3:]).replace(' ','')[1:-1]
    matches = match_lines(OEIS,z)
    #print seq_nums, len(list(matches))
    seq_str = ','.join(str(seq_nums).replace(',','').split())[1:-1]
    s_base = "*`{}`*, `{}`".format(key,seq_str)

    FOUT.write(s_base+'\n')

    counter = 0
    for line in matches:
        counter += 1
        name, seq = None, []
        line = line.split()
        name = line[0]
        seqx = line[1][1:-1].split(',')
        url_text = url.format(name)
        s = output_str.format(seq_name = name, 
                              seq_text = ','.join(seqx[:12]),
                              url = url_text)
        FOUT.write(s+'\n')
        if counter>10:break

    FOUT.write('\n')
    logging.info(s_base + " " + str(counter))
