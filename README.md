Encyclopedia of Finite Graphs
=============================

Set of tools and data to compute all known invariants for small finite graphs [in progress].
The project has three major aims, 

1. To build an exhaustive reference database for all graphs of a given type. 
2. To "mine" this database for sequences not present (or incomplete) in the [OEIS](https://oeis.org/). 
3. To use these sequences to suggest new mathematical relations between graph invariants.

*Authors*:

+ [Travis Hoppe](https://github.com/thoppe)
+ [Anna Petrone](https://github.com/ampetr) 

*Roadmap*:

+ Collect and submit level 1 sequences
+ Write search code for level 2+ sequences
+ Check set relations for _interesting_ queries
+ Writeup project as an experimental math paper (Automatic integer sequence discovery from small graphs?)

*Lower priority tasks*

+ Add harder invariants!
+ Write a better invariant "manager", right now just a loose collection

=======================

### [Sequence Extensions](verification/submission_ext.md)
List of the sequences extended by the project.

### [New Sequences (level 1)](verification/submission_lvl1.md)
[IN PROGRESS] List of the sequences discovered by the project.

### [Unit Tests](verification/report.md)
An auto-generated reported for various base queries and the link to the respective OEIS sequence.

##### New Sequences (level 2) [incomplete]
List of the paired sequences discovered by the project.

##### New Sequences (level 3+) [incomplete]
List of the triplet+ sequences discovered by the project.

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
+ [`is_subgraph_free_K3`](http://mathworld.wolfram.com/Triangle-FreeGraph.html) of which the n=0 case is a triangle-free graph. (graph_tool)
+ `is_subgraph_free_K4`, `is_subgraph_free_K5` (graph_tool)
+ [`is_subgraph_free_C4`](http://mathworld.wolfram.com/Square-FreeGraph.html), ..., `is_subgraph_free_C10` checks for cycles of length k (graph_tool)
+ [`degree_sequence`](http://mathworld.wolfram.com/DegreeSequence.html), [`n_endpoints`](http://mathworld.wolfram.com/Endpoint.html) (trivial), [`is_k_regular`](http://mathworld.wolfram.com/RegularGraph.html), [`is_strongly_regular`](http://mathworld.wolfram.com/StronglyRegularGraph.html)
+ [`tutte_polynomial`](http://mathworld.wolfram.com/TuttePolynomial.html) via the [`chromatic_polynomial`](http://mathworld.wolfram.com/ChromaticPolynomial.html) leads to the [`chromatic_number`](http://mathworld.wolfram.com/ChromaticNumber.html)
+ [`automorphism_group_order`](http://mathworld.wolfram.com/GraphAutomorphism.html) (BLISS)
+ [`k_vertex_connectivity`](http://mathworld.wolfram.com/VertexConnectivity.html)[`k_edge_connectivity`](http://mathworld.wolfram.com/EdgeConnectivity.html) minimal number of nodes/edges that can be deleted to disconnect the graph.
+ [`is_chordal`](http://mathworld.wolfram.com/ChordalGraph.html) (networkx)
+ [`k_max_clique`](http://mathworld.wolfram.com/CliqueNumber.html) (networkx)
+ [`is_integral`](http://mathworld.wolfram.com/IntegralGraph.html) (sympy)

=======================

Proposed Invariants

+ [`is_hamiltonian`](http://mathworld.wolfram.com/HamiltonianGraph.html), [`n_hamiltonian_cycles`](http://mathworld.wolfram.com/HamiltonianCycle.html), [`n_hamiltonian_paths`](http://mathworld.wolfram.com/HamiltonianPath.html)
+ [`is_perfect`](http://mathworld.wolfram.com/PerfectGraph.html)
+ [`is_arc_transitive`](http://mathworld.wolfram.com/Arc-TransitiveGraph.html), [`is_vertex_transitive`](http://mathworld.wolfram.com/Vertex-TransitiveGraph.html)
+ [`characteristic_polynomial`](http://mathworld.wolfram.com/CharacteristicPolynomial.html)
+ [`spectrum`](http://mathworld.wolfram.com/GraphSpectrum.html)

Other Invariants (hard)

+ [`hajos_number`](http://mathworld.wolfram.com/HajosNumber.html)
+ [`hosoya_index`](http://mathworld.wolfram.com/HosoyaIndex.html)
+ [`crossing_number`](http://mathworld.wolfram.com/GraphCrossingNumber.html), [`toroidal_crossing_number`](http://mathworld.wolfram.com/ToroidalCrossingNumber.html)
+ [`sigma_polynomial`](http://mathworld.wolfram.com/SigmaPolynomial.html), [`is_royle`](http://mathworld.wolfram.com/RoyleGraphs.html)
+ [`domination_number`](http://mathworld.wolfram.com/DominationNumber.html)
+ [`coarseness`](http://mathworld.wolfram.com/GraphCoarseness.html), [`thickness`](http://mathworld.wolfram.com/GraphThickness.html)
+ [`genus`](http://mathworld.wolfram.com/GraphGenus.html), [`skewness`](http://mathworld.wolfram.com/GraphSkewness.html)
+ [`independence_number`](http://mathworld.wolfram.com/IndependenceNumber.html)

Other Invariants (trivial)
+ [`n_non_adjacent_vertex_pairs`](http://mathworld.wolfram.com/NonadjacentVertexPairs.html)
+ [`n_peripheral_points`](http://mathworld.wolfram.com/PeripheralPoint.html)

