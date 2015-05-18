import logging
import argparse
import os
import subprocess
import numpy as np
import helper_functions

desc = "Builds the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
parser.add_argument('-f', '--force', default=False, action='store_true')
parser.add_argument('--chunksize', type=int,
                    help="Entries to compute before insert is called",
                    default=10000)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

f_database = helper_functions.generate_database_name(cargs["N"])

# If forced, removed the old database
if cargs["force"] and os.path.exists(f_database):
    logging.warning("Removing database %s" % f_database)
    os.remove(f_database)

does_db_file_exist = os.path.exists(f_database)

# Connect to the database
conn = helper_functions.load_graph_database(cargs["N"], False)

f_graph_template = "templates/graphs.sql"

logging.info("Templating database via %s" % f_graph_template)

# Load the graph template
with open(f_graph_template) as FIN:
    script = FIN.read()
    conn.executescript(script)
    conn.commit()

# Check if the database is populated, if so exit
cmd_check = '''SELECT COUNT(*) FROM computed WHERE function_name="adj"'''
is_populated = helper_functions.grab_scalar(conn, cmd_check)

if is_populated:
    err = "Database {N} has been populated. Skipping nauty."
    logging.info(err.format(**cargs))
    exit()

######################################################################


def nauty_simple_graph_itr(**args):
    ''' Creates a generator for all simple graphs using nauty '''

    cmd = "geng {N} -cq | showg -eq -l0"
    cmd = cmd.format(**args)

    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    while True:
        header_line = proc.stdout.readline()
        edge_line = proc.stdout.readline()
        if not header_line:
            break
        yield edge_line.strip()

__upper_matrix_index = np.triu_indices(cargs["N"])


def convert_edge_to_adj(edges):

    # Map the edge list into an index list
    edges = map(int, edges.split())
    idx = zip((edges[::2], edges[1::2]))

    # Since graph in undirected assign both sides
    A = np.zeros((cargs["N"], cargs["N"]), dtype=int)
    A[idx[0], idx[1]] = 1

    # The string representation of the upper triangular adj matrix
    au = ''.join(map(str, A[__upper_matrix_index]))

    # Convert the binary string to an int
    int_index = int(au, 2)

    return int_index


def insert_graph_list(index_list):
    msg = "Inserting {} values into graph.adj"
    logging.info(msg.format(len(index_list)))

    cmd_add = "INSERT OR IGNORE INTO graph (adj) VALUES (?)"
    conn.executemany(cmd_add, zip(*[index_list]))

######################################################################

# Process input in parallel
logging.info("Generating graphs in parallel from nauty")

all_graph_itr = nauty_simple_graph_itr(**cargs)

PC = helper_functions.parallel_compute
PC(all_graph_itr,
   convert_edge_to_adj,
   callback=insert_graph_list, **cargs)

cmd_mark = '''INSERT OR IGNORE INTO computed VALUES ("adj")'''
conn.execute(cmd_mark)

cmd_copy = '''
INSERT INTO invariant_integer (graph_id) SELECT graph_id FROM graph'''
conn.execute(cmd_copy)

conn.commit()

# Double check we added this many
cmd = "SELECT COUNT(*) from graph"
actually_present = conn.execute(cmd).fetchone()[0]
logging.info("Database reports %i entries." % actually_present)
