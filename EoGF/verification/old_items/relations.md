# Equality relations (converse holds)
+ `diameter=1` <-> `maximal_independent_vertex_set=1`
+ `circumference=0` <-> `girth=0`
+ `circumference=0` <-> `is_tree=1`
+ `girth=0` <-> `circumference=0`
+ `girth=0` <-> `is_tree=1`
+ `n_articulation_points=0` <-> `vertex_connectivity>1`
+ `is_subgraph_free_K3=1` <-> `k_max_clique=2`
+ `is_subgraph_free_C8=1` <-> `is_subgraph_free_C9=1`
+ `is_subgraph_free_C8=1` <-> `is_subgraph_free_C10=1`
+ `is_subgraph_free_C8=1` <-> `vertex_connectivity>0`
+ `is_subgraph_free_C9=1` <-> `is_subgraph_free_C8=1`
+ `is_subgraph_free_C9=1` <-> `is_subgraph_free_C10=1`
+ `is_subgraph_free_C9=1` <-> `vertex_connectivity>0`
+ `is_subgraph_free_C10=1` <-> `is_subgraph_free_C8=1`
+ `is_subgraph_free_C10=1` <-> `is_subgraph_free_C9=1`
+ `is_subgraph_free_C10=1` <-> `vertex_connectivity>0`
+ `vertex_connectivity>0` <-> `is_subgraph_free_C8=1`
+ `vertex_connectivity>0` <-> `is_subgraph_free_C9=1`
+ `vertex_connectivity>0` <-> `is_subgraph_free_C10=1`
+ `vertex_connectivity>1` <-> `n_articulation_points=0`
+ `is_tree=1` <-> `circumference=0`
+ `is_tree=1` <-> `girth=0`
+ `k_max_clique=2` <-> `is_subgraph_free_K3=1`
+ `maximal_independent_vertex_set=1` <-> `diameter=1`

