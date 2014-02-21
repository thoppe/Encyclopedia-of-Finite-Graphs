import numpy as np

square_map = dict((x**2,x) for x in range(100))

def convert_to_numpy(adj):
    A = np.array(map(int,adj))
    n = square_map[A.size]
    return A.reshape((n,n))

#def is_planar(A):
#    print "HI",A
#invariant_function_map = {"is_planar":is_planar}

def n_edge(adj):
    # Only true for directed graphs
    A = convert_to_numpy(adj)
    return A.sum()/2

invariant_function_map = {}
invariant_function_map['n_edge'] = n_edge

