# Subgraph testing code
# Requires graph_tool

# RAW NOT IMPORTED PROPERLY YET

import itertools
import graph_tool
import graph_tool.topology
from base_invariant import graph_invariant

_largest_N_subgraph = 30


def __generate_KN(n):
    # Generates a complete graph
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

_complete_graphs = [__generate_KN(n) for n in range(0, _largest_N_subgraph)]
_cycle_graphs = [__generate_CN(n) for n in range(0, _largest_N_subgraph)]
_has_subgraph = graph_tool.topology.subgraph_isomorphism

# Bull graph
_bull_graph = _cycle_graphs[3].copy()
_bull_graph_v1 = _bull_graph.add_vertex()
_bull_graph_v2 = _bull_graph.add_vertex()
_bull_graph.add_edge(_bull_graph_v1, _bull_graph.vertex(0))
_bull_graph.add_edge(_bull_graph_v2, _bull_graph.vertex(1))


# Bowtie and open-bowtie
_open_bowtie_graph = _cycle_graphs[3].copy()
_open_bowtie_graph_v1 = _open_bowtie_graph.add_vertex()
_open_bowtie_graph_v2 = _open_bowtie_graph.add_vertex()
_open_bowtie_graph.add_edge(_open_bowtie_graph_v1,
                            _open_bowtie_graph.vertex(0))
_open_bowtie_graph.add_edge(_open_bowtie_graph_v2,
                            _open_bowtie_graph.vertex(0))

_bowtie_graph = _cycle_graphs[3].copy()
_bowtie_graph_v1 = _bowtie_graph.add_vertex()
_bowtie_graph_v2 = _bowtie_graph.add_vertex()
_bowtie_graph.add_edge(_bowtie_graph_v1, _bowtie_graph.vertex(0))
_bowtie_graph.add_edge(_bowtie_graph_v2, _bowtie_graph.vertex(0))
_bowtie_graph.add_edge(_bowtie_graph_v2, _bowtie_graph_v1)

# Diamond graph
_diamond_graph = _cycle_graphs[4].copy()
_diamond_graph.add_edge(_diamond_graph.vertex(0), _diamond_graph.vertex(2))

# Paw graph
_paw_graph = _cycle_graphs[3].copy()
_paw_graph_v1 = _paw_graph.add_vertex()
_paw_graph.add_edge(_paw_graph_v1, _paw_graph.vertex(0))

# Banner graphs
_banner_graph = _cycle_graphs[4].copy()
_banner_graph_v1 = _banner_graph.add_vertex()
_banner_graph.add_edge(_banner_graph_v1, _banner_graph.vertex(0))

#######################################################################

def _is_subgraph_free(subg):
    subg_n = len([x for x in subg.vertices()])

    def f(adj, **kwargs):
        # Early breakout if input graph is too small
        if kwargs["N"] < subg_n:
            return True
        
        g = graph_tool_representation(adj, **kwargs)

        return len(_has_subgraph(subg, g, max_n=1))==0

    return f


#######################################################################



##### Detection code

is_subgraph_free_diamond = _is_subgraph_free(_diamond_graph)
is_subgraph_free_paw = _is_subgraph_free(_paw_graph)
is_subgraph_free_banner = _is_subgraph_free(_banner_graph)
is_subgraph_free_open_bowtie = _is_subgraph_free(_open_bowtie_graph)
is_subgraph_free_bowtie = _is_subgraph_free(_bowtie_graph)
is_subgraph_free_bull = _is_subgraph_free(_bull_graph)

# is_subgraph_free_K3=1, OEIS:A024607
is_subgraph_free_K3 = _is_subgraph_free(_complete_graphs[3])
is_subgraph_free_K4 = _is_subgraph_free(_complete_graphs[4])
is_subgraph_free_K5 = _is_subgraph_free(_complete_graphs[5])

is_subgraph_free_C4 = _is_subgraph_free(_cycle_graphs[4])
is_subgraph_free_C5 = _is_subgraph_free(_cycle_graphs[5])

is_subgraph_free_C6 = _is_subgraph_free(_cycle_graphs[6])
is_subgraph_free_C7 = _is_subgraph_free(_cycle_graphs[7])
is_subgraph_free_C8 = _is_subgraph_free(_cycle_graphs[8])
is_subgraph_free_C9 = _is_subgraph_free(_cycle_graphs[9])
is_subgraph_free_C10 = _is_subgraph_free(_cycle_graphs[10])



#####################