# Subset relations (converse is not true)
+ `circumference=0` -> `chromatic_number=2`
+ `girth=0` -> `chromatic_number=2`
+ `is_tree=1` -> `chromatic_number=2`
+ `circumference=3` -> `chromatic_number=3`
+ `chromatic_number=4` -> `girth=3`
+ `diameter=1` -> `girth=3`
+ `circumference=3` -> `girth=3`
+ `maximal_independent_vertex_set=1` -> `girth=3`
+ `automorphism_group_n=4` -> `is_k_regular=0`
+ `circumference=0` -> `is_k_regular=0`
+ `girth=0` -> `is_k_regular=0`
+ `n_articulation_points=1` -> `is_k_regular=0`
+ `n_articulation_points=2` -> `is_k_regular=0`
+ `edge_connectivity=1` -> `is_k_regular=0`
+ `is_tree=1` -> `is_k_regular=0`
+ `automorphism_group_n=2` -> `is_strongly_regular=0`
+ `automorphism_group_n=4` -> `is_strongly_regular=0`
+ `diameter=3` -> `is_strongly_regular=0`
+ `circumference=0` -> `is_strongly_regular=0`
+ `girth=0` -> `is_strongly_regular=0`
+ `is_k_regular=0` -> `is_strongly_regular=0`
+ `is_distance_regular=0` -> `is_strongly_regular=0`
+ `n_articulation_points=1` -> `is_strongly_regular=0`
+ `n_articulation_points=2` -> `is_strongly_regular=0`
+ `edge_connectivity=1` -> `is_strongly_regular=0`
+ `is_tree=1` -> `is_strongly_regular=0`
+ `is_distinct_spectrum=1` -> `is_strongly_regular=0`
+ `is_hamiltonian=0` -> `is_strongly_regular=0`
+ `diameter=1` -> `is_strongly_regular=1`
+ `maximal_independent_vertex_set=1` -> `is_strongly_regular=1`
+ `diameter=1` -> `radius=1`
+ `maximal_independent_vertex_set=1` -> `radius=1`
+ `maximal_independent_edge_set=1` -> `radius=1`
+ `n_articulation_points=2` -> `radius=2`
+ `circumference=0` -> `is_eulerian=0`
+ `girth=0` -> `is_eulerian=0`
+ `edge_connectivity=1` -> `is_eulerian=0`
+ `edge_connectivity=3` -> `is_eulerian=0`
+ `is_tree=1` -> `is_eulerian=0`
+ `automorphism_group_n=2` -> `is_distance_regular=0`
+ `automorphism_group_n=4` -> `is_distance_regular=0`
+ `circumference=0` -> `is_distance_regular=0`
+ `girth=0` -> `is_distance_regular=0`
+ `n_articulation_points=1` -> `is_distance_regular=0`
+ `n_articulation_points=2` -> `is_distance_regular=0`
+ `edge_connectivity=1` -> `is_distance_regular=0`
+ `is_tree=1` -> `is_distance_regular=0`
+ `is_distinct_spectrum=1` -> `is_distance_regular=0`
+ `is_hamiltonian=0` -> `is_distance_regular=0`
+ `diameter=1` -> `is_distance_regular=1`
+ `is_strongly_regular=1` -> `is_distance_regular=1`
+ `maximal_independent_vertex_set=1` -> `is_distance_regular=1`
+ `circumference=0` -> `is_planar=1`
+ `circumference=3` -> `is_planar=1`
+ `girth=0` -> `is_planar=1`
+ `is_k_regular=2` -> `is_planar=1`
+ `is_subgraph_free_C4=1` -> `is_planar=1`
+ `is_tree=1` -> `is_planar=1`
+ `maximal_independent_edge_set=1` -> `is_planar=1`
+ `diameter=1` -> `is_bipartite=0`
+ `is_subgraph_free_K3=0` -> `is_bipartite=0`
+ `is_subgraph_free_K4=0` -> `is_bipartite=0`
+ `k_max_clique=3` -> `is_bipartite=0`
+ `k_max_clique=4` -> `is_bipartite=0`
+ `is_subgraph_free_diamond=0` -> `is_bipartite=0`
+ `maximal_independent_vertex_set=1` -> `is_bipartite=0`
+ `diameter=1` -> `n_articulation_points=0`
+ `is_k_regular=2` -> `n_articulation_points=0`
+ `is_strongly_regular=1` -> `n_articulation_points=0`
+ `is_distance_regular=1` -> `n_articulation_points=0`
+ `vertex_connectivity>2` -> `n_articulation_points=0`
+ `is_hamiltonian=1` -> `n_articulation_points=0`
+ `maximal_independent_vertex_set=1` -> `n_articulation_points=0`
+ `diameter=1` -> `is_subgraph_free_K3=0`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_K3=0`
+ `k_max_clique=3` -> `is_subgraph_free_K3=0`
+ `k_max_clique=4` -> `is_subgraph_free_K3=0`
+ `is_subgraph_free_diamond=0` -> `is_subgraph_free_K3=0`
+ `maximal_independent_vertex_set=1` -> `is_subgraph_free_K3=0`
+ `is_bipartite=1` -> `is_subgraph_free_K3=1`
+ `k_max_clique=4` -> `is_subgraph_free_K4=0`
+ `circumference=0` -> `is_subgraph_free_K4=1`
+ `girth=0` -> `is_subgraph_free_K4=1`
+ `is_bipartite=1` -> `is_subgraph_free_K4=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_K4=1`
+ `is_subgraph_free_C4=1` -> `is_subgraph_free_K4=1`
+ `is_tree=1` -> `is_subgraph_free_K4=1`
+ `k_max_clique=2` -> `is_subgraph_free_K4=1`
+ `k_max_clique=3` -> `is_subgraph_free_K4=1`
+ `is_subgraph_free_diamond=1` -> `is_subgraph_free_K4=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_K4=1`
+ `chromatic_number=2` -> `is_subgraph_free_K5=1`
+ `circumference=0` -> `is_subgraph_free_K5=1`
+ `circumference=3` -> `is_subgraph_free_K5=1`
+ `circumference=4` -> `is_subgraph_free_K5=1`
+ `girth=0` -> `is_subgraph_free_K5=1`
+ `girth=4` -> `is_subgraph_free_K5=1`
+ `is_k_regular=2` -> `is_subgraph_free_K5=1`
+ `is_planar=1` -> `is_subgraph_free_K5=1`
+ `is_bipartite=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_K4=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_C4=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_C5=1` -> `is_subgraph_free_K5=1`
+ `is_tree=1` -> `is_subgraph_free_K5=1`
+ `k_max_clique=2` -> `is_subgraph_free_K5=1`
+ `k_max_clique=3` -> `is_subgraph_free_K5=1`
+ `k_max_clique=4` -> `is_subgraph_free_K5=1`
+ `is_distinct_spectrum=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_bull=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_bowtie=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_diamond=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_open_bowtie=1` -> `is_subgraph_free_K5=1`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `is_subgraph_free_K5=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_C4=0`
+ `vertex_connectivity>2` -> `is_subgraph_free_C4=0`
+ `edge_connectivity=3` -> `is_subgraph_free_C4=0`
+ `k_max_clique=4` -> `is_subgraph_free_C4=0`
+ `is_subgraph_free_diamond=0` -> `is_subgraph_free_C4=0`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C4=1`
+ `is_bipartite=1` -> `is_subgraph_free_C5=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C5=1`
+ `circumference=0` -> `is_subgraph_free_C6=1`
+ `girth=0` -> `is_subgraph_free_C6=1`
+ `n_articulation_points=2` -> `is_subgraph_free_C6=1`
+ `is_tree=1` -> `is_subgraph_free_C6=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C6=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C6=1`
+ `circumference=0` -> `is_subgraph_free_C7=1`
+ `circumference=3` -> `is_subgraph_free_C7=1`
+ `circumference=4` -> `is_subgraph_free_C7=1`
+ `girth=0` -> `is_subgraph_free_C7=1`
+ `is_k_regular=2` -> `is_subgraph_free_C7=1`
+ `is_bipartite=1` -> `is_subgraph_free_C7=1`
+ `n_articulation_points=1` -> `is_subgraph_free_C7=1`
+ `n_articulation_points=2` -> `is_subgraph_free_C7=1`
+ `edge_connectivity=1` -> `is_subgraph_free_C7=1`
+ `is_tree=1` -> `is_subgraph_free_C7=1`
+ `is_hamiltonian=0` -> `is_subgraph_free_C7=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C7=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C7=1`
+ `automorphism_group_n=2` -> `is_subgraph_free_C8=1`
+ `automorphism_group_n=4` -> `is_subgraph_free_C8=1`
+ `automorphism_group_n=6` -> `is_subgraph_free_C8=1`
+ `automorphism_group_n=8` -> `is_subgraph_free_C8=1`
+ `automorphism_group_n=24` -> `is_subgraph_free_C8=1`
+ `chromatic_number=2` -> `is_subgraph_free_C8=1`
+ `chromatic_number=3` -> `is_subgraph_free_C8=1`
+ `chromatic_number=4` -> `is_subgraph_free_C8=1`
+ `diameter=1` -> `is_subgraph_free_C8=1`
+ `diameter=2` -> `is_subgraph_free_C8=1`
+ `diameter=3` -> `is_subgraph_free_C8=1`
+ `circumference=0` -> `is_subgraph_free_C8=1`
+ `circumference=3` -> `is_subgraph_free_C8=1`
+ `circumference=4` -> `is_subgraph_free_C8=1`
+ `girth=0` -> `is_subgraph_free_C8=1`
+ `girth=3` -> `is_subgraph_free_C8=1`
+ `girth=4` -> `is_subgraph_free_C8=1`
+ `is_k_regular=0` -> `is_subgraph_free_C8=1`
+ `is_k_regular=2` -> `is_subgraph_free_C8=1`
+ `is_strongly_regular=0` -> `is_subgraph_free_C8=1`
+ `is_strongly_regular=1` -> `is_subgraph_free_C8=1`
+ `radius=1` -> `is_subgraph_free_C8=1`
+ `radius=2` -> `is_subgraph_free_C8=1`
+ `is_eulerian=0` -> `is_subgraph_free_C8=1`
+ `is_eulerian=1` -> `is_subgraph_free_C8=1`
+ `is_distance_regular=0` -> `is_subgraph_free_C8=1`
+ `is_distance_regular=1` -> `is_subgraph_free_C8=1`
+ `is_planar=1` -> `is_subgraph_free_C8=1`
+ `is_bipartite=0` -> `is_subgraph_free_C8=1`
+ `is_bipartite=1` -> `is_subgraph_free_C8=1`
+ `n_articulation_points=0` -> `is_subgraph_free_C8=1`
+ `n_articulation_points=1` -> `is_subgraph_free_C8=1`
+ `n_articulation_points=2` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_K3=0` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_K4=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_K5=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_C4=0` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_C4=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_C5=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_C6=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_C7=1` -> `is_subgraph_free_C8=1`
+ `is_integral=0` -> `is_subgraph_free_C8=1`
+ `is_integral=1` -> `is_subgraph_free_C8=1`
+ `vertex_connectivity>1` -> `is_subgraph_free_C8=1`
+ `vertex_connectivity>2` -> `is_subgraph_free_C8=1`
+ `edge_connectivity=1` -> `is_subgraph_free_C8=1`
+ `edge_connectivity=2` -> `is_subgraph_free_C8=1`
+ `edge_connectivity=3` -> `is_subgraph_free_C8=1`
+ `is_tree=0` -> `is_subgraph_free_C8=1`
+ `is_tree=1` -> `is_subgraph_free_C8=1`
+ `is_chordal=0` -> `is_subgraph_free_C8=1`
+ `is_chordal=1` -> `is_subgraph_free_C8=1`
+ `k_max_clique=2` -> `is_subgraph_free_C8=1`
+ `k_max_clique=3` -> `is_subgraph_free_C8=1`
+ `k_max_clique=4` -> `is_subgraph_free_C8=1`
+ `is_distinct_spectrum=0` -> `is_subgraph_free_C8=1`
+ `is_distinct_spectrum=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_bull=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_bowtie=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_diamond=0` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_diamond=1` -> `is_subgraph_free_C8=1`
+ `is_subgraph_free_open_bowtie=1` -> `is_subgraph_free_C8=1`
+ `is_hamiltonian=0` -> `is_subgraph_free_C8=1`
+ `is_hamiltonian=1` -> `is_subgraph_free_C8=1`
+ `has_fractional_duality_gap_vertex_chromatic=0` -> `is_subgraph_free_C8=1`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `is_subgraph_free_C8=1`
+ `maximal_independent_vertex_set=1` -> `is_subgraph_free_C8=1`
+ `maximal_independent_vertex_set=2` -> `is_subgraph_free_C8=1`
+ `maximal_independent_vertex_set=3` -> `is_subgraph_free_C8=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C8=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C8=1`
+ `automorphism_group_n=2` -> `is_subgraph_free_C9=1`
+ `automorphism_group_n=4` -> `is_subgraph_free_C9=1`
+ `automorphism_group_n=6` -> `is_subgraph_free_C9=1`
+ `automorphism_group_n=8` -> `is_subgraph_free_C9=1`
+ `automorphism_group_n=24` -> `is_subgraph_free_C9=1`
+ `chromatic_number=2` -> `is_subgraph_free_C9=1`
+ `chromatic_number=3` -> `is_subgraph_free_C9=1`
+ `chromatic_number=4` -> `is_subgraph_free_C9=1`
+ `diameter=1` -> `is_subgraph_free_C9=1`
+ `diameter=2` -> `is_subgraph_free_C9=1`
+ `diameter=3` -> `is_subgraph_free_C9=1`
+ `circumference=0` -> `is_subgraph_free_C9=1`
+ `circumference=3` -> `is_subgraph_free_C9=1`
+ `circumference=4` -> `is_subgraph_free_C9=1`
+ `girth=0` -> `is_subgraph_free_C9=1`
+ `girth=3` -> `is_subgraph_free_C9=1`
+ `girth=4` -> `is_subgraph_free_C9=1`
+ `is_k_regular=0` -> `is_subgraph_free_C9=1`
+ `is_k_regular=2` -> `is_subgraph_free_C9=1`
+ `is_strongly_regular=0` -> `is_subgraph_free_C9=1`
+ `is_strongly_regular=1` -> `is_subgraph_free_C9=1`
+ `radius=1` -> `is_subgraph_free_C9=1`
+ `radius=2` -> `is_subgraph_free_C9=1`
+ `is_eulerian=0` -> `is_subgraph_free_C9=1`
+ `is_eulerian=1` -> `is_subgraph_free_C9=1`
+ `is_distance_regular=0` -> `is_subgraph_free_C9=1`
+ `is_distance_regular=1` -> `is_subgraph_free_C9=1`
+ `is_planar=1` -> `is_subgraph_free_C9=1`
+ `is_bipartite=0` -> `is_subgraph_free_C9=1`
+ `is_bipartite=1` -> `is_subgraph_free_C9=1`
+ `n_articulation_points=0` -> `is_subgraph_free_C9=1`
+ `n_articulation_points=1` -> `is_subgraph_free_C9=1`
+ `n_articulation_points=2` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_K3=0` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_K4=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_K5=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_C4=0` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_C4=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_C5=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_C6=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_C7=1` -> `is_subgraph_free_C9=1`
+ `is_integral=0` -> `is_subgraph_free_C9=1`
+ `is_integral=1` -> `is_subgraph_free_C9=1`
+ `vertex_connectivity>1` -> `is_subgraph_free_C9=1`
+ `vertex_connectivity>2` -> `is_subgraph_free_C9=1`
+ `edge_connectivity=1` -> `is_subgraph_free_C9=1`
+ `edge_connectivity=2` -> `is_subgraph_free_C9=1`
+ `edge_connectivity=3` -> `is_subgraph_free_C9=1`
+ `is_tree=0` -> `is_subgraph_free_C9=1`
+ `is_tree=1` -> `is_subgraph_free_C9=1`
+ `is_chordal=0` -> `is_subgraph_free_C9=1`
+ `is_chordal=1` -> `is_subgraph_free_C9=1`
+ `k_max_clique=2` -> `is_subgraph_free_C9=1`
+ `k_max_clique=3` -> `is_subgraph_free_C9=1`
+ `k_max_clique=4` -> `is_subgraph_free_C9=1`
+ `is_distinct_spectrum=0` -> `is_subgraph_free_C9=1`
+ `is_distinct_spectrum=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_bull=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_bowtie=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_diamond=0` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_diamond=1` -> `is_subgraph_free_C9=1`
+ `is_subgraph_free_open_bowtie=1` -> `is_subgraph_free_C9=1`
+ `is_hamiltonian=0` -> `is_subgraph_free_C9=1`
+ `is_hamiltonian=1` -> `is_subgraph_free_C9=1`
+ `has_fractional_duality_gap_vertex_chromatic=0` -> `is_subgraph_free_C9=1`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `is_subgraph_free_C9=1`
+ `maximal_independent_vertex_set=1` -> `is_subgraph_free_C9=1`
+ `maximal_independent_vertex_set=2` -> `is_subgraph_free_C9=1`
+ `maximal_independent_vertex_set=3` -> `is_subgraph_free_C9=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C9=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C9=1`
+ `automorphism_group_n=2` -> `is_subgraph_free_C10=1`
+ `automorphism_group_n=4` -> `is_subgraph_free_C10=1`
+ `automorphism_group_n=6` -> `is_subgraph_free_C10=1`
+ `automorphism_group_n=8` -> `is_subgraph_free_C10=1`
+ `automorphism_group_n=24` -> `is_subgraph_free_C10=1`
+ `chromatic_number=2` -> `is_subgraph_free_C10=1`
+ `chromatic_number=3` -> `is_subgraph_free_C10=1`
+ `chromatic_number=4` -> `is_subgraph_free_C10=1`
+ `diameter=1` -> `is_subgraph_free_C10=1`
+ `diameter=2` -> `is_subgraph_free_C10=1`
+ `diameter=3` -> `is_subgraph_free_C10=1`
+ `circumference=0` -> `is_subgraph_free_C10=1`
+ `circumference=3` -> `is_subgraph_free_C10=1`
+ `circumference=4` -> `is_subgraph_free_C10=1`
+ `girth=0` -> `is_subgraph_free_C10=1`
+ `girth=3` -> `is_subgraph_free_C10=1`
+ `girth=4` -> `is_subgraph_free_C10=1`
+ `is_k_regular=0` -> `is_subgraph_free_C10=1`
+ `is_k_regular=2` -> `is_subgraph_free_C10=1`
+ `is_strongly_regular=0` -> `is_subgraph_free_C10=1`
+ `is_strongly_regular=1` -> `is_subgraph_free_C10=1`
+ `radius=1` -> `is_subgraph_free_C10=1`
+ `radius=2` -> `is_subgraph_free_C10=1`
+ `is_eulerian=0` -> `is_subgraph_free_C10=1`
+ `is_eulerian=1` -> `is_subgraph_free_C10=1`
+ `is_distance_regular=0` -> `is_subgraph_free_C10=1`
+ `is_distance_regular=1` -> `is_subgraph_free_C10=1`
+ `is_planar=1` -> `is_subgraph_free_C10=1`
+ `is_bipartite=0` -> `is_subgraph_free_C10=1`
+ `is_bipartite=1` -> `is_subgraph_free_C10=1`
+ `n_articulation_points=0` -> `is_subgraph_free_C10=1`
+ `n_articulation_points=1` -> `is_subgraph_free_C10=1`
+ `n_articulation_points=2` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_K3=0` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_K4=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_K5=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_C4=0` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_C4=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_C5=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_C6=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_C7=1` -> `is_subgraph_free_C10=1`
+ `is_integral=0` -> `is_subgraph_free_C10=1`
+ `is_integral=1` -> `is_subgraph_free_C10=1`
+ `vertex_connectivity>1` -> `is_subgraph_free_C10=1`
+ `vertex_connectivity>2` -> `is_subgraph_free_C10=1`
+ `edge_connectivity=1` -> `is_subgraph_free_C10=1`
+ `edge_connectivity=2` -> `is_subgraph_free_C10=1`
+ `edge_connectivity=3` -> `is_subgraph_free_C10=1`
+ `is_tree=0` -> `is_subgraph_free_C10=1`
+ `is_tree=1` -> `is_subgraph_free_C10=1`
+ `is_chordal=0` -> `is_subgraph_free_C10=1`
+ `is_chordal=1` -> `is_subgraph_free_C10=1`
+ `k_max_clique=2` -> `is_subgraph_free_C10=1`
+ `k_max_clique=3` -> `is_subgraph_free_C10=1`
+ `k_max_clique=4` -> `is_subgraph_free_C10=1`
+ `is_distinct_spectrum=0` -> `is_subgraph_free_C10=1`
+ `is_distinct_spectrum=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_bull=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_bowtie=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_diamond=0` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_diamond=1` -> `is_subgraph_free_C10=1`
+ `is_subgraph_free_open_bowtie=1` -> `is_subgraph_free_C10=1`
+ `is_hamiltonian=0` -> `is_subgraph_free_C10=1`
+ `is_hamiltonian=1` -> `is_subgraph_free_C10=1`
+ `has_fractional_duality_gap_vertex_chromatic=0` -> `is_subgraph_free_C10=1`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `is_subgraph_free_C10=1`
+ `maximal_independent_vertex_set=1` -> `is_subgraph_free_C10=1`
+ `maximal_independent_vertex_set=2` -> `is_subgraph_free_C10=1`
+ `maximal_independent_vertex_set=3` -> `is_subgraph_free_C10=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C10=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C10=1`
+ `automorphism_group_n=2` -> `is_integral=0`
+ `is_distinct_spectrum=1` -> `is_integral=0`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `is_integral=0`
+ `diameter=1` -> `is_integral=1`
+ `maximal_independent_vertex_set=1` -> `is_integral=1`
+ `automorphism_group_n=2` -> `vertex_connectivity>0`
+ `automorphism_group_n=4` -> `vertex_connectivity>0`
+ `automorphism_group_n=6` -> `vertex_connectivity>0`
+ `automorphism_group_n=8` -> `vertex_connectivity>0`
+ `automorphism_group_n=24` -> `vertex_connectivity>0`
+ `chromatic_number=2` -> `vertex_connectivity>0`
+ `chromatic_number=3` -> `vertex_connectivity>0`
+ `chromatic_number=4` -> `vertex_connectivity>0`
+ `diameter=1` -> `vertex_connectivity>0`
+ `diameter=2` -> `vertex_connectivity>0`
+ `diameter=3` -> `vertex_connectivity>0`
+ `circumference=0` -> `vertex_connectivity>0`
+ `circumference=3` -> `vertex_connectivity>0`
+ `circumference=4` -> `vertex_connectivity>0`
+ `girth=0` -> `vertex_connectivity>0`
+ `girth=3` -> `vertex_connectivity>0`
+ `girth=4` -> `vertex_connectivity>0`
+ `is_k_regular=0` -> `vertex_connectivity>0`
+ `is_k_regular=2` -> `vertex_connectivity>0`
+ `is_strongly_regular=0` -> `vertex_connectivity>0`
+ `is_strongly_regular=1` -> `vertex_connectivity>0`
+ `radius=1` -> `vertex_connectivity>0`
+ `radius=2` -> `vertex_connectivity>0`
+ `is_eulerian=0` -> `vertex_connectivity>0`
+ `is_eulerian=1` -> `vertex_connectivity>0`
+ `is_distance_regular=0` -> `vertex_connectivity>0`
+ `is_distance_regular=1` -> `vertex_connectivity>0`
+ `is_planar=1` -> `vertex_connectivity>0`
+ `is_bipartite=0` -> `vertex_connectivity>0`
+ `is_bipartite=1` -> `vertex_connectivity>0`
+ `n_articulation_points=0` -> `vertex_connectivity>0`
+ `n_articulation_points=1` -> `vertex_connectivity>0`
+ `n_articulation_points=2` -> `vertex_connectivity>0`
+ `is_subgraph_free_K3=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_K3=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_K4=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_K4=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_K5=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C4=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_C4=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C5=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C6=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C7=1` -> `vertex_connectivity>0`
+ `is_integral=0` -> `vertex_connectivity>0`
+ `is_integral=1` -> `vertex_connectivity>0`
+ `edge_connectivity=1` -> `vertex_connectivity>0`
+ `edge_connectivity=2` -> `vertex_connectivity>0`
+ `edge_connectivity=3` -> `vertex_connectivity>0`
+ `is_tree=0` -> `vertex_connectivity>0`
+ `is_tree=1` -> `vertex_connectivity>0`
+ `is_chordal=0` -> `vertex_connectivity>0`
+ `is_chordal=1` -> `vertex_connectivity>0`
+ `k_max_clique=2` -> `vertex_connectivity>0`
+ `k_max_clique=3` -> `vertex_connectivity>0`
+ `k_max_clique=4` -> `vertex_connectivity>0`
+ `is_distinct_spectrum=0` -> `vertex_connectivity>0`
+ `is_distinct_spectrum=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_bull=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_bowtie=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_diamond=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_diamond=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_open_bowtie=1` -> `vertex_connectivity>0`
+ `is_hamiltonian=0` -> `vertex_connectivity>0`
+ `is_hamiltonian=1` -> `vertex_connectivity>0`
+ `has_fractional_duality_gap_vertex_chromatic=0` -> `vertex_connectivity>0`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=1` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=2` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=3` -> `vertex_connectivity>0`
+ `maximal_independent_edge_set=1` -> `vertex_connectivity>0`
+ `maximal_independent_edge_set=2` -> `vertex_connectivity>0`
+ `diameter=1` -> `vertex_connectivity>1`
+ `is_k_regular=2` -> `vertex_connectivity>1`
+ `is_strongly_regular=1` -> `vertex_connectivity>1`
+ `is_distance_regular=1` -> `vertex_connectivity>1`
+ `is_hamiltonian=1` -> `vertex_connectivity>1`
+ `maximal_independent_vertex_set=1` -> `vertex_connectivity>1`
+ `is_k_regular=2` -> `edge_connectivity=2`
+ `automorphism_group_n=4` -> `is_tree=0`
+ `chromatic_number=3` -> `is_tree=0`
+ `chromatic_number=4` -> `is_tree=0`
+ `diameter=1` -> `is_tree=0`
+ `circumference=3` -> `is_tree=0`
+ `circumference=4` -> `is_tree=0`
+ `girth=3` -> `is_tree=0`
+ `girth=4` -> `is_tree=0`
+ `is_k_regular=2` -> `is_tree=0`
+ `is_strongly_regular=1` -> `is_tree=0`
+ `is_eulerian=1` -> `is_tree=0`
+ `is_distance_regular=1` -> `is_tree=0`
+ `is_subgraph_free_K4=0` -> `is_tree=0`
+ `vertex_connectivity>2` -> `is_tree=0`
+ `edge_connectivity=3` -> `is_tree=0`
+ `k_max_clique=4` -> `is_tree=0`
+ `is_hamiltonian=1` -> `is_tree=0`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `is_tree=0`
+ `maximal_independent_vertex_set=1` -> `is_tree=0`
+ `diameter=1` -> `is_chordal=1`
+ `maximal_independent_vertex_set=1` -> `is_chordal=1`
+ `maximal_independent_edge_set=1` -> `is_chordal=1`
+ `is_bipartite=1` -> `k_max_clique=2`
+ `automorphism_group_n=6` -> `is_distinct_spectrum=0`
+ `automorphism_group_n=8` -> `is_distinct_spectrum=0`
+ `automorphism_group_n=24` -> `is_distinct_spectrum=0`
+ `diameter=1` -> `is_distinct_spectrum=0`
+ `is_strongly_regular=1` -> `is_distinct_spectrum=0`
+ `is_distance_regular=1` -> `is_distinct_spectrum=0`
+ `is_integral=1` -> `is_distinct_spectrum=0`
+ `maximal_independent_vertex_set=1` -> `is_distinct_spectrum=0`
+ `is_bipartite=1` -> `is_subgraph_free_bull=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_bull=1`
+ `k_max_clique=2` -> `is_subgraph_free_bull=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_bull=1`
+ `is_bipartite=1` -> `is_subgraph_free_bowtie=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_bowtie=1`
+ `k_max_clique=2` -> `is_subgraph_free_bowtie=1`
+ `is_subgraph_free_open_bowtie=1` -> `is_subgraph_free_bowtie=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_bowtie=1`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_diamond=0`
+ `k_max_clique=4` -> `is_subgraph_free_diamond=0`
+ `is_bipartite=1` -> `is_subgraph_free_diamond=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_diamond=1`
+ `is_subgraph_free_C4=1` -> `is_subgraph_free_diamond=1`
+ `k_max_clique=2` -> `is_subgraph_free_diamond=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_diamond=1`
+ `is_bipartite=1` -> `is_subgraph_free_open_bowtie=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_open_bowtie=1`
+ `k_max_clique=2` -> `is_subgraph_free_open_bowtie=1`
+ `circumference=0` -> `is_hamiltonian=0`
+ `girth=0` -> `is_hamiltonian=0`
+ `n_articulation_points=1` -> `is_hamiltonian=0`
+ `n_articulation_points=2` -> `is_hamiltonian=0`
+ `edge_connectivity=1` -> `is_hamiltonian=0`
+ `is_tree=1` -> `is_hamiltonian=0`
+ `diameter=1` -> `is_hamiltonian=1`
+ `is_strongly_regular=1` -> `is_hamiltonian=1`
+ `is_distance_regular=1` -> `is_hamiltonian=1`
+ `maximal_independent_vertex_set=1` -> `is_hamiltonian=1`
+ `automorphism_group_n=6` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `automorphism_group_n=24` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `chromatic_number=2` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `diameter=1` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `circumference=0` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `circumference=3` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `circumference=4` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `girth=0` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `is_integral=1` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `is_tree=1` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `maximal_independent_vertex_set=1` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `maximal_independent_edge_set=1` -> `has_fractional_duality_gap_vertex_chromatic=0`

