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


try:
    import graph_tool.topology
    import graph_tool.draw
except ImportError:
    print "ERROR: The module graph_tool must be installed externally."
    sys.exit(1)

__script_dir = os.path.dirname(os.path.realpath(__file__))

####################### Invariant requirements ####################

######################### Conversion code #########################

def viz_graph(g, pos=None, **kwargs):
    if pos is None:
        pos = graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
    graph_tool.draw.graph_draw(g, pos, **kwargs)

######################### Special invariant code #################

@require_arguments("N")
def special_independent_vertex_sets(adj, **kwargs):
    cmd_idep = "main {N} {adj}".format(adj=adj, **kwargs)
    cmd = os.path.join(__script_dir, 'independent_vertex_sets', cmd_idep)
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    # Convert to two's representation
    independent_sets = [int(line, 2) for line in proc.stdout]
    return tuple([(x,) for x in independent_sets])

@require_arguments("N")
def special_independent_edge_sets(adj, **kwargs):
    cmd_idep = "main {N} {adj}".format(adj=adj, **kwargs)
    cmd = os.path.join(__script_dir, 'independent_edge_sets', cmd_idep)
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    # Already in two's representation
    independent_sets = [int(line) for line in proc.stdout]
    return tuple([(x,) for x in independent_sets])


######################### PuLP code (Integer programming) ###

########## Independent set iterator/Fractional programs #################

@require_arguments("independent_vertex_sets")
def n_independent_vertex_sets(adj, independent_vertex_sets, **kwargs):
    return len(independent_vertex_sets)

@require_arguments("independent_vertex_sets")
def maximal_independent_vertex_set(adj, independent_vertex_sets, **kwargs):
    active = [bin(x[0]).count('1') for x in independent_vertex_sets]
    return max(active)

@require_arguments("independent_edge_sets")
def n_independent_edge_sets(adj, independent_edge_sets, **kwargs):
    return len(independent_edge_sets)

@require_arguments("independent_edge_sets")
def maximal_independent_edge_set(adj, independent_edge_sets, **kwargs):
    active = [bin(x[0]).count('1') for x in independent_edge_sets]
    return max(active)



######################### Subgraph code #########################


def __generate_KN(n):
    g = graph_tool.Graph(directed=False)
    g.add_vertex(n)
    for i, j in itertools.combinations(range(n), 2):
        g.add_edge(i, j)
    return g


def __generate_CN(n):
    g = graph_tool.Graph(directed=False)
    g.add_vertex(n)
    labels = range(n)
    for i in range(-1, n - 1):
        g.add_edge(labels[i], labels[i + 1])
    return g

_complete_graphs = [__generate_KN(n) for n in range(0, 15)]
_cycle_graphs = [__generate_CN(n) for n in range(0, 15)]
_has_subgraph = graph_tool.topology.subgraph_isomorphism


def _is_subgraph_free(subg):
    subg_n = len([x for x in subg.vertices()])

    def f(adj, **kwargs):
        # Early breakout if input graph is too small
        if kwargs["N"] < subg_n:
            return 1
        g = graph_tool_representation(adj, **kwargs)

        return len(_has_subgraph(subg, g, max_n=1))==0

    return f

# is_subgraph_free_K3=1, OEIS:A024607
is_subgraph_free_K3 = _is_subgraph_free(_complete_graphs[3])
is_subgraph_free_K4 = _is_subgraph_free(_complete_graphs[4])
is_subgraph_free_K5 = _is_subgraph_free(_complete_graphs[5])

is_subgraph_free_C4 = _is_subgraph_free(_cycle_graphs[4])
is_subgraph_free_C5 = _is_subgraph_free(_cycle_graphs[5])

# zero_func = lambda x,**args:0
is_subgraph_free_C6 = _is_subgraph_free(_cycle_graphs[6])
is_subgraph_free_C7 = _is_subgraph_free(_cycle_graphs[7])
is_subgraph_free_C8 = _is_subgraph_free(_cycle_graphs[8])
is_subgraph_free_C9 = _is_subgraph_free(_cycle_graphs[9])
is_subgraph_free_C10 = _is_subgraph_free(_cycle_graphs[10])

_bull_graph = _cycle_graphs[3].copy()
_bull_graph_v1 = _bull_graph.add_vertex()
_bull_graph_v2 = _bull_graph.add_vertex()
_bull_graph.add_edge(_bull_graph_v1, _bull_graph.vertex(0))
_bull_graph.add_edge(_bull_graph_v2, _bull_graph.vertex(1))
is_subgraph_free_bull = _is_subgraph_free(_bull_graph)

_open_bowtie_graph = _cycle_graphs[3].copy()
_open_bowtie_graph_v1 = _open_bowtie_graph.add_vertex()
_open_bowtie_graph_v2 = _open_bowtie_graph.add_vertex()
_open_bowtie_graph.add_edge(_open_bowtie_graph_v1,
                            _open_bowtie_graph.vertex(0))
_open_bowtie_graph.add_edge(_open_bowtie_graph_v2,
                            _open_bowtie_graph.vertex(0))
is_subgraph_free_open_bowtie = _is_subgraph_free(_open_bowtie_graph)

_bowtie_graph = _cycle_graphs[3].copy()
_bowtie_graph_v1 = _bowtie_graph.add_vertex()
_bowtie_graph_v2 = _bowtie_graph.add_vertex()
_bowtie_graph.add_edge(_bowtie_graph_v1, _bowtie_graph.vertex(0))
_bowtie_graph.add_edge(_bowtie_graph_v2, _bowtie_graph.vertex(0))
_bowtie_graph.add_edge(_bowtie_graph_v2, _bowtie_graph_v1)
is_subgraph_free_bowtie = _is_subgraph_free(_bowtie_graph)

_diamond_graph = _cycle_graphs[4].copy()
_diamond_graph.add_edge(_diamond_graph.vertex(0), _diamond_graph.vertex(2))
is_subgraph_free_diamond = _is_subgraph_free(_diamond_graph)

_paw_graph = _cycle_graphs[3].copy()
_paw_graph_v1 = _paw_graph.add_vertex()
_paw_graph.add_edge(_paw_graph_v1, _paw_graph.vertex(0))
is_subgraph_free_paw = _is_subgraph_free(_paw_graph)

_banner_graph = _cycle_graphs[4].copy()
_banner_graph_v1 = _banner_graph.add_vertex()
_banner_graph.add_edge(_banner_graph_v1, _banner_graph.vertex(0))
is_subgraph_free_banner = _is_subgraph_free(_banner_graph)

######################### Bliss code #########################

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
