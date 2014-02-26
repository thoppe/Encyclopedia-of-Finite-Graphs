import sqlite3, logging, argparse, os
import subprocess, itertools
import numpy as np
import helper_functions

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

f_database = helper_functions.generate_database_name(cargs["N"])

# If forced, removed the old database
if cargs["force"] and os.path.exists(f_database):
    logging.warning("Removing database %s"%f_database)
    os.remove(f_database)

does_db_file_exist = os.path.exists(f_database)

# Connect to the database
conn = helper_functions.load_graph_database(cargs["N"], False)

# Load the invariant template from file, add new columns if needed
f_invariant_template = "templates/graph_invariants.sql"
with open(f_invariant_template) as FIN:
    logging.info("Updating invariants from %s"%f_invariant_template)
    script = FIN.read()
    conn.executescript(script);

# Check if database exists, if so exit!
if does_db_file_exist:
    #err = "Database %s already exists, exiting"%f_database
    #logging.warning(err)
    exit()

logging.info("Creating database "+f_database)

# Load the template from file
f_graph_template = "templates/graph.sql"
with open(f_graph_template) as FIN:
    script = FIN.read()
    conn.executescript(script)


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
    msg = "Inserting {} values into graph.adj"
    msg = msg.format(len(index_list), **cargs)
    logging.info(msg)

    cmd_add = "INSERT INTO graph (adj) VALUES (?)"
    cmd_add = cmd_add.format(**cargs)
    conn.executemany(cmd_add, zip(*[index_list]))

# Process input in parallel
logging.info("Generating graphs in parallel from nauty")

all_graph_itr = nauty_simple_graph_itr(**cargs)

PC = helper_functions.parallel_compute
PC(all_graph_itr, 
   convert_edge_to_adj, 
   callback=insert_graph_list, **cargs)

conn.commit()

# Double check we added this many
cmd = "SELECT * from graph".format(**cargs)
actually_present = len(conn.execute(cmd).fetchall())
logging.info("Database reports %i entries."%actually_present)


   

