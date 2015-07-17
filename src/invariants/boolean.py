import numpy as np
import itertools
import os

from base_invariant import graph_invariant

_script_dir = os.path.dirname(os.path.realpath(__file__))

class boolean_invariant(graph_invariant):
    dtype = np.bool
    def shape(self, **kwargs): return 1


class is_strongly_regular(boolean_invariant):

    def calculate(self, A, N, **kwargs):
        # Check with http://oeis.org/A088741
        # Returns the value of k if it is k strongly regular, otherwise 0
        # Strongly regular graphs satisfy AJ = kJ, where J is a ones matrix
        # Assume that N=1,2 is are strongly regular to match with OEIS
        if N <= 2:
            return True

        K = A.sum(axis=0)

        if len(set(K)) != 1:
            return False

        L, V = None, None

        for v0, v1 in itertools.combinations(range(N), 2):
            common = (A[v0] * A[v1]).sum()
            if A[v0, v1]:
                if L is None:
                    L = common
                if L and common != L:
                    return False
            if not A[v0, v1]:
                if V is None:
                    V = common
                if V and common != V:
                    return False
        return True

######################################################################

def _poly_factorable_over_field(p, domain, sympy):
    # Factor the char poly over the integers
    pz = sympy.factor(p, domain=domain)

    # Change expression like (a+b)**n -> (a+b)
    def reduce_power(fp):
        try:
            return fp.base
        except:
            return fp

    # Loop over the factors
    for term in pz.as_ordered_factors():
        term_poly = sympy.poly(reduce_power(term))
        # Check if the base factors are not linear
        # indicates can't be factored over choosen domain
        if term_poly.degree() > 1:
            return False
    return True


class is_integral(boolean_invariant):
    import_requirements = ["sympy"]

    def calculate(self, A, **kwargs):
        # Check with http://oeis.org/A064731
        # Symbolically determine if char poly factors over Z
        sympy = self.imports["sympy"]
        M = sympy.Matrix(A)
        p = M.charpoly()
        return _poly_factorable_over_field(p, "ZZ", sympy)


'''

@build_representation("numpy")
def is_rational_spectrum(A, **kwargs):
    # Like is_integral, checks if the char. poly factors over Q instead of Z
    M = sympy.Matrix(A)
    p = M.charpoly()
    return _poly_factorable_over_field(p, "QQ")

@require_arguments("N")
@build_representation("numpy")
def is_distinct_spectrum(A, N, **kwargs):
    # Checks if all eigenvalues are unique
    M = sympy.Matrix(A)
    p = M.charpoly()
    return p.rep.count_real_roots() == N
    
@build_representation("networkx")
def is_chordal(g, **kwargs):
    return nx.is_chordal(g)

@build_representation("networkx")
def is_eulerian(g, **kwargs):
    return nx.is_eulerian(g)

@build_representation("networkx")
def is_distance_regular(g, **kwargs):
    return nx.is_distance_regular(g)

@build_representation("graph_tool")
def is_planar(g, **kwargs):
    return graph_tool.topology.is_planar(g)

@build_representation("graph_tool")
def is_bipartite(g, **kwargs):
    return graph_tool.topology.is_bipartite(g)
'''
