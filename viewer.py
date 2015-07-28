import logging
import argparse
from EoGF.helper_functions import grab_vector, load_options, load_graph_database
from EoGF.invariants import convert_to_numpy
import graph_tool as gt
import numpy as np

desc   = '''
Visualize specific graphs, for a three-graph example:
python viewer.py 10 -i is_bipartite 1 -i is_integral 1 -i is_eulerian 1
'''
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('N', type=int, default=5,
                    help="Graph order (number of vertices) to query)")
parser.add_argument('--limit', type=int, default=15,
                    help="Max number of graphs to draw")
parser.add_argument('--cooling_step', type=float, default=.99,
                    help="Cooling step for the sfdp_layout")
parser.add_argument('--output', type=str, default=None,
                    help="If given, saves the image to this file")
parser.add_argument('-i', '--invariant_query', nargs=2,
                    action='append', required=False,
                    help="Invariant to query (can be repeated)")
cargs = vars(parser.parse_args())
N = cargs["N"]

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database
conn = helper_functions.load_graph_database(N)

# Load the list of invariants to compute
options = load_options()
invariant_names = options["invariant_function_names"]

# Check the inputs to see if they are valid queries
for func_name, val in cargs["invariant_query"]:
    if func_name not in invariant_names:
        err = "{} not a known invariant".format(func_name)
        raise KeyError(err)

    try:
        int(val)
    except Exception as ex:
        err = "{}={} is {}".format(func_name, val, ex)
        raise ValueError(err)

cmd_search = '''
SELECT adj FROM invariant_integer AS A
JOIN graph AS B ON A.graph_id = B.graph_id'''
constraints = ["{}={}".format(*items) for items in cargs["invariant_query"]]
if constraints:
    cmd_search += ' WHERE ' + ' AND '.join(constraints)
cmd_search += " LIMIT {limit} ".format(**cargs)

# Add limit at some point
ADJ = grab_vector(conn, cmd_search)
logging.info("Found at least {} graphs matching the criteria".format(len(ADJ)))

#######################################################################################


def disjoint_graph_add(adj_list, N):
    # Disjoint union of many graphs, assumes graphs are all size N

    total_vertex = N * len(adj_list)

    G = gt.Graph(directed=False)
    G.add_vertex(total_vertex)

    for k, adj in enumerate(adj_list):
        A = convert_to_numpy(adj, N=N)
        for (i, j) in zip(*np.where(A)):
            if i >= j:
                G.add_edge(i + N * k, j + N * k)
    return G


def viz_graph(g, **kwargs):
    pos = gt.draw.sfdp_layout(g,
                              p=3.5,
                              cooling_step=cargs["cooling_step"])
    gt.draw.graph_draw(g, pos,
                       **kwargs)


G = disjoint_graph_add(ADJ, N)

if not cargs["output"]:
    viz_graph(G, vertex_size=10)

else:
    viz_graph(G, vertex_size=10, output=cargs["output"])
