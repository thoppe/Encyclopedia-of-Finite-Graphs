Encyclopedia of Finite Graphs
=============================

Set of tools and data to compute all known invariants for small finite graphs [incomplete].


*Authors*:

+ [Travis Hoppe](https://github.com/thoppe)
+ [ampetr](https://github.com/ampetr) 

*Roadmap*:

+ Document database structure
+ Add a few invariants, easy ones that can be computed with networkx, graph_tool
+ Write a better invariant "manager", right now just a loose collection
+ Compute the database for N=10 over these invariants
+ Build the query maker
+ Write the OEIS checker
+ Check OEIS against combinatorical queries
+ Check set relations for _interesting_ queries
+ Add harder invariants and repeat!
+ Submit new sequences to OEIS
+ Writeup project as an experimental math paper (data mining integer sequences over graphs?)

====================================

*Invariants*:

Calculated Invariants

+ [`n_edges`](http://mathworld.wolfram.com/EdgeCount.html) (trivial)
+ [`diameter`](http://mathworld.wolfram.com/GraphDiameter.html) (networkx)
+ [`radius`](http://mathworld.wolfram.com/GraphRadius.html) (networkx)
+ [`is_eulerian`](http://mathworld.wolfram.com/EulerianGraph.html) (networkx)
+ [`is_distance_regular`](http://mathworld.wolfram.com/Distance-RegularGraph.html) (networkx)
+ [`is_planar`](http://mathworld.wolfram.com/PlanarGraph.html) (graph_tool)
+ [`is_bipartite`](http://mathworld.wolfram.com/BipartiteGraph.html) (graph_tool)
+ [`n_articulation_points`](http://mathworld.wolfram.com/ArticulationVertex.html) (graph_tool)

Proposed Invariants

+ [`n_vertex`](http://mathworld.wolfram.com/VertexCount.html) (trivial)
+ `is_tree`
+ [`is_k_connected`](http://mathworld.wolfram.com/k-ConnectedGraph.html) Can k vertices be removed and graph is still planar? [`is_k_edge_connected`](http://mathworld.wolfram.com/k-Edge-ConnectedGraph.html)
+ [`n_non_adjacent_vertex_pairs`](http://mathworld.wolfram.com/NonadjacentVertexPairs.html)
+ [`crossing_number`](http://mathworld.wolfram.com/GraphCrossingNumber.html), [`toroidal_crossing_number`](http://mathworld.wolfram.com/ToroidalCrossingNumber.html)
+ [`n_peripheral_points`](http://mathworld.wolfram.com/PeripheralPoint.html)
+ [`sigma_polynomial`](http://mathworld.wolfram.com/SigmaPolynomial.html), [`is_royle`](http://mathworld.wolfram.com/RoyleGraphs.html)
+ [`maximum_clique`](http://mathworld.wolfram.com/MaximalClique.html) (graph_tool, networkx)
+ `n_subgraph_A` Number of subgraphs of type A (graph_tool), [`is_triangle_free`](http://mathworld.wolfram.com/Triangle-FreeGraph.html), [`is_square_free`](http://mathworld.wolfram.com/Square-FreeGraph.html), [`hajos_number`](http://mathworld.wolfram.com/HajosNumber.html)
+ [`n_eulerian_cycle`](http://mathworld.wolfram.com/EulerianCycle.html)
+ [`girth`](http://mathworld.wolfram.com/Girth.html)
+ [`is_k_regular`](http://mathworld.wolfram.com/RegularGraph.html)
+ [`is_integral`](http://mathworld.wolfram.com/IntegralGraph.html)
+ [`automorphism_group_order`](http://mathworld.wolfram.com/GraphAutomorphism.html) (nauty)
+ [`circumference`](http://mathworld.wolfram.com/GraphCircumference.html)
+ [`is_hamiltonian`](http://mathworld.wolfram.com/HamiltonianGraph.html), [`n_hamiltonian_cycles`](http://mathworld.wolfram.com/HamiltonianCycle.html), ['n_hamiltonian_paths'](http://mathworld.wolfram.com/HamiltonianPath.html)
+ [`is_perfect`](http://mathworld.wolfram.com/PerfectGraph.html)
+ [`chromatic_number`](http://mathworld.wolfram.com/ChromaticNumber.html), [`chromatic_polynomial`](http://mathworld.wolfram.com/ChromaticPolynomial.html), [`k_colorings`](http://mathworld.wolfram.com/k-Coloring.html)
+ [`is_arc_transitive`](http://mathworld.wolfram.com/Arc-TransitiveGraph.html)
+ [`is_vertex_transitive`](http://mathworld.wolfram.com/Vertex-TransitiveGraph.html)
+ [`is_bridge`](http://mathworld.wolfram.com/BridgedGraph.html)
+ [`characteristic_polynomial`](http://mathworld.wolfram.com/CharacteristicPolynomial.html)
+ [`spectrum`](http://mathworld.wolfram.com/GraphSpectrum.html)
+ [`degree_sequence`](http://mathworld.wolfram.com/DegreeSequence.html), [`n_endpoints`](http://mathworld.wolfram.com/Endpoint.html) (trivial)
+ [`domination_number`](http://mathworld.wolfram.com/DominationNumber.html)
+ [`coarseness`](http://mathworld.wolfram.com/GraphCoarseness.html), [`thickness`](http://mathworld.wolfram.com/GraphThickness.html)
+ [`genus`](http://mathworld.wolfram.com/GraphGenus.html), [`skewness`](http://mathworld.wolfram.com/GraphSkewness.html)
+ [`independence_number`](http://mathworld.wolfram.com/IndependenceNumber.html)
