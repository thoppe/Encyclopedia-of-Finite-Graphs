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
            return 1

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

