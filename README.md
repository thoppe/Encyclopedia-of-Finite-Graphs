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

+ `n_edge number of edges` (trivial)
+ [`diameter`](http://mathworld.wolfram.com/GraphDiameter.html) (networkx)
+ [`radius`](http://mathworld.wolfram.com/GraphRadius.html) (networkx)
+ [`is_eulerian`](http://mathworld.wolfram.com/EulerianGraph.html) (networkx)
+ [`is_distance_regular`](http://mathworld.wolfram.com/Distance-RegularGraph.html) (networkx)
+ [`is_planar`](http://mathworld.wolfram.com/PlanarGraph.html) (graph_tool)
+ [`is_bipartite`](http://mathworld.wolfram.com/BipartiteGraph.html) (graph_tool)
+ [`n_articulation_points`](http://mathworld.wolfram.com/ArticulationVertex.html) (graph_tool)

Proposed Invariants

+ `n_vertex` (trivial)
+ [`maximum_clique`](http://mathworld.wolfram.com/MaximalClique.html) (graph_tool, networkx)
+ `n_subgraph_A` Number of subgraphs of type A (graph_tool)
+ [`n_eulerian_cycle`](http://mathworld.wolfram.com/EulerianCycle.html)
+ [`girth`](http://mathworld.wolfram.com/Girth.html)
+ [`is_k_regular`](http://mathworld.wolfram.com/RegularGraph.html)
+ [`is_integral`](http://mathworld.wolfram.com/IntegralGraph.html)
+ [`automorphism_group_order`](http://mathworld.wolfram.com/GraphAutomorphism.html) (nauty)
+ [`circumference`](http://mathworld.wolfram.com/GraphCircumference.html)
+ [`is_hamiltonian` and `n_hamiltonian_cycles`](http://mathworld.wolfram.com/HamiltonianGraph.html)