# Exclusive relations
+ `automorphism_group_n=2` intersect `diameter=1` = 0
+ `automorphism_group_n=2` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=2` intersect `is_distance_regular=1` = 0
+ `automorphism_group_n=2` intersect `is_integral=1` = 0
+ `automorphism_group_n=2` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=4` intersect `diameter=1` = 0
+ `automorphism_group_n=4` intersect `circumference=0` = 0
+ `automorphism_group_n=4` intersect `girth=0` = 0
+ `automorphism_group_n=4` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=4` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=4` intersect `is_distance_regular=1` = 0
+ `automorphism_group_n=4` intersect `is_tree=1` = 0
+ `automorphism_group_n=4` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=4` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=6` intersect `is_distinct_spectrum=1` = 0
+ `automorphism_group_n=6` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `automorphism_group_n=8` intersect `diameter=1` = 0
+ `automorphism_group_n=8` intersect `is_distinct_spectrum=1` = 0
+ `automorphism_group_n=8` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=8` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=24` intersect `circumference=3` = 0
+ `automorphism_group_n=24` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=24` intersect `is_distinct_spectrum=1` = 0
+ `automorphism_group_n=24` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `chromatic_number=2` intersect `diameter=1` = 0
+ `chromatic_number=2` intersect `circumference=3` = 0
+ `chromatic_number=2` intersect `girth=3` = 0
+ `chromatic_number=2` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `chromatic_number=2` intersect `maximal_independent_vertex_set=1` = 0
+ `chromatic_number=3` intersect `circumference=0` = 0
+ `chromatic_number=3` intersect `girth=0` = 0
+ `chromatic_number=3` intersect `is_tree=1` = 0
+ `chromatic_number=4` intersect `circumference=0` = 0
+ `chromatic_number=4` intersect `circumference=3` = 0
+ `chromatic_number=4` intersect `girth=0` = 0
+ `chromatic_number=4` intersect `girth=4` = 0
+ `chromatic_number=4` intersect `is_k_regular=2` = 0
+ `chromatic_number=4` intersect `is_tree=1` = 0
+ `chromatic_number=4` intersect `maximal_independent_edge_set=1` = 0
+ `diameter=1` intersect `automorphism_group_n=2` = 0
+ `diameter=1` intersect `automorphism_group_n=4` = 0
+ `diameter=1` intersect `automorphism_group_n=8` = 0
+ `diameter=1` intersect `chromatic_number=2` = 0
+ `diameter=1` intersect `circumference=0` = 0
+ `diameter=1` intersect `girth=0` = 0
+ `diameter=1` intersect `girth=4` = 0
+ `diameter=1` intersect `is_k_regular=0` = 0
+ `diameter=1` intersect `is_strongly_regular=0` = 0
+ `diameter=1` intersect `radius=2` = 0
+ `diameter=1` intersect `is_distance_regular=0` = 0
+ `diameter=1` intersect `is_bipartite=1` = 0
+ `diameter=1` intersect `n_articulation_points=1` = 0
+ `diameter=1` intersect `n_articulation_points=2` = 0
+ `diameter=1` intersect `is_subgraph_free_K3=1` = 0
+ `diameter=1` intersect `is_integral=0` = 0
+ `diameter=1` intersect `edge_connectivity=1` = 0
+ `diameter=1` intersect `is_tree=1` = 0
+ `diameter=1` intersect `is_chordal=0` = 0
+ `diameter=1` intersect `k_max_clique=2` = 0
+ `diameter=1` intersect `is_distinct_spectrum=1` = 0
+ `diameter=1` intersect `is_hamiltonian=0` = 0
+ `diameter=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `diameter=1` intersect `maximal_independent_vertex_set=2` = 0
+ `diameter=1` intersect `maximal_independent_vertex_set=3` = 0
+ `diameter=2` intersect `n_articulation_points=2` = 0
+ `diameter=2` intersect `maximal_independent_vertex_set=1` = 0
+ `diameter=3` intersect `is_strongly_regular=1` = 0
+ `diameter=3` intersect `radius=1` = 0
+ `diameter=3` intersect `vertex_connectivity>2` = 0
+ `diameter=3` intersect `edge_connectivity=3` = 0
+ `diameter=3` intersect `maximal_independent_vertex_set=1` = 0
+ `diameter=3` intersect `maximal_independent_edge_set=1` = 0
+ `circumference=0` intersect `automorphism_group_n=4` = 0
+ `circumference=0` intersect `chromatic_number=3` = 0
+ `circumference=0` intersect `chromatic_number=4` = 0
+ `circumference=0` intersect `diameter=1` = 0
+ `circumference=0` intersect `girth=3` = 0
+ `circumference=0` intersect `girth=4` = 0
+ `circumference=0` intersect `is_k_regular=2` = 0
+ `circumference=0` intersect `is_strongly_regular=1` = 0
+ `circumference=0` intersect `is_eulerian=1` = 0
+ `circumference=0` intersect `is_distance_regular=1` = 0
+ `circumference=0` intersect `is_subgraph_free_K4=0` = 0
+ `circumference=0` intersect `vertex_connectivity>2` = 0
+ `circumference=0` intersect `edge_connectivity=3` = 0
+ `circumference=0` intersect `is_tree=0` = 0
+ `circumference=0` intersect `k_max_clique=4` = 0
+ `circumference=0` intersect `is_hamiltonian=1` = 0
+ `circumference=0` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `circumference=0` intersect `maximal_independent_vertex_set=1` = 0
+ `circumference=3` intersect `automorphism_group_n=24` = 0
+ `circumference=3` intersect `chromatic_number=2` = 0
+ `circumference=3` intersect `chromatic_number=4` = 0
+ `circumference=3` intersect `girth=0` = 0
+ `circumference=3` intersect `girth=4` = 0
+ `circumference=3` intersect `vertex_connectivity>2` = 0
+ `circumference=3` intersect `edge_connectivity=3` = 0
+ `circumference=3` intersect `is_tree=1` = 0
+ `circumference=3` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `circumference=4` intersect `girth=0` = 0
+ `circumference=4` intersect `is_tree=1` = 0
+ `circumference=4` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `circumference=4` intersect `maximal_independent_edge_set=1` = 0
+ `girth=0` intersect `automorphism_group_n=4` = 0
+ `girth=0` intersect `chromatic_number=3` = 0
+ `girth=0` intersect `chromatic_number=4` = 0
+ `girth=0` intersect `diameter=1` = 0
+ `girth=0` intersect `circumference=3` = 0
+ `girth=0` intersect `circumference=4` = 0
+ `girth=0` intersect `is_k_regular=2` = 0
+ `girth=0` intersect `is_strongly_regular=1` = 0
+ `girth=0` intersect `is_eulerian=1` = 0
+ `girth=0` intersect `is_distance_regular=1` = 0
+ `girth=0` intersect `is_subgraph_free_K4=0` = 0
+ `girth=0` intersect `vertex_connectivity>2` = 0
+ `girth=0` intersect `edge_connectivity=3` = 0
+ `girth=0` intersect `is_tree=0` = 0
+ `girth=0` intersect `k_max_clique=4` = 0
+ `girth=0` intersect `is_hamiltonian=1` = 0
+ `girth=0` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `girth=0` intersect `maximal_independent_vertex_set=1` = 0
+ `girth=3` intersect `chromatic_number=2` = 0
+ `girth=3` intersect `circumference=0` = 0
+ `girth=3` intersect `is_tree=1` = 0
+ `girth=4` intersect `chromatic_number=4` = 0
+ `girth=4` intersect `diameter=1` = 0
+ `girth=4` intersect `circumference=0` = 0
+ `girth=4` intersect `circumference=3` = 0
+ `girth=4` intersect `is_tree=1` = 0
+ `girth=4` intersect `maximal_independent_vertex_set=1` = 0
+ `girth=4` intersect `maximal_independent_edge_set=1` = 0
+ `is_k_regular=0` intersect `diameter=1` = 0
+ `is_k_regular=0` intersect `is_strongly_regular=1` = 0
+ `is_k_regular=0` intersect `maximal_independent_vertex_set=1` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=4` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=24` = 0
+ `is_k_regular=2` intersect `chromatic_number=4` = 0
+ `is_k_regular=2` intersect `circumference=0` = 0
+ `is_k_regular=2` intersect `girth=0` = 0
+ `is_k_regular=2` intersect `n_articulation_points=1` = 0
+ `is_k_regular=2` intersect `n_articulation_points=2` = 0
+ `is_k_regular=2` intersect `vertex_connectivity>2` = 0
+ `is_k_regular=2` intersect `edge_connectivity=1` = 0
+ `is_k_regular=2` intersect `edge_connectivity=3` = 0
+ `is_k_regular=2` intersect `is_tree=1` = 0
+ `is_strongly_regular=0` intersect `diameter=1` = 0
+ `is_strongly_regular=0` intersect `maximal_independent_vertex_set=1` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=2` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=4` = 0
+ `is_strongly_regular=1` intersect `diameter=3` = 0
+ `is_strongly_regular=1` intersect `circumference=0` = 0
+ `is_strongly_regular=1` intersect `girth=0` = 0
+ `is_strongly_regular=1` intersect `is_k_regular=0` = 0
+ `is_strongly_regular=1` intersect `is_distance_regular=0` = 0
+ `is_strongly_regular=1` intersect `n_articulation_points=1` = 0
+ `is_strongly_regular=1` intersect `n_articulation_points=2` = 0
+ `is_strongly_regular=1` intersect `edge_connectivity=1` = 0
+ `is_strongly_regular=1` intersect `is_tree=1` = 0
+ `is_strongly_regular=1` intersect `is_distinct_spectrum=1` = 0
+ `is_strongly_regular=1` intersect `is_hamiltonian=0` = 0
+ `radius=1` intersect `diameter=3` = 0
+ `radius=1` intersect `n_articulation_points=2` = 0
+ `radius=2` intersect `diameter=1` = 0
+ `radius=2` intersect `maximal_independent_vertex_set=1` = 0
+ `radius=2` intersect `maximal_independent_edge_set=1` = 0
+ `is_eulerian=1` intersect `circumference=0` = 0
+ `is_eulerian=1` intersect `girth=0` = 0
+ `is_eulerian=1` intersect `edge_connectivity=1` = 0
+ `is_eulerian=1` intersect `edge_connectivity=3` = 0
+ `is_eulerian=1` intersect `is_tree=1` = 0
+ `is_distance_regular=0` intersect `diameter=1` = 0
+ `is_distance_regular=0` intersect `is_strongly_regular=1` = 0
+ `is_distance_regular=0` intersect `maximal_independent_vertex_set=1` = 0
+ `is_distance_regular=1` intersect `automorphism_group_n=2` = 0
+ `is_distance_regular=1` intersect `automorphism_group_n=4` = 0
+ `is_distance_regular=1` intersect `circumference=0` = 0
+ `is_distance_regular=1` intersect `girth=0` = 0
+ `is_distance_regular=1` intersect `n_articulation_points=1` = 0
+ `is_distance_regular=1` intersect `n_articulation_points=2` = 0
+ `is_distance_regular=1` intersect `edge_connectivity=1` = 0
+ `is_distance_regular=1` intersect `is_tree=1` = 0
+ `is_distance_regular=1` intersect `is_distinct_spectrum=1` = 0
+ `is_distance_regular=1` intersect `is_hamiltonian=0` = 0
+ `is_bipartite=1` intersect `diameter=1` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_K3=0` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_bipartite=1` intersect `k_max_clique=3` = 0
+ `is_bipartite=1` intersect `k_max_clique=4` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_diamond=0` = 0
+ `is_bipartite=1` intersect `maximal_independent_vertex_set=1` = 0
+ `n_articulation_points=0` intersect `edge_connectivity=1` = 0
+ `n_articulation_points=1` intersect `diameter=1` = 0
+ `n_articulation_points=1` intersect `is_k_regular=2` = 0
+ `n_articulation_points=1` intersect `is_strongly_regular=1` = 0
+ `n_articulation_points=1` intersect `is_distance_regular=1` = 0
+ `n_articulation_points=1` intersect `vertex_connectivity>1` = 0
+ `n_articulation_points=1` intersect `vertex_connectivity>2` = 0
+ `n_articulation_points=1` intersect `is_hamiltonian=1` = 0
+ `n_articulation_points=1` intersect `maximal_independent_vertex_set=1` = 0
+ `n_articulation_points=2` intersect `diameter=1` = 0
+ `n_articulation_points=2` intersect `diameter=2` = 0
+ `n_articulation_points=2` intersect `is_k_regular=2` = 0
+ `n_articulation_points=2` intersect `is_strongly_regular=1` = 0
+ `n_articulation_points=2` intersect `radius=1` = 0
+ `n_articulation_points=2` intersect `is_distance_regular=1` = 0
+ `n_articulation_points=2` intersect `vertex_connectivity>1` = 0
+ `n_articulation_points=2` intersect `vertex_connectivity>2` = 0
+ `n_articulation_points=2` intersect `edge_connectivity=3` = 0
+ `n_articulation_points=2` intersect `is_hamiltonian=1` = 0
+ `n_articulation_points=2` intersect `maximal_independent_vertex_set=1` = 0
+ `n_articulation_points=2` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_K3=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_K3=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_K3=1` intersect `diameter=1` = 0
+ `is_subgraph_free_K3=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_subgraph_free_K3=1` intersect `k_max_clique=3` = 0
+ `is_subgraph_free_K3=1` intersect `k_max_clique=4` = 0
+ `is_subgraph_free_K3=1` intersect `is_subgraph_free_diamond=0` = 0
+ `is_subgraph_free_K3=1` intersect `maximal_independent_vertex_set=1` = 0
+ `is_subgraph_free_K4=0` intersect `circumference=0` = 0
+ `is_subgraph_free_K4=0` intersect `girth=0` = 0
+ `is_subgraph_free_K4=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_K4=0` intersect `is_subgraph_free_K3=1` = 0
+ `is_subgraph_free_K4=0` intersect `is_subgraph_free_C4=1` = 0
+ `is_subgraph_free_K4=0` intersect `is_tree=1` = 0
+ `is_subgraph_free_K4=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_K4=0` intersect `k_max_clique=3` = 0
+ `is_subgraph_free_K4=0` intersect `is_subgraph_free_diamond=1` = 0
+ `is_subgraph_free_K4=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_K4=1` intersect `k_max_clique=4` = 0
+ `is_subgraph_free_C4=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_C4=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_subgraph_free_C4=1` intersect `vertex_connectivity>2` = 0
+ `is_subgraph_free_C4=1` intersect `edge_connectivity=3` = 0
+ `is_subgraph_free_C4=1` intersect `k_max_clique=4` = 0
+ `is_subgraph_free_C4=1` intersect `is_subgraph_free_diamond=0` = 0
+ `is_integral=0` intersect `diameter=1` = 0
+ `is_integral=0` intersect `maximal_independent_vertex_set=1` = 0
+ `is_integral=1` intersect `automorphism_group_n=2` = 0
+ `is_integral=1` intersect `is_distinct_spectrum=1` = 0
+ `is_integral=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `vertex_connectivity>1` intersect `n_articulation_points=1` = 0
+ `vertex_connectivity>1` intersect `n_articulation_points=2` = 0
+ `vertex_connectivity>1` intersect `edge_connectivity=1` = 0
+ `vertex_connectivity>2` intersect `diameter=3` = 0
+ `vertex_connectivity>2` intersect `circumference=0` = 0
+ `vertex_connectivity>2` intersect `circumference=3` = 0
+ `vertex_connectivity>2` intersect `girth=0` = 0
+ `vertex_connectivity>2` intersect `is_k_regular=2` = 0
+ `vertex_connectivity>2` intersect `n_articulation_points=1` = 0
+ `vertex_connectivity>2` intersect `n_articulation_points=2` = 0
+ `vertex_connectivity>2` intersect `is_subgraph_free_C4=1` = 0
+ `vertex_connectivity>2` intersect `edge_connectivity=1` = 0
+ `vertex_connectivity>2` intersect `edge_connectivity=2` = 0
+ `vertex_connectivity>2` intersect `is_tree=1` = 0
+ `vertex_connectivity>2` intersect `maximal_independent_edge_set=1` = 0
+ `edge_connectivity=1` intersect `diameter=1` = 0
+ `edge_connectivity=1` intersect `is_k_regular=2` = 0
+ `edge_connectivity=1` intersect `is_strongly_regular=1` = 0
+ `edge_connectivity=1` intersect `is_eulerian=1` = 0
+ `edge_connectivity=1` intersect `is_distance_regular=1` = 0
+ `edge_connectivity=1` intersect `n_articulation_points=0` = 0
+ `edge_connectivity=1` intersect `vertex_connectivity>1` = 0
+ `edge_connectivity=1` intersect `vertex_connectivity>2` = 0
+ `edge_connectivity=1` intersect `is_hamiltonian=1` = 0
+ `edge_connectivity=1` intersect `maximal_independent_vertex_set=1` = 0
+ `edge_connectivity=2` intersect `vertex_connectivity>2` = 0
+ `edge_connectivity=3` intersect `diameter=3` = 0
+ `edge_connectivity=3` intersect `circumference=0` = 0
+ `edge_connectivity=3` intersect `circumference=3` = 0
+ `edge_connectivity=3` intersect `girth=0` = 0
+ `edge_connectivity=3` intersect `is_k_regular=2` = 0
+ `edge_connectivity=3` intersect `is_eulerian=1` = 0
+ `edge_connectivity=3` intersect `n_articulation_points=2` = 0
+ `edge_connectivity=3` intersect `is_subgraph_free_C4=1` = 0
+ `edge_connectivity=3` intersect `is_tree=1` = 0
+ `edge_connectivity=3` intersect `maximal_independent_edge_set=1` = 0
+ `is_tree=0` intersect `circumference=0` = 0
+ `is_tree=0` intersect `girth=0` = 0
+ `is_tree=1` intersect `automorphism_group_n=4` = 0
+ `is_tree=1` intersect `chromatic_number=3` = 0
+ `is_tree=1` intersect `chromatic_number=4` = 0
+ `is_tree=1` intersect `diameter=1` = 0
+ `is_tree=1` intersect `circumference=3` = 0
+ `is_tree=1` intersect `circumference=4` = 0
+ `is_tree=1` intersect `girth=3` = 0
+ `is_tree=1` intersect `girth=4` = 0
+ `is_tree=1` intersect `is_k_regular=2` = 0
+ `is_tree=1` intersect `is_strongly_regular=1` = 0
+ `is_tree=1` intersect `is_eulerian=1` = 0
+ `is_tree=1` intersect `is_distance_regular=1` = 0
+ `is_tree=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_tree=1` intersect `vertex_connectivity>2` = 0
+ `is_tree=1` intersect `edge_connectivity=3` = 0
+ `is_tree=1` intersect `k_max_clique=4` = 0
+ `is_tree=1` intersect `is_hamiltonian=1` = 0
+ `is_tree=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `is_tree=1` intersect `maximal_independent_vertex_set=1` = 0
+ `is_chordal=0` intersect `diameter=1` = 0
+ `is_chordal=0` intersect `maximal_independent_vertex_set=1` = 0
+ `is_chordal=0` intersect `maximal_independent_edge_set=1` = 0
+ `k_max_clique=2` intersect `diameter=1` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_K3=0` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_K4=0` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_diamond=0` = 0
+ `k_max_clique=2` intersect `maximal_independent_vertex_set=1` = 0
+ `k_max_clique=3` intersect `is_bipartite=1` = 0
+ `k_max_clique=3` intersect `is_subgraph_free_K3=1` = 0
+ `k_max_clique=3` intersect `is_subgraph_free_K4=0` = 0
+ `k_max_clique=4` intersect `circumference=0` = 0
+ `k_max_clique=4` intersect `girth=0` = 0
+ `k_max_clique=4` intersect `is_bipartite=1` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_K3=1` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_K4=1` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_C4=1` = 0
+ `k_max_clique=4` intersect `is_tree=1` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_diamond=1` = 0
+ `k_max_clique=4` intersect `maximal_independent_edge_set=1` = 0
+ `is_distinct_spectrum=1` intersect `automorphism_group_n=6` = 0
+ `is_distinct_spectrum=1` intersect `automorphism_group_n=8` = 0
+ `is_distinct_spectrum=1` intersect `automorphism_group_n=24` = 0
+ `is_distinct_spectrum=1` intersect `diameter=1` = 0
+ `is_distinct_spectrum=1` intersect `is_strongly_regular=1` = 0
+ `is_distinct_spectrum=1` intersect `is_distance_regular=1` = 0
+ `is_distinct_spectrum=1` intersect `is_integral=1` = 0
+ `is_distinct_spectrum=1` intersect `maximal_independent_vertex_set=1` = 0
+ `is_subgraph_free_diamond=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_diamond=0` intersect `is_subgraph_free_K3=1` = 0
+ `is_subgraph_free_diamond=0` intersect `is_subgraph_free_C4=1` = 0
+ `is_subgraph_free_diamond=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_diamond=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_diamond=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_subgraph_free_diamond=1` intersect `k_max_clique=4` = 0
+ `is_hamiltonian=0` intersect `diameter=1` = 0
+ `is_hamiltonian=0` intersect `is_strongly_regular=1` = 0
+ `is_hamiltonian=0` intersect `is_distance_regular=1` = 0
+ `is_hamiltonian=0` intersect `maximal_independent_vertex_set=1` = 0
+ `is_hamiltonian=1` intersect `circumference=0` = 0
+ `is_hamiltonian=1` intersect `girth=0` = 0
+ `is_hamiltonian=1` intersect `n_articulation_points=1` = 0
+ `is_hamiltonian=1` intersect `n_articulation_points=2` = 0
+ `is_hamiltonian=1` intersect `edge_connectivity=1` = 0
+ `is_hamiltonian=1` intersect `is_tree=1` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `automorphism_group_n=6` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `automorphism_group_n=24` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `chromatic_number=2` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `diameter=1` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `circumference=0` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `circumference=3` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `circumference=4` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `girth=0` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `is_integral=1` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `is_tree=1` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `maximal_independent_vertex_set=1` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `maximal_independent_edge_set=1` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=2` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=4` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=8` = 0
+ `maximal_independent_vertex_set=1` intersect `chromatic_number=2` = 0
+ `maximal_independent_vertex_set=1` intersect `diameter=2` = 0
+ `maximal_independent_vertex_set=1` intersect `diameter=3` = 0
+ `maximal_independent_vertex_set=1` intersect `circumference=0` = 0
+ `maximal_independent_vertex_set=1` intersect `girth=0` = 0
+ `maximal_independent_vertex_set=1` intersect `girth=4` = 0
+ `maximal_independent_vertex_set=1` intersect `is_k_regular=0` = 0
+ `maximal_independent_vertex_set=1` intersect `is_strongly_regular=0` = 0
+ `maximal_independent_vertex_set=1` intersect `radius=2` = 0
+ `maximal_independent_vertex_set=1` intersect `is_distance_regular=0` = 0
+ `maximal_independent_vertex_set=1` intersect `is_bipartite=1` = 0
+ `maximal_independent_vertex_set=1` intersect `n_articulation_points=1` = 0
+ `maximal_independent_vertex_set=1` intersect `n_articulation_points=2` = 0
+ `maximal_independent_vertex_set=1` intersect `is_subgraph_free_K3=1` = 0
+ `maximal_independent_vertex_set=1` intersect `is_integral=0` = 0
+ `maximal_independent_vertex_set=1` intersect `edge_connectivity=1` = 0
+ `maximal_independent_vertex_set=1` intersect `is_tree=1` = 0
+ `maximal_independent_vertex_set=1` intersect `is_chordal=0` = 0
+ `maximal_independent_vertex_set=1` intersect `k_max_clique=2` = 0
+ `maximal_independent_vertex_set=1` intersect `is_distinct_spectrum=1` = 0
+ `maximal_independent_vertex_set=1` intersect `is_hamiltonian=0` = 0
+ `maximal_independent_vertex_set=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `maximal_independent_vertex_set=2` intersect `diameter=1` = 0
+ `maximal_independent_vertex_set=3` intersect `diameter=1` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=4` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=8` = 0
+ `maximal_independent_edge_set=1` intersect `chromatic_number=4` = 0
+ `maximal_independent_edge_set=1` intersect `diameter=3` = 0
+ `maximal_independent_edge_set=1` intersect `circumference=4` = 0
+ `maximal_independent_edge_set=1` intersect `girth=4` = 0
+ `maximal_independent_edge_set=1` intersect `radius=2` = 0
+ `maximal_independent_edge_set=1` intersect `n_articulation_points=2` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_K4=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_C4=0` = 0
+ `maximal_independent_edge_set=1` intersect `vertex_connectivity>2` = 0
+ `maximal_independent_edge_set=1` intersect `edge_connectivity=3` = 0
+ `maximal_independent_edge_set=1` intersect `is_chordal=0` = 0
+ `maximal_independent_edge_set=1` intersect `k_max_clique=4` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_diamond=0` = 0
+ `maximal_independent_edge_set=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
