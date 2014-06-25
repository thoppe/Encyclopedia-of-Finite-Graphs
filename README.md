Encyclopedia of Finite Graphs
=============================

This project has three major aims, 

1. To build an exhaustive reference database for all graphs of a given type. 
2. To "mine" this database for sequences not present (or incomplete) in the [OEIS](https://oeis.org/). 
3. To use these sequences to suggest new mathematical relations between graph invariants.

*Authors*:

+ [Travis Hoppe](https://github.com/thoppe)
+ [Anna Petrone](https://github.com/ampetr) 

*Roadmap*:

+ [`Writeup`](report/report.tex) for submission to either [Journal of Integer Sequences](https://cs.uwaterloo.ca/journals/JIS/), [Discrete Applied Mathematics](www.journals.elsevier.com/discrete-applied-mathematics/), [Experimental Mathematics](http://www.tandfonline.com/loi/uexm20).

=======================

### [Sequence Extensions](verification/submission_ext.md)
List of the sequences extended by the project.

### [New Sequences (level 1)](verification/submission_lvl1.md)
List of the sequences discovered by the project.

### [New Sequences (level 2)](verification/submission_lvl2.md)
List of the paired sequences discovered by the project.

### [Relations](verification/relations.md)
List of all the interesting (equality, subset and exclusive) relations between the sequences found.

### [Unit Tests](verification/unit_tests.md)
An auto-generated reported for various base queries and the link to the respective OEIS sequence.

====================================

**Invariants**

Calculated Invariants

+ [`n_edges`](http://mathworld.wolfram.com/EdgeCount.html), [`n_vertex`](http://mathworld.wolfram.com/VertexCount.html) (trivial)
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
+ `is_subgraph_free_bull`, `is_subgraph_free_bowtie`, `is_subgraph_free_diamond`, `is_subgraph_free_paw`, `is_subgraph_free_banner`, `is_subgraph_free_open_bowtie`

Fractional invariants

+ [`has_fractional_duality_gap_vertex_chromatic`](http://en.wikipedia.org/wiki/Fractional_coloring)

Others

+ [`maximal_independent_vertex_set`](http://mathworld.wolfram.com/IndependenceNumber.html) also called the Independence number, [`n_independent_vertex_sets`](http://mathworld.wolfram.com/IndependentVertexSet.html)


=======================

Proposed Invariants

+ [`n_hamiltonian_cycles`](http://mathworld.wolfram.com/HamiltonianCycle.html) [`n_hamiltonian_paths`](http://mathworld.wolfram.com/HamiltonianPath.html)
+ [`is_perfect`](http://mathworld.wolfram.com/PerfectGraph.html) (SAGE)
+ [`is_arc_transitive`](http://mathworld.wolfram.com/Arc-TransitiveGraph.html), [`is_vertex_transitive`](http://mathworld.wolfram.com/Vertex-TransitiveGraph.html)
+ [`characteristic_polynomial`](http://mathworld.wolfram.com/CharacteristicPolynomial.html)
+ [`spectrum`](http://mathworld.wolfram.com/GraphSpectrum.html)
+ [`is_cartesian_product`](mathworld.wolfram.com/GraphCartesianProduct.html) (SAGE)
+ [`is_well_covered`](http://mathworld.wolfram.com/Well-CoveredGraph.html)

Other Invariants (hard)

+ [`hajos_number`](http://mathworld.wolfram.com/HajosNumber.html)
+ [`hosoya_index`](http://mathworld.wolfram.com/HosoyaIndex.html)
+ [`crossing_number`](http://mathworld.wolfram.com/GraphCrossingNumber.html), [`toroidal_crossing_number`](http://mathworld.wolfram.com/ToroidalCrossingNumber.html)
+ [`sigma_polynomial`](http://mathworld.wolfram.com/SigmaPolynomial.html), [`is_royle`](http://mathworld.wolfram.com/RoyleGraphs.html)
+ [`domination_number`](http://mathworld.wolfram.com/DominationNumber.html)
+ [`coarseness`](http://mathworld.wolfram.com/GraphCoarseness.html), [`thickness`](http://mathworld.wolfram.com/GraphThickness.html)
+ [`genus`](http://mathworld.wolfram.com/GraphGenus.html), [`skewness`](http://mathworld.wolfram.com/GraphSkewness.html)

Other Invariants (trivial)
+ [`n_non_adjacent_vertex_pairs`](http://mathworld.wolfram.com/NonadjacentVertexPairs.html)
+ [`n_peripheral_points`](http://mathworld.wolfram.com/PeripheralPoint.html)

