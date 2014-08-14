import unittest
import invariants
import networkx as nx
import numpy as np

petersen_prop = {
    "n_vertex": 10,
    "n_edge": 15,
    "automorphism_group_n": 120,
    "radius": 2,
    "diameter": 2,
    "girth": 5,
    "chromatic_number": 3,
    "k_max_clique": 2,
    "is_eulerian": False,
    "is_hamiltonian": False,
    "is_integral": True,
    "maximal_independent_vertex_set": 4,
    "is_k_regular": 3,
    "is_strongly_regular": True,
    "is_distance_regular": True,
    "is_planar": False,
    "is_subgraph_free_K3": True,
    "is_subgraph_free_C4": True,
    "vertex_connectivity": 3,
    "edge_connectivity": 3,
    "n_endpoints": 0,
    "is_tree": False,
    "is_chordal": False,
}

import logging
# Start the logger

# logging.root.setLevel(logging.INFO)
logging.info("Testing the Petersen graph for all the invariants")

logging.info("Creating the graph.")
g = nx.petersen_graph()

logging.info("Converting to adj. format")
adj = invariants.convert_nx_to_adj(g)

N = 10
args = {"N": N}

logging.info("Computing the Tutte polynomial")
p = invariants.special_polynomial_tutte(adj, **args)
args["tutte_polynomial"] = p

logging.info("Computing the chromatic polynomial")
p = invariants.special_chromatic_polynomial(adj, **args)
args["chromatic_polynomial"] = p

logging.info("Computing the degree sequence")
p = invariants.special_degree_sequence(adj, **args)
args["degree_sequence"] = np.array(p).ravel()

logging.info("Computing the fractional chromatic number")
p = invariants.fractional_chromatic_number(adj, **args)
args["fractional_chromatic_number"] = p[0]

logging.info("Computing the characteristic polynomial")
p = invariants.special_characteristic_polynomial(adj, **args)
args["characteristic_polynomial"] = p

logging.info("Computing the laplacian polynomial")
p = invariants.special_laplacian_polynomial(adj, **args)
args["laplacian_polynomial"] = p

logging.info("Computing the independent vertex sets")
p = invariants.special_independent_vertex_sets(adj, **args)
args["independent_vertex_sets"] = p

logging.info("Computing the independent edge sets")
p = invariants.special_independent_edge_sets(adj, **args)
args["independent_edge_sets"] = p

logging.info("Computing the cycle basis")
import collections
p = invariants.special_cycle_basis(adj, **args)
cb = collections.defaultdict(list)
for cycle_k, idx in p:
    cb[cycle_k].append(idx)
args["cycle_basis"] = cb.values()

''' TestMaker from StackOverflow: http://stackoverflow.com/a/25267641/249341 '''


class TestMaker(type):

    def __new__(cls, clsname, bases, dct):
        # Add a method to the class' __dict__ for every key in
        # the petersen_prop dict.
        for prop in petersen_prop:
            dct['test_{}'.format(prop)] = cls.make_test(prop)

        return super(TestMaker, cls).__new__(cls, clsname, bases, dct)

    @staticmethod
    def make_test(prop):
        # test_wrap is the method body that will be used for each
        # test
        def test_wrap(self):
            func = getattr(invariants, prop)
            self.assertEqual(func(self.adj, **self.args),
                             petersen_prop[prop])
        return test_wrap


class PetersenGraph(unittest.TestCase):
    __metaclass__ = TestMaker

    def setUp(self):
        self.args = args
        self.adj = adj


unittest.main(verbosity=2)
