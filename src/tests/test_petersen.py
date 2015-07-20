from nose.tools import *
from unittest import TestCase
import src.helper_functions as helper

import networkx as nx
import numpy as np

from invariants.integer import *

options = helper.load_options("options_simple_connected.json")


# Invariant tests are run in the order listed here.
# Results proprogate forward to future invariants if needed.

petersen_graph = [
    ("automorphism_group_n", 120),
    ("diameter", 2),
]


class test_petersen(object):

    gx = nx.petersen_graph()
    A  = np.array(nx.to_numpy_matrix(gx)).astype(np.int)
    _upper_matrix_index = np.triu_indices(10)
    au = ''.join(map(str, A[_upper_matrix_index]))
    int_index = int(au, 2)

    known_invariants = {}
    
    def invariant_func(self, *args):
        data = {"twos_representation":self.int_index, "N":10}
        name, expected_result = args
        
        # Copy any invariants already known
        data.update(self.known_invariants)
        
        func = globals()[name]()
        result = func(data)
        assert(result == expected_result)
        self.known_invariants[name] = result

    def test_invariants(self):
        
        for name, value in petersen_graph:
            
            yield self.invariant_func, name, value
