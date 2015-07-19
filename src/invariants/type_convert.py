import numpy as np
import networkx as nx

try:
    import graph_tool
except ImportError:
    print "ERROR: The module graph_tool must be installed externally."
    sys.exit(1)


def twos_C_numpy(twos_representation, N, **kwargs):
    
    possible_edges = int ((N * (N + 1)) / 2)

    edge_map = np.binary_repr(twos_representation, possible_edges)
    edge_int = [int(x) for x in edge_map]

    idx = np.triu_indices(N)
    A = np.zeros((N, N), dtype=np.int)

    A[idx] = edge_int

    A = A + A.T - np.diag(A)
    return A


def twos_C_networkx(twos_representation, N, **kwargs):
    A = twos_C_numpy(twos_representation, N)
    return nx.from_numpy_matrix(A)


def twos_C_graphtool(twos_representation, N, **kwargs):
    A = twos_C_numpy(twos_representation, N)
    g = graph_tool.Graph(directed=False)
    g.add_vertex(N)
    for edge in zip(*np.where(A)):
        n0, n1 = edge
        if n0 > n1:
            g.add_edge(n0, n1)
    return g


    return nx.from_numpy_matrix(A)


type_conversion_funcs = {
    ("twos","numpy")    : (twos_C_numpy, "A"),
    ("twos","networkx") : (twos_C_networkx, "gx"),
    ("twos","graph_tool") : (twos_C_graphtool, "gtx"),
}
