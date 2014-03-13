Encyclopedia of Finite Graphs
=============================

Set of tools and data to compute all known invariants for small finite graphs [incomplete].


*Authors*:

+ [Travis Hoppe](https://github.com/thoppe)
+ [ampetr](https://github.com/ampetr) 

*Roadmap*:

+ Write unit-tests for known sequences
+ Signup and template OEIS response (bfile and submission)
+ Submit new sequences to OEIS
+ Document these submissions
+ Add harder invariants and repeat!
+ Check set relations for _interesting_ queries
+ Writeup project as an experimental math paper (Automatic integer sequence discovery from small graphs?)

*Lower priority tasks*

+ Document database structure
+ Write a better invariant "manager", right now just a loose collection

====================================

*Invariants*:

Calculated Invariants

+ [`n_edges`](http://mathworld.wolfram.com/EdgeCount.html), [`n_vertex`](http://mathworld.wolfram.com/VertexCount.html) (trivial)
+ [`diameter`](http://mathworld.wolfram.com/GraphDiameter.html) (networkx)
+ [`radius`](http://mathworld.wolfram.com/GraphRadius.html) (networkx)
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
+ [`automorphism_group_order`](http://mathworld.wolfram.com/GraphAutomorphism.html) (nauty)
+ [`is_integral`](http://mathworld.wolfram.com/IntegralGraph.html) (numpy,sympy)

Proposed Invariants

+ [`is_hamiltonian`](http://mathworld.wolfram.com/HamiltonianGraph.html), [`n_hamiltonian_cycles`](http://mathworld.wolfram.com/HamiltonianCycle.html), [`n_hamiltonian_paths`](http://mathworld.wolfram.com/HamiltonianPath.html)
+ [`is_k_connected`](http://mathworld.wolfram.com/k-ConnectedGraph.html) Can k vertices be removed and graph is still planar? [`is_k_edge_connected`](http://mathworld.wolfram.com/k-Edge-ConnectedGraph.html)
+ [`k_vertex_connectivity`](http://mathworld.wolfram.com/VertexConnectivity.html)[`k_edge_connectivity`](http://mathworld.wolfram.com/EdgeConnectivity.html) minimal number of nodes/edges that can be deleted to disconnect the graph.
+ [`maximum_clique`](http://mathworld.wolfram.com/MaximalClique.html) (graph_tool, networkx)
+ [`is_perfect`](http://mathworld.wolfram.com/PerfectGraph.html)
+ [`is_arc_transitive`](http://mathworld.wolfram.com/Arc-TransitiveGraph.html), [`is_vertex_transitive`](http://mathworld.wolfram.com/Vertex-TransitiveGraph.html)
+ [`is_bridge`](http://mathworld.wolfram.com/BridgedGraph.html)
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

====================================

*Unit tests*:

Passed

[`is_eulerian = 1`](http://oeis.org/A003049)
[`is_k_regular = 3`](http://oeis.org/A002851)
[`is_k_regular = 4`](http://oeis.org/A006820)
[`is_k_regular = 5`](http://oeis.org/A006820)
[`is_k_regular = 6`](http://oeis.org/A006822)
[`is_k_regular = 7`](http://oeis.org/A014377)
[`is_k_regular = 8`](http://oeis.org/A014378)
[`is_strongly_regular = 1`](http://oeis.org/A088741)

[`chromatic_number = 2`](http://oeis.org/A005142)
[`chromatic_number = 3`](http://oeis.org/A126737)
[`chromatic_number = 4`](http://oeis.org/A126738)
[`chromatic_number = 5`](http://oeis.org/A126739)
[`chromatic_number = 6`](http://oeis.org/A126740)
