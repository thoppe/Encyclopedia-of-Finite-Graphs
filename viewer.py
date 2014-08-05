import sqlite3, logging, argparse, os, collections, ast
import subprocess
import numpy as np

import src.helper_functions as helper_functions
from src.invariants import graph_tool_representation, convert_to_numpy
import graph_tool

desc   = "Visualize specific graphs"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('--max_n',type=int,default=8,
                    help="Maximum graph size n to compute tests")
parser.add_argument('--min_n',type=int,default=2,
                    help="Minimum graph size n to match tests")
cargs = vars(parser.parse_args())

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_database = "database/sequence.db"
conn = sqlite3.connect(f_database, check_same_thread=False)

graph_conn = collections.OrderedDict()
for n in range(1, cargs["max_n"]+1):
    graph_conn[n] = helper_functions.load_graph_database(n)

def grab_vector(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()]

def grab_scalar(connection, cmd):
    return [x[0] for x in connection.execute(cmd).fetchall()][0]

cmd_graphs = '''
SELECT c.adj FROM invariant_integer as a 
LEFT JOIN ref_invariant_integer as b
ON  a.invariant_id  = b.invariant_id 
LEFT JOIN graph as c
ON  a.graph_id = c.graph_id
WHERE b.function_name = "{function_name}"
AND   a.value {conditional} {value}
'''

N = 6
args = {"N":N}

cmd = cmd_graphs.format(function_name = "automorphism_group_n",
                        conditional   = "=",
                        value = 1)




for adj in grab_vector(graph_conn[N], cmd):
    g = graph_tool_representation(adj,**args)

    A = convert_to_numpy(adj,**args)
    edges = np.where(A)

    s = ["p edge {N} {}".format(A.sum()/2,**args)]
    for i,j in zip(*edges):
        if i>=j:
            s.append("e {} {}".format(i+1,j+1))

    f_save = "test_{}.txt".format(adj)
    #with open(f_save,'w') as FOUT:
    #    for line in s:
    #        FOUT.write("%s\n"%line)
         
    s_echo = '"%s"'%('\n'.join(s))
    cmd = "echo %s | src/bliss/bliss" % s_echo

    proc = subprocess.Popen([cmd],stdout=subprocess.PIPE,shell=True)
    for line in proc.stdout:
        #print line.strip()
        if "|Aut|" in line:
            print int(line.split()[-1])


    pos = graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
    graph_tool.draw.graph_draw(g,pos)


