import sqlite3, subprocess, multiprocessing
import numpy as np

args = {"N":8}
args["table_name"] = "graph{N}".format(**args)
f_database = 'database/{table_name}.db'.format(**args)
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
conn.execute("DELETE FROM {table_name}".format(**args))
conn.commit()

# Process input in parallel
P = multiprocessing.Pool()
gitr = nauty_simple_graph_itr(**args)
sol = P.imap(convert_edge_to_adj, gitr)
P.close()
P.join()

for adj in sol:
    cmd_add = "INSERT INTO {table_name} (adj) VALUES ('{adj}')"
    cmd_add = cmd_add.format(adj = adj, **args)
    conn.execute(cmd_add)

conn.commit()

# Debug method to check
'''
def select_itr(cmd, arraysize=1000):
    itr = conn.execute(cmd)
    
    "An interator over the search using chunks"
    while True:
        results = itr.fetchmany(arraysize)
        if not results:         break
        for result in results:  yield result  

cmd = "SELECT * from {table_name}".format(**args)
print len(list(select_itr(cmd)))
'''



