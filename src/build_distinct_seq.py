import logging, argparse, os
import subprocess
from helper_functions import load_graph_database, load_distinct_database
from helper_functions import load_sql_script, select_itr, load_options
from helper_functions import grab_vector, grab_all

desc   = '''
Build sequences from distinct counts 
(e.g. number of automorhism groups for a given size n.'''
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())
N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Load the list of invariants to compute
distinct_seq_names = load_options()["distinct_sequences"]

##########################################################################

# Load the special database
sconn = load_graph_database(N,check_exist=True, special=True)
cmd_get_id = '''SELECT DISTINCT(graph_id) FROM {}'''

dconn = load_distinct_database(check_exist=False)
load_sql_script(dconn, "templates/distinct.sql")

# Create an index on graph_id if it doesn't exist yet!
cmd_index = '''CREATE INDEX IF NOT EXISTS idx_{} ON {} (graph_id)'''
for name in distinct_seq_names:
    sconn.execute(cmd_index.format(name,name))
sconn.commit()

# If forced, drop the terms previously computed
cmd_remove = '''DELETE FROM distinct_sequence WHERE N=(?) AND function_name=(?)'''
if cargs["force"]:
    for name in distinct_seq_names:
        dconn.execute(cmd_remove,(N,name))

# Skip terms that have already been computed
cmd_computed = '''SELECT function_name FROM distinct_sequence WHERE N=(?)'''
known_terms = set(grab_vector(dconn, cmd_computed, (N,)))

for term in known_terms.intersection(distinct_seq_names):
    del distinct_seq_names[term]

##########################################################################

def build_collection(target_function, target_columns):
    g_id_itr = select_itr(sconn,cmd_get_id.format(target_function))

    cmd_get_seq = '''
    SELECT {cols} FROM {func} WHERE graph_id=(?) ORDER BY {cols}'''
    cmd_get_seq = cmd_get_seq.format(cols=target_columns, func=target_function)

    def format_collection_query(g_id):
        vals = grab_all(sconn,cmd_get_seq,g_id)
        return tuple(vals)

    f_sort = "distinct_sort_{}_{}".format(target_function, N)
    with open(f_sort,'w') as FOUT:
        for k,g_id in enumerate(g_id_itr):
            vals = format_collection_query(g_id)
            FOUT.write(str(vals)+'\n')

    # Use unix to count
    msg = "Sorting distinct terms in {} ({})".format(target_function,N)
    logging.info(msg)

    cmd_count_sorted = "sort -g {} | uniq | wc -l".format(f_sort)
    count = int(subprocess.check_output(cmd_count_sorted,shell=True))

    if os.path.exists(f_sort):
        os.remove(f_sort)
    return count

for target_function, target_columns in distinct_seq_names.items():

    msg = "Computing distinct terms in {} ({})".format(target_function,N)
    logging.info(msg)

    count = build_collection(target_function, target_columns)
    cmd_insert = '''INSERT INTO distinct_sequence 
    (function_name, N, coeff) VALUES ("{}",{},{})'''
    cmd = cmd_insert.format(target_function, N, count)
    dconn.execute(cmd)
    dconn.commit()
        
