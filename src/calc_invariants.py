import numpy as np
from numpy import binary_repr
import networkx as nx

#square_map = dict((x**2,x) for x in range(100))

def convert_to_numpy(adj,**args):
    N = args["N"]

    possible_edges = (N*(N+1))/2
    edge_map = np.binary_repr(adj, possible_edges)
    edge_int = map(int, edge_map)

    idx = np.triu_indices(N)
    A = np.zeros((N,N),dtype=np.int)
    
    A[idx] = edge_int

    # Works for loopless graphs
    A += A.T
    return A


#def is_planar(A):
#    print "HI",A
#invariant_function_map = {"is_planar":is_planar}

def n_edge(adj,**args):
    # Only true for undirected graphs
    A = convert_to_numpy(adj,**args)
    return int(A.sum()/2)

def diameter(adj,**args):
    # Only true for undirected graphs
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return nx.diameter(g)

invariant_function_map = {}
invariant_function_map['n_edge'] = n_edge
invariant_function_map['diameter'] = diameter

