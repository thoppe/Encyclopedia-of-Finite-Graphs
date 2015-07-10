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


class chromatic_polynomial(graph_invariant):
    '''
    TODO: Write a type conversion for this to tutte!
    
    This is the chromatic polynomial, derived from the Tutte polynomial
    The chromatic polynomial for a connected graphs evaluates T(x,y)
    at C(k) = T(x=1-k,y=0)*(-1)**N*(1-k)*N
    '''

    def shape(self, N, **kwargs): return 0

    def calculate(self, tutte_poly, **kwargs):
        print tutte_poly
        raise ValueError

        T = special_tutte_polynomial(repack)

        # Extract only the x component of the tutte poly
        from sympy.abc import x
        p = 0
        for power,row in enumerate(T):
            if row and row[0]:
                p += row[0] * x ** power

        C = (-1) ** (N - 1) * x * p.subs(x, 1 - x)
        C = sympy.poly(C)
        coeffs = C.all_coeffs()

        # Resize coeffs to match desired length
        coeffs = [0,]*(N+1-len(coeffs)) + coeffs
        return np.array(coeffs).astype(np.int32)
    


if __name__ == "__main__":

    B = degree_sequence()
    item = {"twos_representation":474, "N":4}
    print B(item)
    print B.shape(**item)
