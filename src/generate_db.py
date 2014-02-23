import sqlite3, logging, argparse, os
import multiprocessing, subprocess, itertools
import numpy as np
from helper_functions import grouper, load_template

desc   = "Builds the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('-f','--force',default=False,action='store_true')
parser.add_argument('--chunksize',type=int,
                    help="Entries to compute before insert is called",
                    default=10000)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

cargs["table_name"] = "graph{N}".format(**cargs)
f_database = 'database/{table_name}.db'.format(**cargs)

# If forced, removed the old database
if cargs["force"] and os.path.exists(f_database):
    logging.warning("Removing database %s"%f_database)
    os.remove(f_database)

# Check if database exists, if so exit!
if os.path.exists(f_database):
    err = "Database %s already exists, exiting"%f_database
    logging.warning(err)
    exit()

logging.info("Creating database "+f_database)
conn = sqlite3.connect(f_database,check_same_thread=False)



def create_table_cmd(template, **cargs):

    N = cargs["N"]
    args = cargs.copy()
    args["max_edges"] = N**2
    args["cols"] = (',\n'.join(template)).format(**args)

    cmd = "CREATE TABLE IF NOT EXISTS {table_name} ({cols})"
    cmd = cmd.format(**args)
    return cmd

# Load the template from file
f_graph_template = "templates/graph_template.txt"
template = load_template(f_graph_template)

# Create the database if it doesn't exist
cmd = create_table_cmd(template, **cargs)
conn.execute(cmd)

# Start populating it with graphs from nauty

def nauty_simple_graph_itr(**args):
    ''' Creates a generator for all simple graphs using nauty '''

    cmd = "geng {N} -cq | showg -eq -l0"
    cmd = cmd.format(**args)

    proc = subprocess.Popen([cmd],stdout=subprocess.PIPE,shell=True)
    while True:
        header_line = proc.stdout.readline()
        edge_line   = proc.stdout.readline()
        if not header_line: break
        yield edge_line.strip()

upper_matrix_index = np.triu_indices(cargs["N"])

def convert_edge_to_adj(edges):
    # Map the edge list into an index list
    edges = map(int,edges.split())
    idx = zip((edges[::2], edges[1::2]))
    
    # Since graph in undirected assign both sides
    A = np.zeros((cargs["N"],cargs["N"]),dtype=int)
    A[idx[0],idx[1]] = 1
    
    # The string representation of the upper triangular adj matrix
    au = ''.join(map(str,A[upper_matrix_index]))
    
    # Convert the binary string to an int
    int_index = int(au,2)

    return int_index

def insert_graph_list(index_list):
    msg = "Inserting {} values into {table_name}.adj"
    msg = msg.format(len(index_list), **cargs)
    logging.info(msg)

    cmd_add = "INSERT INTO {table_name} (adj) VALUES (?)"
    cmd_add = cmd_add.format(**cargs)
    conn.executemany(cmd_add, zip(*[index_list]))

# Process input in parallel
logging.info("Generating graphs in parallel from nauty")

P = multiprocessing.Pool()
all_graph_itr = nauty_simple_graph_itr(**cargs)
graph_allocator = grouper(all_graph_itr, cargs["chunksize"])

for gitr in graph_allocator:
    sol = P.map_async(convert_edge_to_adj, gitr, 
                      chunksize=10, callback=insert_graph_list)

P.close()
P.join()

conn.commit()

# Double check we added this many
cmd = "SELECT * from {table_name}".format(**cargs)
actually_present = len(conn.execute(cmd).fetchall())
logging.info("Database reports %i entries."%actually_present)

#assert(actually_present==count)

   

