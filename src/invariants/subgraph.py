# Subgraph testing code
# Requires graph_tool

import sys
import itertools
import graph_tool
import graph_tool.topology
from base_invariant import graph_invariant

_largest_N_subgraph = 20

#######################################################################
# Graph Generators

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

#######################################################################
# Defined graphs

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
# Detection class factories

class _is_subgraph_free(graph_invariant):

    subg = None
    output_type = "graph_tool"

    def shape(self,**kwargs):
        return 1

    def subg_N(self):
        verts = self.subg.vertices()
        return len(list(verts))
    
    def calculate(self,gtx,N,**kwargs):

        # Early breakout if input graph is too small
        if N < self.subg_N():
            return True

        # Only look for a single subgraph, break early if found
        has_sub = _has_subgraph(self.subg, gtx, max_n=1)
        
        return len(has_sub) == 0


def subgraph_builder(name, input_subg):
    # Add the named class to the current module
    
    thismodule = sys.modules[__name__]
    
    class x(_is_subgraph_free):
        subg = input_subg
        
    full_name = "is_subgraph_free_{}".format(name)
    setattr(thismodule, full_name, x)


#######################################################################
# Explict detection code

subgraph_builder("diamond",_diamond_graph)
subgraph_builder("paw",_paw_graph)
subgraph_builder("banner",_banner_graph)
subgraph_builder("open_bowtie",_open_bowtie_graph)
subgraph_builder("bowtie",_bowtie_graph)
subgraph_builder("bull",_bull_graph)

for K in xrange(3, _largest_N_subgraph):
    # is_subgraph_free_K3=1, OEIS:A024607
    subgraph_builder("K{}".format(K),_complete_graphs[K])
    subgraph_builder("C{}".format(K),_cycle_graphs[K])

#######################################################################

if __name__ == "__main__":
    B = is_subgraph_free_K3()
    item = {"twos_representation":474, "N":4}
    print B(item)
    print B.shape(**item)
