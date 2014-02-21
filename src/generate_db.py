import sqlite3, logging, argparse, os
import multiprocessing, subprocess
import numpy as np

desc   = "Builds the database for fixed N"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int)
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Debug mode, do everything in memory
#conn = sqlite3.connect(':memory:')

cargs["table_name"] = "graph{N}".format(**cargs)
f_database = 'database/{table_name}.db'.format(**cargs)

# Check if database exists, if so exit!
if os.path.exists(f_database):
    err = "Database %s already exists, exiting"%f_database
    logging.critical(err)
    exit()

logging.info("Creating database "+f_database)
conn = sqlite3.connect(f_database)

def load_template(f_template, **kwargs):
    template = []
    with open(f_template) as FIN:
        for line in FIN:
            line = line.strip()
            if line and line[0][0] != "#":
                template.append(line)
    return ",\n".join(template)

def create_table_cmd(template, **cargs):

    N = cargs["N"]
    args = cargs.copy()
    args["max_edges"] = N**2
    args["cols"] = template.format(**args)

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


def convert_edge_to_adj(edges):
    # Map the edge list into an index list
    edges = map(int,edges.split())
    idx = zip((edges[::2], edges[1::2]))
    
    # Since graph in undirected assign both sides
    A = np.zeros((cargs["N"],cargs["N"]),dtype=int)
    A[idx[0],idx[1]] = A[idx[1],idx[0]] = 1

    # Convert output into a string
    s = ''.join(map(str,A.ravel()))

    return s

# Process input in parallel
logging.info("Generating graphs in parallel from nauty")
P = multiprocessing.Pool()
gitr = nauty_simple_graph_itr(**cargs)
sol = P.imap(convert_edge_to_adj, gitr, chunksize=10)
P.close()
P.join()

logging.info("Adding graphs from nauty")

for count,adj in enumerate(sol):
    cmd_add = "INSERT INTO {table_name} (adj) VALUES ('{adj}')"
    cmd_add = cmd_add.format(adj = adj, **cargs)
    conn.execute(cmd_add)

    #if count and not k%1000: 
    #    logging.info("Processed %i graphs"%k)

count += 1
logging.info("Complete. Processed %i graphs"%count)
conn.commit()
# Double check we added this many
cmd = "SELECT * from {table_name}".format(**cargs)
actually_present = len(conn.execute(cmd).fetchall())
logging.info("Database reports %i entries."%actually_present)

assert(actually_present==count)



'''
def select_itr(cmd, arraysize=100):
    itr = conn.execute(cmd)
    
    "An interator over the search using chunks"
    while True:
        results = itr.fetchmany(arraysize)
        if not results:         break
        for result in results:  yield result      

'''    

