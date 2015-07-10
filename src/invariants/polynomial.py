import numpy as np

from base_invariant import graph_invariant


class degree_sequence(graph_invariant):
    def shape(self, N, **kwargs): return N

    def calculate(self, A, **kwargs):
        deg = sorted(A.sum(axis=0))
        return deg

class laplacian_polynomial(graph_invariant):
    '''
    This is the characteristic polynomial of the Laplacian matrix
    L = A - D
    '''

    def shape(self, N, **kwargs): return N+1

    def calculate(self, A, **kwargs):
        L = np.zeros(A.shape)
        np.fill_diagonal(L, A.sum(axis=0))
        L -= A
        p = np.round(np.poly(L))
        return p.astype(np.int32)


class characteristic_polynomial(graph_invariant):
    ''' Characteristic polynomial of the adjacency matrix '''

    def shape(self, N, **kwargs): return N+1

    def calculate(self, A, **kwargs):
        p = np.poly(A)
        return p.astype(np.int32)


if __name__ == "__main__":

    B = degree_sequence()
    item = {"twos_representation":474, "N":4}
    print B(item)
    print B.shape(**item)
