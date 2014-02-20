import sqlite3, subprocess, multiprocessing
import logging, argparse
import numpy as np

desc   = "Populates the database at fixed N (WARNING ERASES CURRENT)"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
args = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

args["table_name"] = "graph{N}".format(**args)
f_database = 'database/{table_name}.db'.format(**args)

logging.info("Loading database "+f_database)
conn = sqlite3.connect(f_database)

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


def convert_edge_to_adj(edges):
    # Map the edge list into an index list
    edges = map(int,edges.split())
    idx = zip((edges[::2], edges[1::2]))
    
    # Since graph in undirected assign both sides
    A = np.zeros((args["N"],args["N"]),dtype=int)
    A[idx[0],idx[1]] = A[idx[1],idx[0]] = 1

    # Convert output into a string
    s = ''.join(map(str,A.ravel()))
    return s

def add_graph_to_database(edges):
    print edges
    adj = convert_edge_to_adj(edges)
    
# First empty the database
logging.warn("Cleaning all entries in current database")
conn.execute("DELETE FROM {table_name}".format(**args))
conn.commit()

# Process input in parallel
P = multiprocessing.Pool()
gitr = nauty_simple_graph_itr(**args)
sol = P.imap(convert_edge_to_adj, gitr)
P.close()
P.join()

for k,adj in enumerate(sol):
    cmd_add = "INSERT INTO {table_name} (adj) VALUES ('{adj}')"
    cmd_add = cmd_add.format(adj = adj, **args)
    conn.execute(cmd_add)

    if k and not k%1000: 
        logging.info("Processed %i graphs"%k)
k += 1
logging.info("Complete. Processed %i graphs"%k)
conn.commit()

# Double check we added this many
cmd = "SELECT * from {table_name}".format(**args)
actually_present = len(conn.execute(cmd).fetchall())
logging.info("Database reports %i entries."%actually_present)

assert(actually_present==k)





