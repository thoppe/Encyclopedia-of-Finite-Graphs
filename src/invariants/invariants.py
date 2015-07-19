import itertools
import os
import sys
import fractions
import subprocess
import collections

import networkx as nx
import numpy as np
import sympy
import pulp

from functools import wraps
from helper_functions import require_arguments


####################### Invariant requirements ####################

######################### Conversion code #########################

def viz_graph(g, pos=None, **kwargs):
    if pos is None:
        pos = graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
    graph_tool.draw.graph_draw(g, pos, **kwargs)

######################### Subgraph code #########################


######################### Test code #########################

if __name__ == "__main__":
    import logging

    # Start the logger
    logging.root.setLevel(logging.INFO)
    logging.info("Testing the Petersen graph for all the invariants")

    logging.info("Creating the graph.")
    g = nx.petersen_graph()

    logging.info("Converting to adj. format")
    adj = convert_nx_to_adj(g)

    N = 10
    args = {"N": N}

    logging.info("Converting to numpy format")
    A = convert_to_numpy(adj, **args)

    logging.info("Converting to networkx format")
    gx = networkx_representation(adj, **args)

    logging.info("Converting to graph-tool format")
    gt = graph_tool_representation(adj, **args)

    logging.info("Computing the Tutte polynomial")
    p = special_polynomial_tutte(adj, **args)
    args["tutte_polynomial"] = p
    print (p)

    logging.info("Computing the chromatic polynomial")
    p = special_chromatic_polynomial(adj, **args)
    args["chromatic_polynomial"] = p
    print (p)

    logging.info("Computing the degree sequence")
    p = special_degree_sequence(adj, **args)
    args["degree_sequence"] = np.array(p).ravel()

    logging.info("Computing the fractional chromatic number")
    p = fractional_chromatic_number(adj, **args)
    args["fractional_chromatic_number"] = p[0]
    print (p)

    logging.info("Computing the characteristic polynomial")
    p = special_characteristic_polynomial(adj, **args)
    args["characteristic_polynomial"] = p
    print (p)

    logging.info("Computing the laplacian polynomial")
    p = special_laplacian_polynomial(adj, **args)
    args["laplacian_polynomial"] = p
    print (p)

    logging.info("Computing the independent vertex sets")
    p = special_independent_vertex_sets(adj, **args)
    args["independent_vertex_sets"] = p
    print (p)

    logging.info("Computing the independent edge sets")
    p = special_independent_edge_sets(adj, **args)
    args["independent_edge_sets"] = p
    print (p)

    logging.info("Computing the cycle basis")
    import collections
    p = special_cycle_basis(adj, **args)
    cb = collections.defaultdict(list)
    for cycle_k, idx in p:
        cb[cycle_k].append(idx)
    args["cycle_basis"] = cb.values()

    from helper_functions import load_options
    options = load_options()

    for func in options["invariant_function_names"]:
        logging.info("Computing {}".format(func))
        x = eval(func)(adj, **args)
        print (x)

    viz_graph(gt)
