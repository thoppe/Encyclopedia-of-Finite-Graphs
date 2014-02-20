import sqlite3, logging

N = 8
#conn = sqlite3.connect(':memory:')
table_name = "graph{}".format(N)
f_database = 'database/{}.db'.format(table_name)
conn = sqlite3.connect(f_database)

def load_template(f_template, **kwargs):
    template = []
    with open(f_template) as FIN:
        for line in FIN:
            line = line.strip()
            if line and line[0][0] != "#":
                template.append(line)
    return "\n".join(template)

def create_table_cmd(N, template):

    args = {}
    args["table_name"] = table_name
    args["max_edges"] = N**2
    args["cols"] = template.format(**args)

    cmd = "CREATE TABLE IF NOT EXISTS {table_name} ({cols})"
    cmd = cmd.format(**args)
    return cmd

def select_itr(cmd, arraysize=100):
    itr = conn.execute(cmd)
    
    "An interator over the search using chunks"
    while True:
        results = itr.fetchmany(arraysize)
        if not results:         break
        for result in results:  yield result      

# Load the template from file
f_graph_template = "graph_template.txt"
template = load_template(f_graph_template)

# Create the database if it doesn't exist
conn.execute( create_table_cmd(N, template) )

'''
# Test case, generate a few random graphs and try to add them
import numpy as np
for _ in xrange(5):
    A = np.random.randint(0,2,size=N*N).reshape((N,N))

    args = {}
    args["n_edge"] = A.sum()
    args["adj"]    = ''.join(map(str, A.ravel().tolist()))
    keys = ", ".join(args.keys())
    vals = ", ".join("'%s'"%args[k] for k in args.keys())
    cmd = "INSERT INTO graph{} ({}) VALUES ({})"
    cmd = cmd.format(N,keys,vals)
    conn.execute(cmd)
conn.commit()
  
cmd = "SELECT * from {}".format(database_name)

for item in select_itr(cmd):
    print item
'''    

