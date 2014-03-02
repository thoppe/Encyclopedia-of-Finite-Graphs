import numpy as np
import itertools
import networkx as nx
import graph_tool.topology
import graph_tool.draw

def convert_to_numpy(adj,**args):
    N = args["N"]

    possible_edges = (N*(N+1))/2
    edge_map = np.binary_repr(adj, possible_edges)
    edge_int = map(int, edge_map)

    idx = np.triu_indices(N)
    A = np.zeros((N,N),dtype=np.int)
    
    A[idx] = edge_int

    # Works for loopless graphs only
    A += A.T
    return A

def graph_tool_representation(adj, **args):
    A = convert_to_numpy(adj,**args)
    g = graph_tool.Graph(directed=False)
    g.add_vertex(args["N"])
    for edge in zip(*np.where(A)):
        n0, n1 = edge
        if n0>n1:
            g.add_edge(n0,n1)
    return g

def viz_graph(g):
    pos = graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
    graph_tool.draw.graph_draw(g,pos)

def n_edge(adj,**args):
    # Only true for undirected graphs
    A = convert_to_numpy(adj,**args)
    return A.sum()/2

def n_vertex(adj,**args):
    return args["N"]

def diameter(adj,**args):
    if args["N"]==1: return 0
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return nx.diameter(g)

def radius(adj,**args):
    if args["N"]==1: return 0
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return nx.radius(g)

def n_cycle_basis(adj, **args):
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return len(nx.cycle_basis(g))

def is_eulerian(adj,**args):
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return nx.is_eulerian(g)

def is_distance_regular(adj,**args):
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return nx.is_distance_regular(g)

def is_planar(adj,**args):
    g = graph_tool_representation(adj,**args)
    return graph_tool.topology.is_planar(g)

def is_bipartite(adj,**args):
    g = graph_tool_representation(adj,**args)
    return graph_tool.topology.is_bipartite(g)

def n_articulation_points(adj,**args):
    g = graph_tool_representation(adj,**args)
    bicomp, art, nc = graph_tool.topology.label_biconnected_components(g)
    return sum(art.a)

######################### Subgraph code ######################### 

def __generate_KN(n):
    g = graph_tool.Graph(directed=False)
    g.add_vertex(n)
    for i,j in itertools.combinations(range(n),2):
        g.add_edge(i,j)
    return g

_complete_graphs = [__generate_KN(n) for n in xrange(0, 15)]
_has_subgraph = graph_tool.topology.subgraph_isomorphism

def _count_subgraphs(subg, g):
    return len(_has_subgraph(subg,g)[0])

def n_subgraph_triangle(adj, **args):
    ''' n_subgraph_triangle=0, OEIS:A024607 '''
    g = graph_tool_representation(adj,**args)
    return _count_subgraphs(_complete_graphs[3], g)


if __name__ == "__main__":
    # Function testing here

    N = 7
    adj = 14781504
    args= {"N":N}

    A  = convert_to_numpy(adj,**args)    
    gx = nx.from_numpy_matrix(A)
    g = graph_tool_representation(adj,**args)

    print "n_cycle_basis:",n_cycle_basis(adj,**args)
    print "is_planar",is_planar(adj,**args), is_bipartite(adj,**args)
    print "n_articulation_points",n_articulation_points(adj,**args)
    viz_graph(g)
    

