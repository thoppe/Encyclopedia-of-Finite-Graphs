from nose.tools import *
from unittest import TestCase
import EoGF.helper_functions as helper

import networkx as nx
import numpy as np

from EoGF.invariants.integer import *
from EoGF.invariants.boolean import *
from EoGF.invariants.subgraph import *
from EoGF.invariants.polynomial import *

options = helper.load_options("options_simple_connected.json")


# Invariant tests are run in the order listed here.
# Results proprogate forward to future invariants if needed.

petersen_graph = [
    ("automorphism_group_n", 120),
    ("diameter", 2),
    ("n_edge", 15),
    ("radius", 2),
    ("girth", 5),
    ("is_planar", False),
    ("vertex_connectivity", 3),
    ("k_max_clique", 2),
    ("is_eulerian", False),
    ("is_hamiltonian", False),
    ("is_integral", True),
    ("edge_connectivity", 3),
    ("n_endpoints", 0),
    ("is_tree", False),
    ("is_chordal", False),   
    ("is_strongly_regular", True),
    ("is_distance_regular", True),
    ("is_subgraph_free_K3", True),
    ("is_subgraph_free_C4", True),

    ("independent_vertex_set_polynomial", [0,0,0,0,0,0,5,30,30,10,1]),
    ("independence_number", 4),
    
    ("degree_sequence",[3,]*10),
    ("k_regular", 3),

    
    
    ("characteristic_polynomial", [1,0,-15,0,75,-24,-165,120,120,-160,48]),
    ("chromatic_polynomial", [1,-15,105,-455,1353,-2861,
                              4275,-4305,2606,-704,0]),
    ("chromatic_number",3)
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

        # Check if result is numpy
        try:
            if type(result).__module__ == np.__name__:
                assert((result == np.array(expected_result)).all())
            else:
                assert(result == expected_result)
        except:
            msg = "{} vs {}".format(result, expected_result)
            raise ValueError(msg)
            
        self.known_invariants[name] = result

    def test_invariants(self):
        
        for name, value in petersen_graph:
            
            yield self.invariant_func, name, value
