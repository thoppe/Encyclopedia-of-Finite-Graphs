Encyclopedia of Finite Graphs
=============================
[![zenodo.11304.png](https://zenodo.org/badge/doi/10.5281/zenodo.11304.png)](http://dx.doi.org/10.5281/zenodo.11304)
_Encyclopedia of Finite Graphs code_

[![zenodo.11280.png](https://zenodo.org/badge/doi/10.5281/zenodo.11280.png)](http://dx.doi.org/10.5281/zenodo.11280)
_Simple Connected Graph Invariant database_

[![1408.3644](templates/arXiv_badge.png)](http://arxiv-web3.library.cornell.edu/abs/1408.3644)
_Integer sequence discovery from small graphs_

This project has three major aims, 

1. To build an exhaustive reference database for graph invariants of a given class. 
2. To "mine" this database for sequences not present (or incomplete) in the [OEIS](https://oeis.org/). 
3. To use these sequences to suggest new mathematical relations between graph invariants.

*Authors*: 
[**Travis Hoppe**](https://github.com/thoppe) and
[**Anna Petrone**](https://github.com/ampetr) 

*Requirements*: 
The Encyclopedia calls upon many external libraries to generate the data.
To fully repopulate the database, it requires 
[`numpy`](http://www.numpy.org/),
[`networkx`](https://networkx.github.io/),
[`graph-tool`](http://graph-tool.skewed.de/),
[`sympy`](http://sympy.org/en/index.html),
[`pulp`](http://code.google.com/p/pulp-or/) and,
[`nauty`](http://cs.anu.edu.au/~bdm/nauty/).
As an alternative, there is a standalone version of of the simple connected graph database for [download](http://dx.doi.org/10.5281/zenodo.11203). 

*Writeup*: 
[_Integer sequence discovery from small graphs_](http://arxiv-web3.library.cornell.edu/abs/1408.3644)

In preparation for submission to either [Journal of Integer Sequences](https://cs.uwaterloo.ca/journals/JIS/), [Discrete Applied Mathematics](http://www.journals.elsevier.com/discrete-applied-mathematics/), or the [Experimental Mathematics](http://www.tandfonline.com/loi/uexm20).

## Integer Sequences Discovered

A catalog of all the sequences discovered and submitted to the OEIS.

[**Sequence Extensions**](verification/submission_ext.md): 
Sequences present in the OEIS, but extended.

[**Distinct Sequences**](verification/distinct.md):
Sequences generated by distinct classes.

[**New Primary Sequences**](verification/submission_lvl1.md):
Sequences generated by a single invariant conditions.

[**Secondary Sequences**](verification/submission_lvl2.md):
Sequences generated by paired invariant conditions.

[**Relations**](verification/relations.md):
List of all the interesting (equality, subset and exclusive) relations between the sequences. 
Many of the relations are obviously true, some of these have been [collected in a table](verification/relations_obvious.md).

## Usage:

*Visualization*

Once the database is built, invariant conditions can be explored. For example, to display the only the three graphs that are simultaneously bipartite, integral and Eulerian with ten vertices:

    python viewer.py 10 -i is_bipartite 1 -i is_integral 1 -i is_eulerian 1

*Testing*

First compile the invariant calculations, and run the unit test on the Petersen graph:

    make compile
    make test

*Database*

You can automatically download an [updated copy of the database](https://github.com/thoppe/Simple-connected-graph-invariant-database) by cloning the database repository in the Encyclopedia directory:

    git submodule add https://github.com/thoppe/Simple-connected-graph-invariant-database.git database

Note that we are unable to store the special invariants for larger graphs due to size constraints; these larger special invariants will have to be recomputed for `n>6`.
We recommend rebuilding portions of the database as both a consistency check and a learning tool if you are considering adding additional invariants. 

If the database has been updated, you can grab a new copy by running:

    git submodule foreach git pull origin master

## Calculated Invariants

+ [`diameter`](http://mathworld.wolfram.com/GraphDiameter.html), [`radius`](http://mathworld.wolfram.com/GraphRadius.html) (networkx)
+ [`is_eulerian`](http://mathworld.wolfram.com/EulerianGraph.html) (networkx)
+ [`is_distance_regular`](http://mathworld.wolfram.com/Distance-RegularGraph.html) (networkx)
+ [`is_planar`](http://mathworld.wolfram.com/PlanarGraph.html) (graph_tool)
+ [`is_bipartite`](http://mathworld.wolfram.com/BipartiteGraph.html) (graph_tool)
+ [`n_articulation_points`](http://mathworld.wolfram.com/ArticulationVertex.html) (graph_tool)
+ [`n_cycle_basis`](http://en.wikipedia.org/wiki/Cycle_space) of which the n=0 case [`is_tree`](http://mathworld.wolfram.com/Tree.html) (networkx), [`circumference`](http://mathworld.wolfram.com/GraphCircumference.html), [`girth`](http://mathworld.wolfram.com/Girth.html)
+ [`degree_sequence`](http://mathworld.wolfram.com/DegreeSequence.html), [`n_endpoints`](http://mathworld.wolfram.com/Endpoint.html) (trivial), [`is_k_regular`](http://mathworld.wolfram.com/RegularGraph.html), [`is_strongly_regular`](http://mathworld.wolfram.com/StronglyRegularGraph.html)
+ [`tutte_polynomial`](http://mathworld.wolfram.com/TuttePolynomial.html) via the [`chromatic_polynomial`](http://mathworld.wolfram.com/ChromaticPolynomial.html) leads to the [`chromatic_number`](http://mathworld.wolfram.com/ChromaticNumber.html)
+ [`automorphism_group_order`](http://mathworld.wolfram.com/GraphAutomorphism.html) (BLISS)
+ [`k_vertex_connectivity`](http://mathworld.wolfram.com/VertexConnectivity.html)[`k_edge_connectivity`](http://mathworld.wolfram.com/EdgeConnectivity.html) minimal number of nodes/edges that can be deleted to disconnect the graph.
+ [`is_chordal`](http://mathworld.wolfram.com/ChordalGraph.html) (networkx)
+ [`k_max_clique`](http://mathworld.wolfram.com/CliqueNumber.html) (networkx)
+ [`is_hamiltonian`](http://mathworld.wolfram.com/HamiltonianGraph.html)

Spectrum invariants

+ [`is_integral`](http://mathworld.wolfram.com/IntegralGraph.html), (sympy)
+ `is_rational_spectrum`, `is_real_spectrum`

Subgraph invariants

+ [`is_subgraph_free_K3`](http://mathworld.wolfram.com/Triangle-FreeGraph.html) of which the n=0 case is a triangle-free graph. (graph_tool)
+ `is_subgraph_free_K4`, `is_subgraph_free_K5` (graph_tool)
+ [`is_subgraph_free_C4`](http://mathworld.wolfram.com/Square-FreeGraph.html), ..., `is_subgraph_free_C10` checks for cycles of length k (graph_tool)
+ [`is_subgraph_free_bull`](http://mathworld.wolfram.com/BullGraph.html), [`is_subgraph_free_bowtie`](http://mathworld.wolfram.com/ButterflyGraph.html), [`is_subgraph_free_diamond`](http://mathworld.wolfram.com/DiamondGraph.html), [`is_subgraph_free_open_bowtie`]()

Fractional invariants

+ [`has_fractional_duality_gap_vertex_chromatic`](http://en.wikipedia.org/wiki/Fractional_coloring)

Others

+ [`maximal_independent_vertex_set`](http://mathworld.wolfram.com/IndependentVertexSet.html) also called the [Independence number](http://mathworld.wolfram.com/IndependenceNumber.html), [`n_independent_vertex_sets`](http://mathworld.wolfram.com/IndependentVertexSet.html)
+ [`maximal_independent_edge_set`](http://mathworld.wolfram.com/MaximumIndependentEdgeSet.html), [`n_independent_edge_sets`](http://mathworld.wolfram.com/IndependentEdgeSet.html) also called the [Hosoya Index](http://mathworld.wolfram.com/HosoyaIndex.html).

Trivial invariants

+ [`n_edges`](http://mathworld.wolfram.com/EdgeCount.html)
+ [`n_vertex`](http://mathworld.wolfram.com/VertexCount.html)

## Future Invariants

+ [`n_hamiltonian_cycles`](http://mathworld.wolfram.com/HamiltonianCycle.html) [`n_hamiltonian_paths`](http://mathworld.wolfram.com/HamiltonianPath.html)
+ [`is_perfect`](http://mathworld.wolfram.com/PerfectGraph.html) (SAGE)
+ [`is_arc_transitive`](http://mathworld.wolfram.com/Arc-TransitiveGraph.html), [`is_vertex_transitive`](http://mathworld.wolfram.com/Vertex-TransitiveGraph.html)
+ [`characteristic_polynomial`](http://mathworld.wolfram.com/CharacteristicPolynomial.html)
+ [`spectrum`](http://mathworld.wolfram.com/GraphSpectrum.html)
+ [`is_cartesian_product`](mathworld.wolfram.com/GraphCartesianProduct.html) (SAGE)
+ [`is_well_covered`](http://mathworld.wolfram.com/Well-CoveredGraph.html)

Other Invariants (hard)

+ [`hajos_number`](http://mathworld.wolfram.com/HajosNumber.html)
+ [`crossing_number`](http://mathworld.wolfram.com/GraphCrossingNumber.html), [`toroidal_crossing_number`](http://mathworld.wolfram.com/ToroidalCrossingNumber.html)
+ [`sigma_polynomial`](http://mathworld.wolfram.com/SigmaPolynomial.html), [`is_royle`](http://mathworld.wolfram.com/RoyleGraphs.html)
+ [`domination_number`](http://mathworld.wolfram.com/DominationNumber.html)
+ [`coarseness`](http://mathworld.wolfram.com/GraphCoarseness.html), [`thickness`](http://mathworld.wolfram.com/GraphThickness.html)
+ [`genus`](http://mathworld.wolfram.com/GraphGenus.html), [`skewness`](http://mathworld.wolfram.com/GraphSkewness.html)

Other Invariants (trivial)
+ [`n_non_adjacent_vertex_pairs`](http://mathworld.wolfram.com/NonadjacentVertexPairs.html)
+ [`n_peripheral_points`](http://mathworld.wolfram.com/PeripheralPoint.html)

