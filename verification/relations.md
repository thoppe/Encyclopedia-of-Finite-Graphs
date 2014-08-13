# Equality relations (converse holds)
+ `circumference=0` <-> `girth=0`
+ `circumference=0` <-> `is_tree=1`
+ `girth=0` <-> `circumference=0`
+ `girth=0` <-> `is_tree=1`
+ `n_articulation_points=0` <-> `vertex_connectivity>1`
+ `is_subgraph_free_K3=1` <-> `k_max_clique=2`
+ `vertex_connectivity>1` <-> `n_articulation_points=0`
+ `is_tree=1` <-> `circumference=0`
+ `is_tree=1` <-> `girth=0`
+ `k_max_clique=2` <-> `is_subgraph_free_K3=1`

# Subset relations (converse is not true)
+ `circumference=0` -> `chromatic_number=2`
+ `girth=0` -> `chromatic_number=2`
+ `is_tree=1` -> `chromatic_number=2`
+ `circumference=3` -> `chromatic_number=3`
+ `girth=5` -> `chromatic_number=3`
+ `girth=7` -> `chromatic_number=3`
+ `chromatic_number=5` -> `girth=3`
+ `chromatic_number=6` -> `girth=3`
+ `chromatic_number=7` -> `girth=3`
+ `circumference=3` -> `girth=3`
+ `is_k_regular=6` -> `girth=3`
+ `is_subgraph_free_K5=0` -> `girth=3`
+ `vertex_connectivity>5` -> `girth=3`
+ `edge_connectivity=6` -> `girth=3`
+ `k_max_clique=5` -> `girth=3`
+ `k_max_clique=6` -> `girth=3`
+ `k_max_clique=7` -> `girth=3`
+ `maximal_independent_vertex_set=1` -> `girth=3`
+ `automorphism_group_n=14` -> `is_k_regular=0`
+ `automorphism_group_n=24` -> `is_k_regular=0`
+ `automorphism_group_n=36` -> `is_k_regular=0`
+ `diameter=6` -> `is_k_regular=0`
+ `circumference=0` -> `is_k_regular=0`
+ `girth=0` -> `is_k_regular=0`
+ `n_articulation_points=3` -> `is_k_regular=0`
+ `n_articulation_points=4` -> `is_k_regular=0`
+ `n_articulation_points=5` -> `is_k_regular=0`
+ `is_tree=1` -> `is_k_regular=0`
+ `maximal_independent_vertex_set=6` -> `is_k_regular=0`
+ `automorphism_group_n=1` -> `is_strongly_regular=0`
+ `automorphism_group_n=2` -> `is_strongly_regular=0`
+ `automorphism_group_n=4` -> `is_strongly_regular=0`
+ `automorphism_group_n=12` -> `is_strongly_regular=0`
+ `automorphism_group_n=14` -> `is_strongly_regular=0`
+ `automorphism_group_n=16` -> `is_strongly_regular=0`
+ `automorphism_group_n=20` -> `is_strongly_regular=0`
+ `automorphism_group_n=36` -> `is_strongly_regular=0`
+ `automorphism_group_n=144` -> `is_strongly_regular=0`
+ `automorphism_group_n=240` -> `is_strongly_regular=0`
+ `diameter=3` -> `is_strongly_regular=0`
+ `diameter=4` -> `is_strongly_regular=0`
+ `diameter=5` -> `is_strongly_regular=0`
+ `diameter=6` -> `is_strongly_regular=0`
+ `girth=6` -> `is_strongly_regular=0`
+ `girth=7` -> `is_strongly_regular=0`
+ `radius=3` -> `is_strongly_regular=0`
+ `is_distance_regular=0` -> `is_strongly_regular=0`
+ `n_articulation_points=1` -> `is_strongly_regular=0`
+ `n_articulation_points=2` -> `is_strongly_regular=0`
+ `n_articulation_points=3` -> `is_strongly_regular=0`
+ `n_articulation_points=4` -> `is_strongly_regular=0`
+ `n_articulation_points=5` -> `is_strongly_regular=0`
+ `edge_connectivity=1` -> `is_strongly_regular=0`
+ `is_real_spectrum=1` -> `is_strongly_regular=0`
+ `maximal_independent_vertex_set=6` -> `is_strongly_regular=0`
+ `diameter=1` -> `is_strongly_regular=1`
+ `diameter=1` -> `radius=1`
+ `circumference=0` -> `is_eulerian=0`
+ `girth=0` -> `is_eulerian=0`
+ `girth=7` -> `is_eulerian=0`
+ `is_k_regular=3` -> `is_eulerian=0`
+ `n_articulation_points=4` -> `is_eulerian=0`
+ `n_articulation_points=5` -> `is_eulerian=0`
+ `edge_connectivity=1` -> `is_eulerian=0`
+ `edge_connectivity=3` -> `is_eulerian=0`
+ `edge_connectivity=5` -> `is_eulerian=0`
+ `is_tree=1` -> `is_eulerian=0`
+ `is_k_regular=4` -> `is_eulerian=1`
+ `is_k_regular=6` -> `is_eulerian=1`
+ `automorphism_group_n=1` -> `is_distance_regular=0`
+ `automorphism_group_n=2` -> `is_distance_regular=0`
+ `automorphism_group_n=4` -> `is_distance_regular=0`
+ `automorphism_group_n=36` -> `is_distance_regular=0`
+ `automorphism_group_n=144` -> `is_distance_regular=0`
+ `diameter=6` -> `is_distance_regular=0`
+ `girth=7` -> `is_distance_regular=0`
+ `n_articulation_points=1` -> `is_distance_regular=0`
+ `n_articulation_points=2` -> `is_distance_regular=0`
+ `n_articulation_points=3` -> `is_distance_regular=0`
+ `n_articulation_points=4` -> `is_distance_regular=0`
+ `n_articulation_points=5` -> `is_distance_regular=0`
+ `edge_connectivity=1` -> `is_distance_regular=0`
+ `is_real_spectrum=1` -> `is_distance_regular=0`
+ `maximal_independent_vertex_set=6` -> `is_distance_regular=0`
+ `diameter=1` -> `is_distance_regular=1`
+ `is_strongly_regular=1` -> `is_distance_regular=1`
+ `chromatic_number=6` -> `is_planar=0`
+ `chromatic_number=7` -> `is_planar=0`
+ `is_k_regular=6` -> `is_planar=0`
+ `is_subgraph_free_K5=0` -> `is_planar=0`
+ `vertex_connectivity>4` -> `is_planar=0`
+ `vertex_connectivity>5` -> `is_planar=0`
+ `edge_connectivity=5` -> `is_planar=0`
+ `edge_connectivity=6` -> `is_planar=0`
+ `k_max_clique=5` -> `is_planar=0`
+ `k_max_clique=6` -> `is_planar=0`
+ `k_max_clique=7` -> `is_planar=0`
+ `circumference=3` -> `is_planar=1`
+ `circumference=4` -> `is_planar=1`
+ `girth=7` -> `is_planar=1`
+ `is_k_regular=2` -> `is_planar=1`
+ `maximal_independent_edge_set=1` -> `is_planar=1`
+ `automorphism_group_n=10` -> `is_bipartite=0`
+ `automorphism_group_n=14` -> `is_bipartite=0`
+ `chromatic_number=5` -> `is_bipartite=0`
+ `chromatic_number=6` -> `is_bipartite=0`
+ `chromatic_number=7` -> `is_bipartite=0`
+ `diameter=1` -> `is_bipartite=0`
+ `is_k_regular=6` -> `is_bipartite=0`
+ `is_subgraph_free_K3=0` -> `is_bipartite=0`
+ `is_subgraph_free_K4=0` -> `is_bipartite=0`
+ `is_subgraph_free_K5=0` -> `is_bipartite=0`
+ `is_subgraph_free_C5=0` -> `is_bipartite=0`
+ `is_subgraph_free_C7=0` -> `is_bipartite=0`
+ `vertex_connectivity>5` -> `is_bipartite=0`
+ `edge_connectivity=6` -> `is_bipartite=0`
+ `k_max_clique=3` -> `is_bipartite=0`
+ `k_max_clique=4` -> `is_bipartite=0`
+ `k_max_clique=5` -> `is_bipartite=0`
+ `k_max_clique=6` -> `is_bipartite=0`
+ `k_max_clique=7` -> `is_bipartite=0`
+ `is_subgraph_free_bull=0` -> `is_bipartite=0`
+ `is_subgraph_free_bowtie=0` -> `is_bipartite=0`
+ `is_subgraph_free_diamond=0` -> `is_bipartite=0`
+ `is_subgraph_free_open_bowtie=0` -> `is_bipartite=0`
+ `diameter=1` -> `n_articulation_points=0`
+ `is_k_regular=4` -> `n_articulation_points=0`
+ `is_k_regular=6` -> `n_articulation_points=0`
+ `is_strongly_regular=1` -> `n_articulation_points=0`
+ `is_distance_regular=1` -> `n_articulation_points=0`
+ `vertex_connectivity>2` -> `n_articulation_points=0`
+ `vertex_connectivity>3` -> `n_articulation_points=0`
+ `vertex_connectivity>4` -> `n_articulation_points=0`
+ `vertex_connectivity>5` -> `n_articulation_points=0`
+ `edge_connectivity=5` -> `n_articulation_points=0`
+ `edge_connectivity=6` -> `n_articulation_points=0`
+ `is_hamiltonian=1` -> `n_articulation_points=0`
+ `chromatic_number=5` -> `is_subgraph_free_K3=0`
+ `chromatic_number=6` -> `is_subgraph_free_K3=0`
+ `chromatic_number=7` -> `is_subgraph_free_K3=0`
+ `diameter=1` -> `is_subgraph_free_K3=0`
+ `is_k_regular=6` -> `is_subgraph_free_K3=0`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_K3=0`
+ `is_subgraph_free_K5=0` -> `is_subgraph_free_K3=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_K3=0`
+ `edge_connectivity=6` -> `is_subgraph_free_K3=0`
+ `k_max_clique=3` -> `is_subgraph_free_K3=0`
+ `k_max_clique=4` -> `is_subgraph_free_K3=0`
+ `k_max_clique=5` -> `is_subgraph_free_K3=0`
+ `k_max_clique=6` -> `is_subgraph_free_K3=0`
+ `k_max_clique=7` -> `is_subgraph_free_K3=0`
+ `is_subgraph_free_bull=0` -> `is_subgraph_free_K3=0`
+ `is_subgraph_free_bowtie=0` -> `is_subgraph_free_K3=0`
+ `is_subgraph_free_diamond=0` -> `is_subgraph_free_K3=0`
+ `is_subgraph_free_open_bowtie=0` -> `is_subgraph_free_K3=0`
+ `girth=7` -> `is_subgraph_free_K3=1`
+ `is_bipartite=1` -> `is_subgraph_free_K3=1`
+ `chromatic_number=6` -> `is_subgraph_free_K4=0`
+ `chromatic_number=7` -> `is_subgraph_free_K4=0`
+ `is_subgraph_free_K5=0` -> `is_subgraph_free_K4=0`
+ `k_max_clique=4` -> `is_subgraph_free_K4=0`
+ `k_max_clique=5` -> `is_subgraph_free_K4=0`
+ `k_max_clique=6` -> `is_subgraph_free_K4=0`
+ `k_max_clique=7` -> `is_subgraph_free_K4=0`
+ `girth=5` -> `is_subgraph_free_K4=1`
+ `girth=6` -> `is_subgraph_free_K4=1`
+ `girth=7` -> `is_subgraph_free_K4=1`
+ `is_k_regular=2` -> `is_subgraph_free_K4=1`
+ `is_k_regular=3` -> `is_subgraph_free_K4=1`
+ `is_bipartite=1` -> `is_subgraph_free_K4=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_K4=1`
+ `is_subgraph_free_C4=1` -> `is_subgraph_free_K4=1`
+ `k_max_clique=2` -> `is_subgraph_free_K4=1`
+ `k_max_clique=3` -> `is_subgraph_free_K4=1`
+ `is_subgraph_free_diamond=1` -> `is_subgraph_free_K4=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_K4=1`
+ `chromatic_number=7` -> `is_subgraph_free_K5=0`
+ `k_max_clique=5` -> `is_subgraph_free_K5=0`
+ `k_max_clique=6` -> `is_subgraph_free_K5=0`
+ `k_max_clique=7` -> `is_subgraph_free_K5=0`
+ `chromatic_number=2` -> `is_subgraph_free_K5=1`
+ `circumference=0` -> `is_subgraph_free_K5=1`
+ `circumference=3` -> `is_subgraph_free_K5=1`
+ `circumference=4` -> `is_subgraph_free_K5=1`
+ `girth=0` -> `is_subgraph_free_K5=1`
+ `girth=4` -> `is_subgraph_free_K5=1`
+ `girth=5` -> `is_subgraph_free_K5=1`
+ `girth=6` -> `is_subgraph_free_K5=1`
+ `girth=7` -> `is_subgraph_free_K5=1`
+ `is_k_regular=2` -> `is_subgraph_free_K5=1`
+ `is_k_regular=3` -> `is_subgraph_free_K5=1`
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
+ `is_subgraph_free_bull=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_bowtie=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_diamond=1` -> `is_subgraph_free_K5=1`
+ `is_subgraph_free_open_bowtie=1` -> `is_subgraph_free_K5=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_K5=1`
+ `chromatic_number=5` -> `is_subgraph_free_C4=0`
+ `chromatic_number=6` -> `is_subgraph_free_C4=0`
+ `chromatic_number=7` -> `is_subgraph_free_C4=0`
+ `is_k_regular=4` -> `is_subgraph_free_C4=0`
+ `is_k_regular=6` -> `is_subgraph_free_C4=0`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_C4=0`
+ `is_subgraph_free_K5=0` -> `is_subgraph_free_C4=0`
+ `vertex_connectivity>3` -> `is_subgraph_free_C4=0`
+ `vertex_connectivity>4` -> `is_subgraph_free_C4=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_C4=0`
+ `edge_connectivity=4` -> `is_subgraph_free_C4=0`
+ `edge_connectivity=5` -> `is_subgraph_free_C4=0`
+ `edge_connectivity=6` -> `is_subgraph_free_C4=0`
+ `k_max_clique=4` -> `is_subgraph_free_C4=0`
+ `k_max_clique=5` -> `is_subgraph_free_C4=0`
+ `k_max_clique=6` -> `is_subgraph_free_C4=0`
+ `k_max_clique=7` -> `is_subgraph_free_C4=0`
+ `is_subgraph_free_diamond=0` -> `is_subgraph_free_C4=0`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C4=1`
+ `automorphism_group_n=10` -> `is_subgraph_free_C5=0`
+ `chromatic_number=6` -> `is_subgraph_free_C5=0`
+ `chromatic_number=7` -> `is_subgraph_free_C5=0`
+ `is_k_regular=6` -> `is_subgraph_free_C5=0`
+ `is_subgraph_free_K5=0` -> `is_subgraph_free_C5=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_C5=0`
+ `edge_connectivity=6` -> `is_subgraph_free_C5=0`
+ `k_max_clique=5` -> `is_subgraph_free_C5=0`
+ `k_max_clique=6` -> `is_subgraph_free_C5=0`
+ `k_max_clique=7` -> `is_subgraph_free_C5=0`
+ `girth=7` -> `is_subgraph_free_C5=1`
+ `is_bipartite=1` -> `is_subgraph_free_C5=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C5=1`
+ `chromatic_number=6` -> `is_subgraph_free_C6=0`
+ `chromatic_number=7` -> `is_subgraph_free_C6=0`
+ `is_k_regular=6` -> `is_subgraph_free_C6=0`
+ `vertex_connectivity>4` -> `is_subgraph_free_C6=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_C6=0`
+ `edge_connectivity=5` -> `is_subgraph_free_C6=0`
+ `edge_connectivity=6` -> `is_subgraph_free_C6=0`
+ `k_max_clique=6` -> `is_subgraph_free_C6=0`
+ `k_max_clique=7` -> `is_subgraph_free_C6=0`
+ `n_articulation_points=5` -> `is_subgraph_free_C6=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C6=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C6=1`
+ `automorphism_group_n=14` -> `is_subgraph_free_C7=0`
+ `chromatic_number=7` -> `is_subgraph_free_C7=0`
+ `is_k_regular=6` -> `is_subgraph_free_C7=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_C7=0`
+ `edge_connectivity=6` -> `is_subgraph_free_C7=0`
+ `k_max_clique=7` -> `is_subgraph_free_C7=0`
+ `circumference=0` -> `is_subgraph_free_C7=1`
+ `circumference=3` -> `is_subgraph_free_C7=1`
+ `girth=0` -> `is_subgraph_free_C7=1`
+ `is_k_regular=2` -> `is_subgraph_free_C7=1`
+ `is_bipartite=1` -> `is_subgraph_free_C7=1`
+ `n_articulation_points=4` -> `is_subgraph_free_C7=1`
+ `n_articulation_points=5` -> `is_subgraph_free_C7=1`
+ `is_tree=1` -> `is_subgraph_free_C7=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C7=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C7=1`
+ `circumference=0` -> `is_subgraph_free_C8=1`
+ `circumference=3` -> `is_subgraph_free_C8=1`
+ `circumference=4` -> `is_subgraph_free_C8=1`
+ `circumference=5` -> `is_subgraph_free_C8=1`
+ `circumference=6` -> `is_subgraph_free_C8=1`
+ `circumference=7` -> `is_subgraph_free_C8=1`
+ `girth=0` -> `is_subgraph_free_C8=1`
+ `n_articulation_points=3` -> `is_subgraph_free_C8=1`
+ `n_articulation_points=4` -> `is_subgraph_free_C8=1`
+ `n_articulation_points=5` -> `is_subgraph_free_C8=1`
+ `is_tree=1` -> `is_subgraph_free_C8=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C8=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C8=1`
+ `maximal_independent_edge_set=3` -> `is_subgraph_free_C8=1`
+ `chromatic_number=2` -> `is_subgraph_free_C9=1`
+ `diameter=6` -> `is_subgraph_free_C9=1`
+ `circumference=0` -> `is_subgraph_free_C9=1`
+ `circumference=3` -> `is_subgraph_free_C9=1`
+ `circumference=4` -> `is_subgraph_free_C9=1`
+ `circumference=5` -> `is_subgraph_free_C9=1`
+ `circumference=6` -> `is_subgraph_free_C9=1`
+ `circumference=7` -> `is_subgraph_free_C9=1`
+ `girth=0` -> `is_subgraph_free_C9=1`
+ `girth=7` -> `is_subgraph_free_C9=1`
+ `is_bipartite=1` -> `is_subgraph_free_C9=1`
+ `n_articulation_points=2` -> `is_subgraph_free_C9=1`
+ `n_articulation_points=3` -> `is_subgraph_free_C9=1`
+ `n_articulation_points=4` -> `is_subgraph_free_C9=1`
+ `n_articulation_points=5` -> `is_subgraph_free_C9=1`
+ `is_tree=1` -> `is_subgraph_free_C9=1`
+ `maximal_independent_vertex_set=6` -> `is_subgraph_free_C9=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C9=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C9=1`
+ `maximal_independent_edge_set=3` -> `is_subgraph_free_C9=1`
+ `automorphism_group_n=14` -> `is_subgraph_free_C10=1`
+ `automorphism_group_n=5040` -> `is_subgraph_free_C10=1`
+ `diameter=6` -> `is_subgraph_free_C10=1`
+ `circumference=0` -> `is_subgraph_free_C10=1`
+ `circumference=3` -> `is_subgraph_free_C10=1`
+ `circumference=4` -> `is_subgraph_free_C10=1`
+ `circumference=5` -> `is_subgraph_free_C10=1`
+ `circumference=6` -> `is_subgraph_free_C10=1`
+ `circumference=7` -> `is_subgraph_free_C10=1`
+ `girth=0` -> `is_subgraph_free_C10=1`
+ `girth=7` -> `is_subgraph_free_C10=1`
+ `n_articulation_points=1` -> `is_subgraph_free_C10=1`
+ `n_articulation_points=2` -> `is_subgraph_free_C10=1`
+ `n_articulation_points=3` -> `is_subgraph_free_C10=1`
+ `n_articulation_points=4` -> `is_subgraph_free_C10=1`
+ `n_articulation_points=5` -> `is_subgraph_free_C10=1`
+ `edge_connectivity=1` -> `is_subgraph_free_C10=1`
+ `is_tree=1` -> `is_subgraph_free_C10=1`
+ `is_hamiltonian=0` -> `is_subgraph_free_C10=1`
+ `maximal_independent_vertex_set=6` -> `is_subgraph_free_C10=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_C10=1`
+ `maximal_independent_edge_set=2` -> `is_subgraph_free_C10=1`
+ `maximal_independent_edge_set=3` -> `is_subgraph_free_C10=1`
+ `automorphism_group_n=1` -> `is_integral=0`
+ `automorphism_group_n=10` -> `is_integral=0`
+ `automorphism_group_n=14` -> `is_integral=0`
+ `automorphism_group_n=20` -> `is_integral=0`
+ `automorphism_group_n=36` -> `is_integral=0`
+ `diameter=5` -> `is_integral=0`
+ `diameter=6` -> `is_integral=0`
+ `girth=7` -> `is_integral=0`
+ `n_articulation_points=5` -> `is_integral=0`
+ `is_real_spectrum=1` -> `is_integral=0`
+ `diameter=1` -> `is_integral=1`
+ `automorphism_group_n=1` -> `vertex_connectivity>0`
+ `automorphism_group_n=2` -> `vertex_connectivity>0`
+ `automorphism_group_n=4` -> `vertex_connectivity>0`
+ `automorphism_group_n=6` -> `vertex_connectivity>0`
+ `automorphism_group_n=8` -> `vertex_connectivity>0`
+ `automorphism_group_n=10` -> `vertex_connectivity>0`
+ `automorphism_group_n=12` -> `vertex_connectivity>0`
+ `automorphism_group_n=14` -> `vertex_connectivity>0`
+ `automorphism_group_n=16` -> `vertex_connectivity>0`
+ `automorphism_group_n=20` -> `vertex_connectivity>0`
+ `automorphism_group_n=24` -> `vertex_connectivity>0`
+ `automorphism_group_n=36` -> `vertex_connectivity>0`
+ `automorphism_group_n=48` -> `vertex_connectivity>0`
+ `automorphism_group_n=72` -> `vertex_connectivity>0`
+ `automorphism_group_n=120` -> `vertex_connectivity>0`
+ `automorphism_group_n=144` -> `vertex_connectivity>0`
+ `automorphism_group_n=240` -> `vertex_connectivity>0`
+ `automorphism_group_n=720` -> `vertex_connectivity>0`
+ `automorphism_group_n=5040` -> `vertex_connectivity>0`
+ `chromatic_number=2` -> `vertex_connectivity>0`
+ `chromatic_number=3` -> `vertex_connectivity>0`
+ `chromatic_number=4` -> `vertex_connectivity>0`
+ `chromatic_number=5` -> `vertex_connectivity>0`
+ `chromatic_number=6` -> `vertex_connectivity>0`
+ `chromatic_number=7` -> `vertex_connectivity>0`
+ `diameter=1` -> `vertex_connectivity>0`
+ `diameter=2` -> `vertex_connectivity>0`
+ `diameter=3` -> `vertex_connectivity>0`
+ `diameter=4` -> `vertex_connectivity>0`
+ `diameter=5` -> `vertex_connectivity>0`
+ `diameter=6` -> `vertex_connectivity>0`
+ `circumference=0` -> `vertex_connectivity>0`
+ `circumference=3` -> `vertex_connectivity>0`
+ `circumference=4` -> `vertex_connectivity>0`
+ `circumference=5` -> `vertex_connectivity>0`
+ `circumference=6` -> `vertex_connectivity>0`
+ `circumference=7` -> `vertex_connectivity>0`
+ `girth=0` -> `vertex_connectivity>0`
+ `girth=3` -> `vertex_connectivity>0`
+ `girth=4` -> `vertex_connectivity>0`
+ `girth=5` -> `vertex_connectivity>0`
+ `girth=6` -> `vertex_connectivity>0`
+ `girth=7` -> `vertex_connectivity>0`
+ `is_k_regular=0` -> `vertex_connectivity>0`
+ `is_k_regular=2` -> `vertex_connectivity>0`
+ `is_k_regular=3` -> `vertex_connectivity>0`
+ `is_k_regular=4` -> `vertex_connectivity>0`
+ `is_k_regular=6` -> `vertex_connectivity>0`
+ `is_strongly_regular=0` -> `vertex_connectivity>0`
+ `is_strongly_regular=1` -> `vertex_connectivity>0`
+ `radius=1` -> `vertex_connectivity>0`
+ `radius=2` -> `vertex_connectivity>0`
+ `radius=3` -> `vertex_connectivity>0`
+ `is_eulerian=0` -> `vertex_connectivity>0`
+ `is_eulerian=1` -> `vertex_connectivity>0`
+ `is_distance_regular=0` -> `vertex_connectivity>0`
+ `is_distance_regular=1` -> `vertex_connectivity>0`
+ `is_planar=0` -> `vertex_connectivity>0`
+ `is_planar=1` -> `vertex_connectivity>0`
+ `is_bipartite=0` -> `vertex_connectivity>0`
+ `is_bipartite=1` -> `vertex_connectivity>0`
+ `n_articulation_points=0` -> `vertex_connectivity>0`
+ `n_articulation_points=1` -> `vertex_connectivity>0`
+ `n_articulation_points=2` -> `vertex_connectivity>0`
+ `n_articulation_points=3` -> `vertex_connectivity>0`
+ `n_articulation_points=4` -> `vertex_connectivity>0`
+ `n_articulation_points=5` -> `vertex_connectivity>0`
+ `is_subgraph_free_K3=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_K3=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_K4=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_K4=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_K5=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_K5=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C4=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_C4=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C5=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_C5=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C6=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_C6=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C7=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_C7=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C8=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C9=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_C10=1` -> `vertex_connectivity>0`
+ `is_integral=0` -> `vertex_connectivity>0`
+ `is_integral=1` -> `vertex_connectivity>0`
+ `edge_connectivity=1` -> `vertex_connectivity>0`
+ `edge_connectivity=2` -> `vertex_connectivity>0`
+ `edge_connectivity=3` -> `vertex_connectivity>0`
+ `edge_connectivity=4` -> `vertex_connectivity>0`
+ `edge_connectivity=5` -> `vertex_connectivity>0`
+ `edge_connectivity=6` -> `vertex_connectivity>0`
+ `is_tree=0` -> `vertex_connectivity>0`
+ `is_tree=1` -> `vertex_connectivity>0`
+ `is_chordal=0` -> `vertex_connectivity>0`
+ `is_chordal=1` -> `vertex_connectivity>0`
+ `k_max_clique=2` -> `vertex_connectivity>0`
+ `k_max_clique=3` -> `vertex_connectivity>0`
+ `k_max_clique=4` -> `vertex_connectivity>0`
+ `k_max_clique=5` -> `vertex_connectivity>0`
+ `k_max_clique=6` -> `vertex_connectivity>0`
+ `k_max_clique=7` -> `vertex_connectivity>0`
+ `is_real_spectrum=0` -> `vertex_connectivity>0`
+ `is_real_spectrum=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_bull=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_bull=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_bowtie=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_bowtie=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_diamond=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_diamond=1` -> `vertex_connectivity>0`
+ `is_subgraph_free_open_bowtie=0` -> `vertex_connectivity>0`
+ `is_subgraph_free_open_bowtie=1` -> `vertex_connectivity>0`
+ `is_hamiltonian=0` -> `vertex_connectivity>0`
+ `is_hamiltonian=1` -> `vertex_connectivity>0`
+ `has_fractional_duality_gap_vertex_chromatic=0` -> `vertex_connectivity>0`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=1` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=2` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=3` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=4` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=5` -> `vertex_connectivity>0`
+ `maximal_independent_vertex_set=6` -> `vertex_connectivity>0`
+ `maximal_independent_edge_set=1` -> `vertex_connectivity>0`
+ `maximal_independent_edge_set=2` -> `vertex_connectivity>0`
+ `maximal_independent_edge_set=3` -> `vertex_connectivity>0`
+ `diameter=1` -> `vertex_connectivity>1`
+ `is_k_regular=4` -> `vertex_connectivity>1`
+ `is_k_regular=6` -> `vertex_connectivity>1`
+ `is_strongly_regular=1` -> `vertex_connectivity>1`
+ `is_distance_regular=1` -> `vertex_connectivity>1`
+ `edge_connectivity=5` -> `vertex_connectivity>1`
+ `edge_connectivity=6` -> `vertex_connectivity>1`
+ `is_hamiltonian=1` -> `vertex_connectivity>1`
+ `is_k_regular=6` -> `vertex_connectivity>2`
+ `edge_connectivity=6` -> `vertex_connectivity>2`
+ `is_k_regular=6` -> `vertex_connectivity>3`
+ `edge_connectivity=6` -> `vertex_connectivity>3`
+ `n_articulation_points=4` -> `edge_connectivity=1`
+ `n_articulation_points=5` -> `edge_connectivity=1`
+ `is_k_regular=6` -> `edge_connectivity=6`
+ `automorphism_group_n=10` -> `is_tree=0`
+ `automorphism_group_n=14` -> `is_tree=0`
+ `automorphism_group_n=20` -> `is_tree=0`
+ `chromatic_number=3` -> `is_tree=0`
+ `chromatic_number=4` -> `is_tree=0`
+ `chromatic_number=5` -> `is_tree=0`
+ `chromatic_number=6` -> `is_tree=0`
+ `chromatic_number=7` -> `is_tree=0`
+ `circumference=3` -> `is_tree=0`
+ `circumference=4` -> `is_tree=0`
+ `circumference=5` -> `is_tree=0`
+ `circumference=6` -> `is_tree=0`
+ `circumference=7` -> `is_tree=0`
+ `girth=3` -> `is_tree=0`
+ `girth=4` -> `is_tree=0`
+ `girth=5` -> `is_tree=0`
+ `girth=6` -> `is_tree=0`
+ `girth=7` -> `is_tree=0`
+ `is_k_regular=2` -> `is_tree=0`
+ `is_k_regular=3` -> `is_tree=0`
+ `is_k_regular=4` -> `is_tree=0`
+ `is_k_regular=6` -> `is_tree=0`
+ `is_eulerian=1` -> `is_tree=0`
+ `is_subgraph_free_K5=0` -> `is_tree=0`
+ `is_subgraph_free_C7=0` -> `is_tree=0`
+ `vertex_connectivity>3` -> `is_tree=0`
+ `vertex_connectivity>4` -> `is_tree=0`
+ `vertex_connectivity>5` -> `is_tree=0`
+ `edge_connectivity=2` -> `is_tree=0`
+ `edge_connectivity=4` -> `is_tree=0`
+ `edge_connectivity=5` -> `is_tree=0`
+ `edge_connectivity=6` -> `is_tree=0`
+ `k_max_clique=5` -> `is_tree=0`
+ `k_max_clique=6` -> `is_tree=0`
+ `k_max_clique=7` -> `is_tree=0`
+ `has_fractional_duality_gap_vertex_chromatic=1` -> `is_tree=0`
+ `maximal_independent_vertex_set=1` -> `is_tree=0`
+ `automorphism_group_n=14` -> `is_chordal=0`
+ `automorphism_group_n=20` -> `is_chordal=0`
+ `girth=6` -> `is_chordal=0`
+ `girth=7` -> `is_chordal=0`
+ `diameter=1` -> `is_chordal=1`
+ `maximal_independent_vertex_set=1` -> `is_chordal=1`
+ `maximal_independent_edge_set=1` -> `is_chordal=1`
+ `girth=7` -> `k_max_clique=2`
+ `is_bipartite=1` -> `k_max_clique=2`
+ `automorphism_group_n=6` -> `is_real_spectrum=0`
+ `automorphism_group_n=10` -> `is_real_spectrum=0`
+ `automorphism_group_n=12` -> `is_real_spectrum=0`
+ `automorphism_group_n=14` -> `is_real_spectrum=0`
+ `automorphism_group_n=16` -> `is_real_spectrum=0`
+ `automorphism_group_n=20` -> `is_real_spectrum=0`
+ `automorphism_group_n=24` -> `is_real_spectrum=0`
+ `automorphism_group_n=36` -> `is_real_spectrum=0`
+ `automorphism_group_n=48` -> `is_real_spectrum=0`
+ `automorphism_group_n=72` -> `is_real_spectrum=0`
+ `automorphism_group_n=120` -> `is_real_spectrum=0`
+ `automorphism_group_n=144` -> `is_real_spectrum=0`
+ `automorphism_group_n=240` -> `is_real_spectrum=0`
+ `automorphism_group_n=720` -> `is_real_spectrum=0`
+ `automorphism_group_n=5040` -> `is_real_spectrum=0`
+ `chromatic_number=7` -> `is_real_spectrum=0`
+ `diameter=1` -> `is_real_spectrum=0`
+ `is_strongly_regular=1` -> `is_real_spectrum=0`
+ `is_distance_regular=1` -> `is_real_spectrum=0`
+ `is_integral=1` -> `is_real_spectrum=0`
+ `k_max_clique=7` -> `is_real_spectrum=0`
+ `chromatic_number=5` -> `is_subgraph_free_bull=0`
+ `chromatic_number=6` -> `is_subgraph_free_bull=0`
+ `chromatic_number=7` -> `is_subgraph_free_bull=0`
+ `is_k_regular=6` -> `is_subgraph_free_bull=0`
+ `is_subgraph_free_K5=0` -> `is_subgraph_free_bull=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_bull=0`
+ `edge_connectivity=6` -> `is_subgraph_free_bull=0`
+ `k_max_clique=5` -> `is_subgraph_free_bull=0`
+ `k_max_clique=6` -> `is_subgraph_free_bull=0`
+ `k_max_clique=7` -> `is_subgraph_free_bull=0`
+ `girth=7` -> `is_subgraph_free_bull=1`
+ `is_k_regular=2` -> `is_subgraph_free_bull=1`
+ `is_bipartite=1` -> `is_subgraph_free_bull=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_bull=1`
+ `k_max_clique=2` -> `is_subgraph_free_bull=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_bull=1`
+ `chromatic_number=6` -> `is_subgraph_free_bowtie=0`
+ `chromatic_number=7` -> `is_subgraph_free_bowtie=0`
+ `is_k_regular=6` -> `is_subgraph_free_bowtie=0`
+ `is_subgraph_free_K5=0` -> `is_subgraph_free_bowtie=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_bowtie=0`
+ `edge_connectivity=6` -> `is_subgraph_free_bowtie=0`
+ `k_max_clique=5` -> `is_subgraph_free_bowtie=0`
+ `k_max_clique=6` -> `is_subgraph_free_bowtie=0`
+ `k_max_clique=7` -> `is_subgraph_free_bowtie=0`
+ `girth=7` -> `is_subgraph_free_bowtie=1`
+ `is_k_regular=2` -> `is_subgraph_free_bowtie=1`
+ `is_k_regular=3` -> `is_subgraph_free_bowtie=1`
+ `is_bipartite=1` -> `is_subgraph_free_bowtie=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_bowtie=1`
+ `k_max_clique=2` -> `is_subgraph_free_bowtie=1`
+ `is_subgraph_free_open_bowtie=1` -> `is_subgraph_free_bowtie=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_bowtie=1`
+ `chromatic_number=5` -> `is_subgraph_free_diamond=0`
+ `chromatic_number=6` -> `is_subgraph_free_diamond=0`
+ `chromatic_number=7` -> `is_subgraph_free_diamond=0`
+ `is_k_regular=6` -> `is_subgraph_free_diamond=0`
+ `is_subgraph_free_K4=0` -> `is_subgraph_free_diamond=0`
+ `is_subgraph_free_K5=0` -> `is_subgraph_free_diamond=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_diamond=0`
+ `edge_connectivity=6` -> `is_subgraph_free_diamond=0`
+ `k_max_clique=4` -> `is_subgraph_free_diamond=0`
+ `k_max_clique=5` -> `is_subgraph_free_diamond=0`
+ `k_max_clique=6` -> `is_subgraph_free_diamond=0`
+ `k_max_clique=7` -> `is_subgraph_free_diamond=0`
+ `girth=7` -> `is_subgraph_free_diamond=1`
+ `is_k_regular=2` -> `is_subgraph_free_diamond=1`
+ `is_bipartite=1` -> `is_subgraph_free_diamond=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_diamond=1`
+ `is_subgraph_free_C4=1` -> `is_subgraph_free_diamond=1`
+ `k_max_clique=2` -> `is_subgraph_free_diamond=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_diamond=1`
+ `chromatic_number=5` -> `is_subgraph_free_open_bowtie=0`
+ `chromatic_number=6` -> `is_subgraph_free_open_bowtie=0`
+ `chromatic_number=7` -> `is_subgraph_free_open_bowtie=0`
+ `is_k_regular=6` -> `is_subgraph_free_open_bowtie=0`
+ `is_subgraph_free_K5=0` -> `is_subgraph_free_open_bowtie=0`
+ `vertex_connectivity>5` -> `is_subgraph_free_open_bowtie=0`
+ `edge_connectivity=6` -> `is_subgraph_free_open_bowtie=0`
+ `k_max_clique=5` -> `is_subgraph_free_open_bowtie=0`
+ `k_max_clique=6` -> `is_subgraph_free_open_bowtie=0`
+ `k_max_clique=7` -> `is_subgraph_free_open_bowtie=0`
+ `is_subgraph_free_bowtie=0` -> `is_subgraph_free_open_bowtie=0`
+ `girth=7` -> `is_subgraph_free_open_bowtie=1`
+ `is_k_regular=2` -> `is_subgraph_free_open_bowtie=1`
+ `is_k_regular=3` -> `is_subgraph_free_open_bowtie=1`
+ `is_bipartite=1` -> `is_subgraph_free_open_bowtie=1`
+ `is_subgraph_free_K3=1` -> `is_subgraph_free_open_bowtie=1`
+ `k_max_clique=2` -> `is_subgraph_free_open_bowtie=1`
+ `maximal_independent_edge_set=1` -> `is_subgraph_free_open_bowtie=1`
+ `diameter=6` -> `is_hamiltonian=0`
+ `girth=7` -> `is_hamiltonian=0`
+ `n_articulation_points=1` -> `is_hamiltonian=0`
+ `n_articulation_points=2` -> `is_hamiltonian=0`
+ `n_articulation_points=3` -> `is_hamiltonian=0`
+ `n_articulation_points=4` -> `is_hamiltonian=0`
+ `n_articulation_points=5` -> `is_hamiltonian=0`
+ `edge_connectivity=1` -> `is_hamiltonian=0`
+ `maximal_independent_vertex_set=6` -> `is_hamiltonian=0`
+ `diameter=1` -> `is_hamiltonian=1`
+ `is_k_regular=4` -> `is_hamiltonian=1`
+ `is_k_regular=6` -> `is_hamiltonian=1`
+ `vertex_connectivity>4` -> `is_hamiltonian=1`
+ `vertex_connectivity>5` -> `is_hamiltonian=1`
+ `edge_connectivity=5` -> `is_hamiltonian=1`
+ `edge_connectivity=6` -> `is_hamiltonian=1`
+ `automorphism_group_n=720` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `automorphism_group_n=5040` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `chromatic_number=2` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `diameter=1` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `circumference=0` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `circumference=3` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `circumference=4` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `girth=0` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `is_tree=1` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `maximal_independent_vertex_set=1` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `maximal_independent_edge_set=1` -> `has_fractional_duality_gap_vertex_chromatic=0`
+ `girth=7` -> `has_fractional_duality_gap_vertex_chromatic=1`

# Exclusive relations
+ `automorphism_group_n=1` intersect `diameter=1` = 0
+ `automorphism_group_n=1` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=1` intersect `is_k_regular=6` = 0
+ `automorphism_group_n=1` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=1` intersect `is_distance_regular=1` = 0
+ `automorphism_group_n=1` intersect `is_integral=1` = 0
+ `automorphism_group_n=1` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=1` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=1` intersect `maximal_independent_edge_set=2` = 0
+ `automorphism_group_n=2` intersect `diameter=1` = 0
+ `automorphism_group_n=2` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=2` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=2` intersect `is_distance_regular=1` = 0
+ `automorphism_group_n=4` intersect `diameter=1` = 0
+ `automorphism_group_n=4` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=4` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=4` intersect `is_distance_regular=1` = 0
+ `automorphism_group_n=4` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=4` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=6` intersect `girth=7` = 0
+ `automorphism_group_n=6` intersect `is_k_regular=4` = 0
+ `automorphism_group_n=6` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=8` intersect `diameter=1` = 0
+ `automorphism_group_n=8` intersect `girth=7` = 0
+ `automorphism_group_n=8` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=8` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=10` intersect `chromatic_number=2` = 0
+ `automorphism_group_n=10` intersect `chromatic_number=7` = 0
+ `automorphism_group_n=10` intersect `diameter=1` = 0
+ `automorphism_group_n=10` intersect `diameter=6` = 0
+ `automorphism_group_n=10` intersect `circumference=0` = 0
+ `automorphism_group_n=10` intersect `circumference=3` = 0
+ `automorphism_group_n=10` intersect `circumference=4` = 0
+ `automorphism_group_n=10` intersect `girth=0` = 0
+ `automorphism_group_n=10` intersect `girth=6` = 0
+ `automorphism_group_n=10` intersect `girth=7` = 0
+ `automorphism_group_n=10` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=10` intersect `is_k_regular=6` = 0
+ `automorphism_group_n=10` intersect `is_bipartite=1` = 0
+ `automorphism_group_n=10` intersect `is_subgraph_free_C5=1` = 0
+ `automorphism_group_n=10` intersect `is_integral=1` = 0
+ `automorphism_group_n=10` intersect `is_tree=1` = 0
+ `automorphism_group_n=10` intersect `k_max_clique=6` = 0
+ `automorphism_group_n=10` intersect `k_max_clique=7` = 0
+ `automorphism_group_n=10` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=10` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=10` intersect `maximal_independent_vertex_set=6` = 0
+ `automorphism_group_n=10` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=12` intersect `diameter=1` = 0
+ `automorphism_group_n=12` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=12` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=12` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=12` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=14` intersect `chromatic_number=3` = 0
+ `automorphism_group_n=14` intersect `chromatic_number=7` = 0
+ `automorphism_group_n=14` intersect `diameter=1` = 0
+ `automorphism_group_n=14` intersect `diameter=4` = 0
+ `automorphism_group_n=14` intersect `diameter=5` = 0
+ `automorphism_group_n=14` intersect `diameter=6` = 0
+ `automorphism_group_n=14` intersect `circumference=0` = 0
+ `automorphism_group_n=14` intersect `circumference=3` = 0
+ `automorphism_group_n=14` intersect `circumference=4` = 0
+ `automorphism_group_n=14` intersect `circumference=5` = 0
+ `automorphism_group_n=14` intersect `girth=0` = 0
+ `automorphism_group_n=14` intersect `girth=5` = 0
+ `automorphism_group_n=14` intersect `girth=6` = 0
+ `automorphism_group_n=14` intersect `girth=7` = 0
+ `automorphism_group_n=14` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=14` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=14` intersect `is_k_regular=4` = 0
+ `automorphism_group_n=14` intersect `is_k_regular=6` = 0
+ `automorphism_group_n=14` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=14` intersect `is_bipartite=1` = 0
+ `automorphism_group_n=14` intersect `n_articulation_points=3` = 0
+ `automorphism_group_n=14` intersect `n_articulation_points=4` = 0
+ `automorphism_group_n=14` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=14` intersect `is_subgraph_free_C7=1` = 0
+ `automorphism_group_n=14` intersect `is_integral=1` = 0
+ `automorphism_group_n=14` intersect `vertex_connectivity>5` = 0
+ `automorphism_group_n=14` intersect `edge_connectivity=6` = 0
+ `automorphism_group_n=14` intersect `is_tree=1` = 0
+ `automorphism_group_n=14` intersect `is_chordal=1` = 0
+ `automorphism_group_n=14` intersect `k_max_clique=6` = 0
+ `automorphism_group_n=14` intersect `k_max_clique=7` = 0
+ `automorphism_group_n=14` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=14` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=14` intersect `maximal_independent_vertex_set=5` = 0
+ `automorphism_group_n=14` intersect `maximal_independent_vertex_set=6` = 0
+ `automorphism_group_n=14` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=14` intersect `maximal_independent_edge_set=2` = 0
+ `automorphism_group_n=16` intersect `diameter=1` = 0
+ `automorphism_group_n=16` intersect `girth=7` = 0
+ `automorphism_group_n=16` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=16` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=16` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=16` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=16` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=20` intersect `chromatic_number=7` = 0
+ `automorphism_group_n=20` intersect `diameter=1` = 0
+ `automorphism_group_n=20` intersect `diameter=6` = 0
+ `automorphism_group_n=20` intersect `circumference=0` = 0
+ `automorphism_group_n=20` intersect `circumference=3` = 0
+ `automorphism_group_n=20` intersect `circumference=4` = 0
+ `automorphism_group_n=20` intersect `circumference=5` = 0
+ `automorphism_group_n=20` intersect `girth=0` = 0
+ `automorphism_group_n=20` intersect `girth=5` = 0
+ `automorphism_group_n=20` intersect `girth=6` = 0
+ `automorphism_group_n=20` intersect `girth=7` = 0
+ `automorphism_group_n=20` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=20` intersect `n_articulation_points=4` = 0
+ `automorphism_group_n=20` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=20` intersect `is_integral=1` = 0
+ `automorphism_group_n=20` intersect `is_tree=1` = 0
+ `automorphism_group_n=20` intersect `is_chordal=1` = 0
+ `automorphism_group_n=20` intersect `k_max_clique=6` = 0
+ `automorphism_group_n=20` intersect `k_max_clique=7` = 0
+ `automorphism_group_n=20` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=20` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=20` intersect `maximal_independent_vertex_set=6` = 0
+ `automorphism_group_n=20` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=20` intersect `maximal_independent_edge_set=2` = 0
+ `automorphism_group_n=24` intersect `girth=7` = 0
+ `automorphism_group_n=24` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=24` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=24` intersect `is_k_regular=4` = 0
+ `automorphism_group_n=24` intersect `is_k_regular=6` = 0
+ `automorphism_group_n=24` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=24` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=36` intersect `diameter=1` = 0
+ `automorphism_group_n=36` intersect `diameter=6` = 0
+ `automorphism_group_n=36` intersect `girth=6` = 0
+ `automorphism_group_n=36` intersect `girth=7` = 0
+ `automorphism_group_n=36` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=36` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=36` intersect `is_k_regular=4` = 0
+ `automorphism_group_n=36` intersect `is_k_regular=6` = 0
+ `automorphism_group_n=36` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=36` intersect `is_distance_regular=1` = 0
+ `automorphism_group_n=36` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=36` intersect `is_integral=1` = 0
+ `automorphism_group_n=36` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=36` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=36` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=48` intersect `diameter=1` = 0
+ `automorphism_group_n=48` intersect `girth=7` = 0
+ `automorphism_group_n=48` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=48` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=48` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=48` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=48` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=72` intersect `diameter=1` = 0
+ `automorphism_group_n=72` intersect `diameter=6` = 0
+ `automorphism_group_n=72` intersect `girth=5` = 0
+ `automorphism_group_n=72` intersect `girth=6` = 0
+ `automorphism_group_n=72` intersect `girth=7` = 0
+ `automorphism_group_n=72` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=72` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=72` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=72` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=72` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=120` intersect `diameter=6` = 0
+ `automorphism_group_n=120` intersect `girth=6` = 0
+ `automorphism_group_n=120` intersect `girth=7` = 0
+ `automorphism_group_n=120` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=120` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=144` intersect `diameter=1` = 0
+ `automorphism_group_n=144` intersect `diameter=5` = 0
+ `automorphism_group_n=144` intersect `diameter=6` = 0
+ `automorphism_group_n=144` intersect `girth=5` = 0
+ `automorphism_group_n=144` intersect `girth=6` = 0
+ `automorphism_group_n=144` intersect `girth=7` = 0
+ `automorphism_group_n=144` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=144` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=144` intersect `is_k_regular=6` = 0
+ `automorphism_group_n=144` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=144` intersect `is_distance_regular=1` = 0
+ `automorphism_group_n=144` intersect `n_articulation_points=4` = 0
+ `automorphism_group_n=144` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=144` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=144` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=144` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=240` intersect `diameter=1` = 0
+ `automorphism_group_n=240` intersect `diameter=5` = 0
+ `automorphism_group_n=240` intersect `diameter=6` = 0
+ `automorphism_group_n=240` intersect `girth=7` = 0
+ `automorphism_group_n=240` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=240` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=240` intersect `is_k_regular=6` = 0
+ `automorphism_group_n=240` intersect `is_strongly_regular=1` = 0
+ `automorphism_group_n=240` intersect `n_articulation_points=4` = 0
+ `automorphism_group_n=240` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=240` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=240` intersect `maximal_independent_vertex_set=1` = 0
+ `automorphism_group_n=240` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=720` intersect `diameter=5` = 0
+ `automorphism_group_n=720` intersect `diameter=6` = 0
+ `automorphism_group_n=720` intersect `girth=5` = 0
+ `automorphism_group_n=720` intersect `girth=6` = 0
+ `automorphism_group_n=720` intersect `girth=7` = 0
+ `automorphism_group_n=720` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=720` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=720` intersect `is_k_regular=4` = 0
+ `automorphism_group_n=720` intersect `is_k_regular=6` = 0
+ `automorphism_group_n=720` intersect `radius=3` = 0
+ `automorphism_group_n=720` intersect `n_articulation_points=4` = 0
+ `automorphism_group_n=720` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=720` intersect `vertex_connectivity>5` = 0
+ `automorphism_group_n=720` intersect `edge_connectivity=6` = 0
+ `automorphism_group_n=720` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=720` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `automorphism_group_n=720` intersect `maximal_independent_edge_set=1` = 0
+ `automorphism_group_n=5040` intersect `chromatic_number=4` = 0
+ `automorphism_group_n=5040` intersect `chromatic_number=5` = 0
+ `automorphism_group_n=5040` intersect `chromatic_number=6` = 0
+ `automorphism_group_n=5040` intersect `diameter=4` = 0
+ `automorphism_group_n=5040` intersect `diameter=5` = 0
+ `automorphism_group_n=5040` intersect `diameter=6` = 0
+ `automorphism_group_n=5040` intersect `circumference=3` = 0
+ `automorphism_group_n=5040` intersect `circumference=4` = 0
+ `automorphism_group_n=5040` intersect `circumference=5` = 0
+ `automorphism_group_n=5040` intersect `circumference=6` = 0
+ `automorphism_group_n=5040` intersect `girth=5` = 0
+ `automorphism_group_n=5040` intersect `girth=6` = 0
+ `automorphism_group_n=5040` intersect `girth=7` = 0
+ `automorphism_group_n=5040` intersect `is_k_regular=2` = 0
+ `automorphism_group_n=5040` intersect `is_k_regular=3` = 0
+ `automorphism_group_n=5040` intersect `is_k_regular=4` = 0
+ `automorphism_group_n=5040` intersect `radius=3` = 0
+ `automorphism_group_n=5040` intersect `n_articulation_points=3` = 0
+ `automorphism_group_n=5040` intersect `n_articulation_points=4` = 0
+ `automorphism_group_n=5040` intersect `n_articulation_points=5` = 0
+ `automorphism_group_n=5040` intersect `edge_connectivity=2` = 0
+ `automorphism_group_n=5040` intersect `edge_connectivity=3` = 0
+ `automorphism_group_n=5040` intersect `edge_connectivity=4` = 0
+ `automorphism_group_n=5040` intersect `edge_connectivity=5` = 0
+ `automorphism_group_n=5040` intersect `k_max_clique=4` = 0
+ `automorphism_group_n=5040` intersect `k_max_clique=5` = 0
+ `automorphism_group_n=5040` intersect `k_max_clique=6` = 0
+ `automorphism_group_n=5040` intersect `is_real_spectrum=1` = 0
+ `automorphism_group_n=5040` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `automorphism_group_n=5040` intersect `maximal_independent_vertex_set=3` = 0
+ `automorphism_group_n=5040` intersect `maximal_independent_vertex_set=4` = 0
+ `automorphism_group_n=5040` intersect `maximal_independent_vertex_set=5` = 0
+ `automorphism_group_n=5040` intersect `maximal_independent_vertex_set=6` = 0
+ `chromatic_number=2` intersect `automorphism_group_n=10` = 0
+ `chromatic_number=2` intersect `circumference=3` = 0
+ `chromatic_number=2` intersect `girth=3` = 0
+ `chromatic_number=2` intersect `girth=5` = 0
+ `chromatic_number=2` intersect `girth=7` = 0
+ `chromatic_number=2` intersect `is_k_regular=6` = 0
+ `chromatic_number=2` intersect `is_subgraph_free_K5=0` = 0
+ `chromatic_number=2` intersect `vertex_connectivity>5` = 0
+ `chromatic_number=2` intersect `edge_connectivity=6` = 0
+ `chromatic_number=2` intersect `k_max_clique=5` = 0
+ `chromatic_number=2` intersect `k_max_clique=6` = 0
+ `chromatic_number=2` intersect `k_max_clique=7` = 0
+ `chromatic_number=2` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `chromatic_number=2` intersect `maximal_independent_vertex_set=1` = 0
+ `chromatic_number=3` intersect `automorphism_group_n=14` = 0
+ `chromatic_number=3` intersect `circumference=0` = 0
+ `chromatic_number=3` intersect `girth=0` = 0
+ `chromatic_number=3` intersect `is_tree=1` = 0
+ `chromatic_number=3` intersect `k_max_clique=6` = 0
+ `chromatic_number=3` intersect `k_max_clique=7` = 0
+ `chromatic_number=4` intersect `automorphism_group_n=5040` = 0
+ `chromatic_number=4` intersect `diameter=1` = 0
+ `chromatic_number=4` intersect `circumference=0` = 0
+ `chromatic_number=4` intersect `circumference=3` = 0
+ `chromatic_number=4` intersect `girth=0` = 0
+ `chromatic_number=4` intersect `girth=5` = 0
+ `chromatic_number=4` intersect `girth=6` = 0
+ `chromatic_number=4` intersect `girth=7` = 0
+ `chromatic_number=4` intersect `is_k_regular=2` = 0
+ `chromatic_number=4` intersect `is_tree=1` = 0
+ `chromatic_number=4` intersect `k_max_clique=6` = 0
+ `chromatic_number=4` intersect `k_max_clique=7` = 0
+ `chromatic_number=4` intersect `maximal_independent_edge_set=1` = 0
+ `chromatic_number=5` intersect `automorphism_group_n=5040` = 0
+ `chromatic_number=5` intersect `circumference=0` = 0
+ `chromatic_number=5` intersect `circumference=3` = 0
+ `chromatic_number=5` intersect `circumference=4` = 0
+ `chromatic_number=5` intersect `girth=0` = 0
+ `chromatic_number=5` intersect `girth=4` = 0
+ `chromatic_number=5` intersect `girth=5` = 0
+ `chromatic_number=5` intersect `girth=6` = 0
+ `chromatic_number=5` intersect `girth=7` = 0
+ `chromatic_number=5` intersect `is_k_regular=2` = 0
+ `chromatic_number=5` intersect `is_k_regular=3` = 0
+ `chromatic_number=5` intersect `is_bipartite=1` = 0
+ `chromatic_number=5` intersect `is_subgraph_free_K3=1` = 0
+ `chromatic_number=5` intersect `is_subgraph_free_C4=1` = 0
+ `chromatic_number=5` intersect `is_tree=1` = 0
+ `chromatic_number=5` intersect `k_max_clique=2` = 0
+ `chromatic_number=5` intersect `k_max_clique=7` = 0
+ `chromatic_number=5` intersect `is_subgraph_free_bull=1` = 0
+ `chromatic_number=5` intersect `is_subgraph_free_diamond=1` = 0
+ `chromatic_number=5` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `chromatic_number=5` intersect `maximal_independent_edge_set=1` = 0
+ `chromatic_number=6` intersect `automorphism_group_n=5040` = 0
+ `chromatic_number=6` intersect `diameter=6` = 0
+ `chromatic_number=6` intersect `circumference=0` = 0
+ `chromatic_number=6` intersect `circumference=3` = 0
+ `chromatic_number=6` intersect `circumference=4` = 0
+ `chromatic_number=6` intersect `circumference=5` = 0
+ `chromatic_number=6` intersect `girth=0` = 0
+ `chromatic_number=6` intersect `girth=4` = 0
+ `chromatic_number=6` intersect `girth=5` = 0
+ `chromatic_number=6` intersect `girth=6` = 0
+ `chromatic_number=6` intersect `girth=7` = 0
+ `chromatic_number=6` intersect `is_k_regular=2` = 0
+ `chromatic_number=6` intersect `is_k_regular=3` = 0
+ `chromatic_number=6` intersect `is_k_regular=4` = 0
+ `chromatic_number=6` intersect `is_k_regular=6` = 0
+ `chromatic_number=6` intersect `is_planar=1` = 0
+ `chromatic_number=6` intersect `is_bipartite=1` = 0
+ `chromatic_number=6` intersect `n_articulation_points=5` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_K3=1` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_K4=1` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_C4=1` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_C5=1` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_C6=1` = 0
+ `chromatic_number=6` intersect `is_tree=1` = 0
+ `chromatic_number=6` intersect `k_max_clique=2` = 0
+ `chromatic_number=6` intersect `k_max_clique=3` = 0
+ `chromatic_number=6` intersect `k_max_clique=7` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_bull=1` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_bowtie=1` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_diamond=1` = 0
+ `chromatic_number=6` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `chromatic_number=6` intersect `maximal_independent_vertex_set=6` = 0
+ `chromatic_number=6` intersect `maximal_independent_edge_set=1` = 0
+ `chromatic_number=6` intersect `maximal_independent_edge_set=2` = 0
+ `chromatic_number=7` intersect `automorphism_group_n=10` = 0
+ `chromatic_number=7` intersect `automorphism_group_n=14` = 0
+ `chromatic_number=7` intersect `automorphism_group_n=20` = 0
+ `chromatic_number=7` intersect `diameter=5` = 0
+ `chromatic_number=7` intersect `diameter=6` = 0
+ `chromatic_number=7` intersect `circumference=0` = 0
+ `chromatic_number=7` intersect `circumference=3` = 0
+ `chromatic_number=7` intersect `circumference=4` = 0
+ `chromatic_number=7` intersect `circumference=5` = 0
+ `chromatic_number=7` intersect `circumference=6` = 0
+ `chromatic_number=7` intersect `girth=0` = 0
+ `chromatic_number=7` intersect `girth=4` = 0
+ `chromatic_number=7` intersect `girth=5` = 0
+ `chromatic_number=7` intersect `girth=6` = 0
+ `chromatic_number=7` intersect `girth=7` = 0
+ `chromatic_number=7` intersect `is_k_regular=2` = 0
+ `chromatic_number=7` intersect `is_k_regular=3` = 0
+ `chromatic_number=7` intersect `is_k_regular=4` = 0
+ `chromatic_number=7` intersect `radius=3` = 0
+ `chromatic_number=7` intersect `is_planar=1` = 0
+ `chromatic_number=7` intersect `is_bipartite=1` = 0
+ `chromatic_number=7` intersect `n_articulation_points=4` = 0
+ `chromatic_number=7` intersect `n_articulation_points=5` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_K3=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_K4=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_K5=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_C4=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_C5=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_C6=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_C7=1` = 0
+ `chromatic_number=7` intersect `is_tree=1` = 0
+ `chromatic_number=7` intersect `k_max_clique=2` = 0
+ `chromatic_number=7` intersect `k_max_clique=3` = 0
+ `chromatic_number=7` intersect `k_max_clique=4` = 0
+ `chromatic_number=7` intersect `k_max_clique=5` = 0
+ `chromatic_number=7` intersect `is_real_spectrum=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_bull=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_bowtie=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_diamond=1` = 0
+ `chromatic_number=7` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `chromatic_number=7` intersect `maximal_independent_vertex_set=5` = 0
+ `chromatic_number=7` intersect `maximal_independent_vertex_set=6` = 0
+ `chromatic_number=7` intersect `maximal_independent_edge_set=1` = 0
+ `chromatic_number=7` intersect `maximal_independent_edge_set=2` = 0
+ `diameter=1` intersect `automorphism_group_n=1` = 0
+ `diameter=1` intersect `automorphism_group_n=2` = 0
+ `diameter=1` intersect `automorphism_group_n=4` = 0
+ `diameter=1` intersect `automorphism_group_n=8` = 0
+ `diameter=1` intersect `automorphism_group_n=10` = 0
+ `diameter=1` intersect `automorphism_group_n=12` = 0
+ `diameter=1` intersect `automorphism_group_n=14` = 0
+ `diameter=1` intersect `automorphism_group_n=16` = 0
+ `diameter=1` intersect `automorphism_group_n=20` = 0
+ `diameter=1` intersect `automorphism_group_n=36` = 0
+ `diameter=1` intersect `automorphism_group_n=48` = 0
+ `diameter=1` intersect `automorphism_group_n=72` = 0
+ `diameter=1` intersect `automorphism_group_n=144` = 0
+ `diameter=1` intersect `automorphism_group_n=240` = 0
+ `diameter=1` intersect `chromatic_number=4` = 0
+ `diameter=1` intersect `circumference=4` = 0
+ `diameter=1` intersect `girth=4` = 0
+ `diameter=1` intersect `girth=5` = 0
+ `diameter=1` intersect `girth=6` = 0
+ `diameter=1` intersect `girth=7` = 0
+ `diameter=1` intersect `is_k_regular=3` = 0
+ `diameter=1` intersect `is_strongly_regular=0` = 0
+ `diameter=1` intersect `radius=2` = 0
+ `diameter=1` intersect `radius=3` = 0
+ `diameter=1` intersect `is_distance_regular=0` = 0
+ `diameter=1` intersect `is_bipartite=1` = 0
+ `diameter=1` intersect `n_articulation_points=1` = 0
+ `diameter=1` intersect `n_articulation_points=2` = 0
+ `diameter=1` intersect `n_articulation_points=3` = 0
+ `diameter=1` intersect `n_articulation_points=4` = 0
+ `diameter=1` intersect `n_articulation_points=5` = 0
+ `diameter=1` intersect `is_subgraph_free_K3=1` = 0
+ `diameter=1` intersect `is_integral=0` = 0
+ `diameter=1` intersect `edge_connectivity=1` = 0
+ `diameter=1` intersect `is_chordal=0` = 0
+ `diameter=1` intersect `k_max_clique=2` = 0
+ `diameter=1` intersect `is_real_spectrum=1` = 0
+ `diameter=1` intersect `is_hamiltonian=0` = 0
+ `diameter=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `diameter=1` intersect `maximal_independent_vertex_set=3` = 0
+ `diameter=1` intersect `maximal_independent_vertex_set=4` = 0
+ `diameter=1` intersect `maximal_independent_vertex_set=5` = 0
+ `diameter=1` intersect `maximal_independent_vertex_set=6` = 0
+ `diameter=2` intersect `girth=7` = 0
+ `diameter=2` intersect `radius=3` = 0
+ `diameter=2` intersect `n_articulation_points=2` = 0
+ `diameter=2` intersect `n_articulation_points=3` = 0
+ `diameter=2` intersect `n_articulation_points=4` = 0
+ `diameter=2` intersect `n_articulation_points=5` = 0
+ `diameter=2` intersect `maximal_independent_vertex_set=1` = 0
+ `diameter=3` intersect `is_k_regular=6` = 0
+ `diameter=3` intersect `is_strongly_regular=1` = 0
+ `diameter=3` intersect `radius=1` = 0
+ `diameter=3` intersect `vertex_connectivity>4` = 0
+ `diameter=3` intersect `vertex_connectivity>5` = 0
+ `diameter=3` intersect `edge_connectivity=5` = 0
+ `diameter=3` intersect `edge_connectivity=6` = 0
+ `diameter=3` intersect `maximal_independent_edge_set=1` = 0
+ `diameter=4` intersect `automorphism_group_n=14` = 0
+ `diameter=4` intersect `automorphism_group_n=5040` = 0
+ `diameter=4` intersect `is_k_regular=4` = 0
+ `diameter=4` intersect `is_k_regular=6` = 0
+ `diameter=4` intersect `is_strongly_regular=1` = 0
+ `diameter=4` intersect `radius=1` = 0
+ `diameter=4` intersect `vertex_connectivity>2` = 0
+ `diameter=4` intersect `vertex_connectivity>3` = 0
+ `diameter=4` intersect `vertex_connectivity>4` = 0
+ `diameter=4` intersect `vertex_connectivity>5` = 0
+ `diameter=4` intersect `edge_connectivity=4` = 0
+ `diameter=4` intersect `edge_connectivity=5` = 0
+ `diameter=4` intersect `edge_connectivity=6` = 0
+ `diameter=4` intersect `maximal_independent_vertex_set=1` = 0
+ `diameter=4` intersect `maximal_independent_edge_set=1` = 0
+ `diameter=5` intersect `automorphism_group_n=14` = 0
+ `diameter=5` intersect `automorphism_group_n=144` = 0
+ `diameter=5` intersect `automorphism_group_n=240` = 0
+ `diameter=5` intersect `automorphism_group_n=720` = 0
+ `diameter=5` intersect `automorphism_group_n=5040` = 0
+ `diameter=5` intersect `chromatic_number=7` = 0
+ `diameter=5` intersect `is_k_regular=4` = 0
+ `diameter=5` intersect `is_k_regular=6` = 0
+ `diameter=5` intersect `is_strongly_regular=1` = 0
+ `diameter=5` intersect `radius=1` = 0
+ `diameter=5` intersect `radius=2` = 0
+ `diameter=5` intersect `is_integral=1` = 0
+ `diameter=5` intersect `vertex_connectivity>2` = 0
+ `diameter=5` intersect `vertex_connectivity>3` = 0
+ `diameter=5` intersect `vertex_connectivity>4` = 0
+ `diameter=5` intersect `vertex_connectivity>5` = 0
+ `diameter=5` intersect `edge_connectivity=3` = 0
+ `diameter=5` intersect `edge_connectivity=4` = 0
+ `diameter=5` intersect `edge_connectivity=5` = 0
+ `diameter=5` intersect `edge_connectivity=6` = 0
+ `diameter=5` intersect `k_max_clique=7` = 0
+ `diameter=5` intersect `maximal_independent_vertex_set=1` = 0
+ `diameter=5` intersect `maximal_independent_vertex_set=2` = 0
+ `diameter=5` intersect `maximal_independent_edge_set=2` = 0
+ `diameter=6` intersect `automorphism_group_n=10` = 0
+ `diameter=6` intersect `automorphism_group_n=14` = 0
+ `diameter=6` intersect `automorphism_group_n=20` = 0
+ `diameter=6` intersect `automorphism_group_n=36` = 0
+ `diameter=6` intersect `automorphism_group_n=72` = 0
+ `diameter=6` intersect `automorphism_group_n=120` = 0
+ `diameter=6` intersect `automorphism_group_n=144` = 0
+ `diameter=6` intersect `automorphism_group_n=240` = 0
+ `diameter=6` intersect `automorphism_group_n=720` = 0
+ `diameter=6` intersect `automorphism_group_n=5040` = 0
+ `diameter=6` intersect `chromatic_number=6` = 0
+ `diameter=6` intersect `chromatic_number=7` = 0
+ `diameter=6` intersect `is_k_regular=2` = 0
+ `diameter=6` intersect `is_k_regular=3` = 0
+ `diameter=6` intersect `is_k_regular=4` = 0
+ `diameter=6` intersect `is_k_regular=6` = 0
+ `diameter=6` intersect `is_strongly_regular=1` = 0
+ `diameter=6` intersect `radius=1` = 0
+ `diameter=6` intersect `radius=2` = 0
+ `diameter=6` intersect `is_distance_regular=1` = 0
+ `diameter=6` intersect `n_articulation_points=0` = 0
+ `diameter=6` intersect `n_articulation_points=1` = 0
+ `diameter=6` intersect `is_integral=1` = 0
+ `diameter=6` intersect `vertex_connectivity>1` = 0
+ `diameter=6` intersect `vertex_connectivity>2` = 0
+ `diameter=6` intersect `vertex_connectivity>3` = 0
+ `diameter=6` intersect `vertex_connectivity>4` = 0
+ `diameter=6` intersect `vertex_connectivity>5` = 0
+ `diameter=6` intersect `edge_connectivity=3` = 0
+ `diameter=6` intersect `edge_connectivity=4` = 0
+ `diameter=6` intersect `edge_connectivity=5` = 0
+ `diameter=6` intersect `edge_connectivity=6` = 0
+ `diameter=6` intersect `k_max_clique=6` = 0
+ `diameter=6` intersect `k_max_clique=7` = 0
+ `diameter=6` intersect `is_hamiltonian=1` = 0
+ `diameter=6` intersect `maximal_independent_vertex_set=1` = 0
+ `diameter=6` intersect `maximal_independent_vertex_set=2` = 0
+ `diameter=6` intersect `maximal_independent_edge_set=1` = 0
+ `diameter=6` intersect `maximal_independent_edge_set=2` = 0
+ `circumference=0` intersect `automorphism_group_n=10` = 0
+ `circumference=0` intersect `automorphism_group_n=14` = 0
+ `circumference=0` intersect `automorphism_group_n=20` = 0
+ `circumference=0` intersect `chromatic_number=3` = 0
+ `circumference=0` intersect `chromatic_number=4` = 0
+ `circumference=0` intersect `chromatic_number=5` = 0
+ `circumference=0` intersect `chromatic_number=6` = 0
+ `circumference=0` intersect `chromatic_number=7` = 0
+ `circumference=0` intersect `girth=3` = 0
+ `circumference=0` intersect `girth=4` = 0
+ `circumference=0` intersect `girth=5` = 0
+ `circumference=0` intersect `girth=6` = 0
+ `circumference=0` intersect `girth=7` = 0
+ `circumference=0` intersect `is_k_regular=2` = 0
+ `circumference=0` intersect `is_k_regular=3` = 0
+ `circumference=0` intersect `is_k_regular=4` = 0
+ `circumference=0` intersect `is_k_regular=6` = 0
+ `circumference=0` intersect `is_eulerian=1` = 0
+ `circumference=0` intersect `is_subgraph_free_K5=0` = 0
+ `circumference=0` intersect `is_subgraph_free_C7=0` = 0
+ `circumference=0` intersect `vertex_connectivity>3` = 0
+ `circumference=0` intersect `vertex_connectivity>4` = 0
+ `circumference=0` intersect `vertex_connectivity>5` = 0
+ `circumference=0` intersect `edge_connectivity=2` = 0
+ `circumference=0` intersect `edge_connectivity=4` = 0
+ `circumference=0` intersect `edge_connectivity=5` = 0
+ `circumference=0` intersect `edge_connectivity=6` = 0
+ `circumference=0` intersect `is_tree=0` = 0
+ `circumference=0` intersect `k_max_clique=5` = 0
+ `circumference=0` intersect `k_max_clique=6` = 0
+ `circumference=0` intersect `k_max_clique=7` = 0
+ `circumference=0` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `circumference=0` intersect `maximal_independent_vertex_set=1` = 0
+ `circumference=3` intersect `automorphism_group_n=10` = 0
+ `circumference=3` intersect `automorphism_group_n=14` = 0
+ `circumference=3` intersect `automorphism_group_n=20` = 0
+ `circumference=3` intersect `automorphism_group_n=5040` = 0
+ `circumference=3` intersect `chromatic_number=2` = 0
+ `circumference=3` intersect `chromatic_number=4` = 0
+ `circumference=3` intersect `chromatic_number=5` = 0
+ `circumference=3` intersect `chromatic_number=6` = 0
+ `circumference=3` intersect `chromatic_number=7` = 0
+ `circumference=3` intersect `girth=0` = 0
+ `circumference=3` intersect `girth=4` = 0
+ `circumference=3` intersect `girth=5` = 0
+ `circumference=3` intersect `girth=6` = 0
+ `circumference=3` intersect `girth=7` = 0
+ `circumference=3` intersect `is_k_regular=3` = 0
+ `circumference=3` intersect `is_k_regular=4` = 0
+ `circumference=3` intersect `is_k_regular=6` = 0
+ `circumference=3` intersect `is_planar=0` = 0
+ `circumference=3` intersect `is_subgraph_free_K5=0` = 0
+ `circumference=3` intersect `is_subgraph_free_C7=0` = 0
+ `circumference=3` intersect `vertex_connectivity>2` = 0
+ `circumference=3` intersect `vertex_connectivity>3` = 0
+ `circumference=3` intersect `vertex_connectivity>4` = 0
+ `circumference=3` intersect `vertex_connectivity>5` = 0
+ `circumference=3` intersect `edge_connectivity=3` = 0
+ `circumference=3` intersect `edge_connectivity=4` = 0
+ `circumference=3` intersect `edge_connectivity=5` = 0
+ `circumference=3` intersect `edge_connectivity=6` = 0
+ `circumference=3` intersect `is_tree=1` = 0
+ `circumference=3` intersect `k_max_clique=5` = 0
+ `circumference=3` intersect `k_max_clique=6` = 0
+ `circumference=3` intersect `k_max_clique=7` = 0
+ `circumference=3` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `circumference=4` intersect `automorphism_group_n=10` = 0
+ `circumference=4` intersect `automorphism_group_n=14` = 0
+ `circumference=4` intersect `automorphism_group_n=20` = 0
+ `circumference=4` intersect `automorphism_group_n=5040` = 0
+ `circumference=4` intersect `chromatic_number=5` = 0
+ `circumference=4` intersect `chromatic_number=6` = 0
+ `circumference=4` intersect `chromatic_number=7` = 0
+ `circumference=4` intersect `diameter=1` = 0
+ `circumference=4` intersect `girth=0` = 0
+ `circumference=4` intersect `girth=5` = 0
+ `circumference=4` intersect `girth=6` = 0
+ `circumference=4` intersect `girth=7` = 0
+ `circumference=4` intersect `is_k_regular=4` = 0
+ `circumference=4` intersect `is_k_regular=6` = 0
+ `circumference=4` intersect `is_planar=0` = 0
+ `circumference=4` intersect `is_subgraph_free_K5=0` = 0
+ `circumference=4` intersect `vertex_connectivity>2` = 0
+ `circumference=4` intersect `vertex_connectivity>3` = 0
+ `circumference=4` intersect `vertex_connectivity>4` = 0
+ `circumference=4` intersect `vertex_connectivity>5` = 0
+ `circumference=4` intersect `edge_connectivity=4` = 0
+ `circumference=4` intersect `edge_connectivity=5` = 0
+ `circumference=4` intersect `edge_connectivity=6` = 0
+ `circumference=4` intersect `is_tree=1` = 0
+ `circumference=4` intersect `k_max_clique=5` = 0
+ `circumference=4` intersect `k_max_clique=6` = 0
+ `circumference=4` intersect `k_max_clique=7` = 0
+ `circumference=4` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `circumference=4` intersect `maximal_independent_edge_set=1` = 0
+ `circumference=5` intersect `automorphism_group_n=14` = 0
+ `circumference=5` intersect `automorphism_group_n=20` = 0
+ `circumference=5` intersect `automorphism_group_n=5040` = 0
+ `circumference=5` intersect `chromatic_number=6` = 0
+ `circumference=5` intersect `chromatic_number=7` = 0
+ `circumference=5` intersect `girth=0` = 0
+ `circumference=5` intersect `girth=6` = 0
+ `circumference=5` intersect `girth=7` = 0
+ `circumference=5` intersect `is_k_regular=3` = 0
+ `circumference=5` intersect `is_k_regular=6` = 0
+ `circumference=5` intersect `vertex_connectivity>4` = 0
+ `circumference=5` intersect `vertex_connectivity>5` = 0
+ `circumference=5` intersect `edge_connectivity=5` = 0
+ `circumference=5` intersect `edge_connectivity=6` = 0
+ `circumference=5` intersect `is_tree=1` = 0
+ `circumference=5` intersect `k_max_clique=6` = 0
+ `circumference=5` intersect `k_max_clique=7` = 0
+ `circumference=5` intersect `maximal_independent_edge_set=1` = 0
+ `circumference=6` intersect `automorphism_group_n=5040` = 0
+ `circumference=6` intersect `chromatic_number=7` = 0
+ `circumference=6` intersect `girth=0` = 0
+ `circumference=6` intersect `girth=7` = 0
+ `circumference=6` intersect `is_k_regular=6` = 0
+ `circumference=6` intersect `vertex_connectivity>5` = 0
+ `circumference=6` intersect `edge_connectivity=6` = 0
+ `circumference=6` intersect `is_tree=1` = 0
+ `circumference=6` intersect `k_max_clique=7` = 0
+ `circumference=6` intersect `maximal_independent_edge_set=1` = 0
+ `circumference=7` intersect `girth=0` = 0
+ `circumference=7` intersect `is_k_regular=3` = 0
+ `circumference=7` intersect `is_tree=1` = 0
+ `circumference=7` intersect `maximal_independent_edge_set=1` = 0
+ `girth=0` intersect `automorphism_group_n=10` = 0
+ `girth=0` intersect `automorphism_group_n=14` = 0
+ `girth=0` intersect `automorphism_group_n=20` = 0
+ `girth=0` intersect `chromatic_number=3` = 0
+ `girth=0` intersect `chromatic_number=4` = 0
+ `girth=0` intersect `chromatic_number=5` = 0
+ `girth=0` intersect `chromatic_number=6` = 0
+ `girth=0` intersect `chromatic_number=7` = 0
+ `girth=0` intersect `circumference=3` = 0
+ `girth=0` intersect `circumference=4` = 0
+ `girth=0` intersect `circumference=5` = 0
+ `girth=0` intersect `circumference=6` = 0
+ `girth=0` intersect `circumference=7` = 0
+ `girth=0` intersect `is_k_regular=2` = 0
+ `girth=0` intersect `is_k_regular=3` = 0
+ `girth=0` intersect `is_k_regular=4` = 0
+ `girth=0` intersect `is_k_regular=6` = 0
+ `girth=0` intersect `is_eulerian=1` = 0
+ `girth=0` intersect `is_subgraph_free_K5=0` = 0
+ `girth=0` intersect `is_subgraph_free_C7=0` = 0
+ `girth=0` intersect `vertex_connectivity>3` = 0
+ `girth=0` intersect `vertex_connectivity>4` = 0
+ `girth=0` intersect `vertex_connectivity>5` = 0
+ `girth=0` intersect `edge_connectivity=2` = 0
+ `girth=0` intersect `edge_connectivity=4` = 0
+ `girth=0` intersect `edge_connectivity=5` = 0
+ `girth=0` intersect `edge_connectivity=6` = 0
+ `girth=0` intersect `is_tree=0` = 0
+ `girth=0` intersect `k_max_clique=5` = 0
+ `girth=0` intersect `k_max_clique=6` = 0
+ `girth=0` intersect `k_max_clique=7` = 0
+ `girth=0` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `girth=0` intersect `maximal_independent_vertex_set=1` = 0
+ `girth=3` intersect `chromatic_number=2` = 0
+ `girth=3` intersect `circumference=0` = 0
+ `girth=3` intersect `is_tree=1` = 0
+ `girth=4` intersect `chromatic_number=5` = 0
+ `girth=4` intersect `chromatic_number=6` = 0
+ `girth=4` intersect `chromatic_number=7` = 0
+ `girth=4` intersect `diameter=1` = 0
+ `girth=4` intersect `circumference=0` = 0
+ `girth=4` intersect `circumference=3` = 0
+ `girth=4` intersect `is_k_regular=6` = 0
+ `girth=4` intersect `is_subgraph_free_K5=0` = 0
+ `girth=4` intersect `vertex_connectivity>5` = 0
+ `girth=4` intersect `edge_connectivity=6` = 0
+ `girth=4` intersect `is_tree=1` = 0
+ `girth=4` intersect `k_max_clique=5` = 0
+ `girth=4` intersect `k_max_clique=6` = 0
+ `girth=4` intersect `k_max_clique=7` = 0
+ `girth=4` intersect `maximal_independent_vertex_set=1` = 0
+ `girth=4` intersect `maximal_independent_edge_set=1` = 0
+ `girth=5` intersect `automorphism_group_n=14` = 0
+ `girth=5` intersect `automorphism_group_n=20` = 0
+ `girth=5` intersect `automorphism_group_n=72` = 0
+ `girth=5` intersect `automorphism_group_n=144` = 0
+ `girth=5` intersect `automorphism_group_n=720` = 0
+ `girth=5` intersect `automorphism_group_n=5040` = 0
+ `girth=5` intersect `chromatic_number=2` = 0
+ `girth=5` intersect `chromatic_number=4` = 0
+ `girth=5` intersect `chromatic_number=5` = 0
+ `girth=5` intersect `chromatic_number=6` = 0
+ `girth=5` intersect `chromatic_number=7` = 0
+ `girth=5` intersect `diameter=1` = 0
+ `girth=5` intersect `circumference=0` = 0
+ `girth=5` intersect `circumference=3` = 0
+ `girth=5` intersect `circumference=4` = 0
+ `girth=5` intersect `is_k_regular=4` = 0
+ `girth=5` intersect `is_k_regular=6` = 0
+ `girth=5` intersect `radius=1` = 0
+ `girth=5` intersect `is_subgraph_free_K4=0` = 0
+ `girth=5` intersect `is_subgraph_free_K5=0` = 0
+ `girth=5` intersect `vertex_connectivity>3` = 0
+ `girth=5` intersect `vertex_connectivity>4` = 0
+ `girth=5` intersect `vertex_connectivity>5` = 0
+ `girth=5` intersect `edge_connectivity=4` = 0
+ `girth=5` intersect `edge_connectivity=5` = 0
+ `girth=5` intersect `edge_connectivity=6` = 0
+ `girth=5` intersect `is_tree=1` = 0
+ `girth=5` intersect `k_max_clique=4` = 0
+ `girth=5` intersect `k_max_clique=5` = 0
+ `girth=5` intersect `k_max_clique=6` = 0
+ `girth=5` intersect `k_max_clique=7` = 0
+ `girth=5` intersect `maximal_independent_vertex_set=1` = 0
+ `girth=5` intersect `maximal_independent_edge_set=1` = 0
+ `girth=6` intersect `automorphism_group_n=10` = 0
+ `girth=6` intersect `automorphism_group_n=14` = 0
+ `girth=6` intersect `automorphism_group_n=20` = 0
+ `girth=6` intersect `automorphism_group_n=36` = 0
+ `girth=6` intersect `automorphism_group_n=72` = 0
+ `girth=6` intersect `automorphism_group_n=120` = 0
+ `girth=6` intersect `automorphism_group_n=144` = 0
+ `girth=6` intersect `automorphism_group_n=720` = 0
+ `girth=6` intersect `automorphism_group_n=5040` = 0
+ `girth=6` intersect `chromatic_number=4` = 0
+ `girth=6` intersect `chromatic_number=5` = 0
+ `girth=6` intersect `chromatic_number=6` = 0
+ `girth=6` intersect `chromatic_number=7` = 0
+ `girth=6` intersect `diameter=1` = 0
+ `girth=6` intersect `circumference=0` = 0
+ `girth=6` intersect `circumference=3` = 0
+ `girth=6` intersect `circumference=4` = 0
+ `girth=6` intersect `circumference=5` = 0
+ `girth=6` intersect `is_k_regular=3` = 0
+ `girth=6` intersect `is_k_regular=4` = 0
+ `girth=6` intersect `is_k_regular=6` = 0
+ `girth=6` intersect `is_strongly_regular=1` = 0
+ `girth=6` intersect `radius=2` = 0
+ `girth=6` intersect `n_articulation_points=5` = 0
+ `girth=6` intersect `is_subgraph_free_K4=0` = 0
+ `girth=6` intersect `is_subgraph_free_K5=0` = 0
+ `girth=6` intersect `vertex_connectivity>2` = 0
+ `girth=6` intersect `vertex_connectivity>3` = 0
+ `girth=6` intersect `vertex_connectivity>4` = 0
+ `girth=6` intersect `vertex_connectivity>5` = 0
+ `girth=6` intersect `edge_connectivity=3` = 0
+ `girth=6` intersect `edge_connectivity=4` = 0
+ `girth=6` intersect `edge_connectivity=5` = 0
+ `girth=6` intersect `edge_connectivity=6` = 0
+ `girth=6` intersect `is_tree=1` = 0
+ `girth=6` intersect `is_chordal=1` = 0
+ `girth=6` intersect `k_max_clique=4` = 0
+ `girth=6` intersect `k_max_clique=5` = 0
+ `girth=6` intersect `k_max_clique=6` = 0
+ `girth=6` intersect `k_max_clique=7` = 0
+ `girth=6` intersect `maximal_independent_vertex_set=1` = 0
+ `girth=6` intersect `maximal_independent_vertex_set=2` = 0
+ `girth=6` intersect `maximal_independent_edge_set=1` = 0
+ `girth=6` intersect `maximal_independent_edge_set=2` = 0
+ `girth=7` intersect `automorphism_group_n=6` = 0
+ `girth=7` intersect `automorphism_group_n=8` = 0
+ `girth=7` intersect `automorphism_group_n=10` = 0
+ `girth=7` intersect `automorphism_group_n=14` = 0
+ `girth=7` intersect `automorphism_group_n=16` = 0
+ `girth=7` intersect `automorphism_group_n=20` = 0
+ `girth=7` intersect `automorphism_group_n=24` = 0
+ `girth=7` intersect `automorphism_group_n=36` = 0
+ `girth=7` intersect `automorphism_group_n=48` = 0
+ `girth=7` intersect `automorphism_group_n=72` = 0
+ `girth=7` intersect `automorphism_group_n=120` = 0
+ `girth=7` intersect `automorphism_group_n=144` = 0
+ `girth=7` intersect `automorphism_group_n=240` = 0
+ `girth=7` intersect `automorphism_group_n=720` = 0
+ `girth=7` intersect `automorphism_group_n=5040` = 0
+ `girth=7` intersect `chromatic_number=2` = 0
+ `girth=7` intersect `chromatic_number=4` = 0
+ `girth=7` intersect `chromatic_number=5` = 0
+ `girth=7` intersect `chromatic_number=6` = 0
+ `girth=7` intersect `chromatic_number=7` = 0
+ `girth=7` intersect `diameter=1` = 0
+ `girth=7` intersect `diameter=2` = 0
+ `girth=7` intersect `circumference=0` = 0
+ `girth=7` intersect `circumference=3` = 0
+ `girth=7` intersect `circumference=4` = 0
+ `girth=7` intersect `circumference=5` = 0
+ `girth=7` intersect `circumference=6` = 0
+ `girth=7` intersect `is_k_regular=3` = 0
+ `girth=7` intersect `is_k_regular=4` = 0
+ `girth=7` intersect `is_k_regular=6` = 0
+ `girth=7` intersect `is_strongly_regular=1` = 0
+ `girth=7` intersect `radius=1` = 0
+ `girth=7` intersect `is_eulerian=1` = 0
+ `girth=7` intersect `is_distance_regular=1` = 0
+ `girth=7` intersect `is_planar=0` = 0
+ `girth=7` intersect `n_articulation_points=4` = 0
+ `girth=7` intersect `n_articulation_points=5` = 0
+ `girth=7` intersect `is_subgraph_free_K3=0` = 0
+ `girth=7` intersect `is_subgraph_free_K4=0` = 0
+ `girth=7` intersect `is_subgraph_free_K5=0` = 0
+ `girth=7` intersect `is_subgraph_free_C5=0` = 0
+ `girth=7` intersect `is_integral=1` = 0
+ `girth=7` intersect `vertex_connectivity>2` = 0
+ `girth=7` intersect `vertex_connectivity>3` = 0
+ `girth=7` intersect `vertex_connectivity>4` = 0
+ `girth=7` intersect `vertex_connectivity>5` = 0
+ `girth=7` intersect `edge_connectivity=3` = 0
+ `girth=7` intersect `edge_connectivity=4` = 0
+ `girth=7` intersect `edge_connectivity=5` = 0
+ `girth=7` intersect `edge_connectivity=6` = 0
+ `girth=7` intersect `is_tree=1` = 0
+ `girth=7` intersect `is_chordal=1` = 0
+ `girth=7` intersect `k_max_clique=3` = 0
+ `girth=7` intersect `k_max_clique=4` = 0
+ `girth=7` intersect `k_max_clique=5` = 0
+ `girth=7` intersect `k_max_clique=6` = 0
+ `girth=7` intersect `k_max_clique=7` = 0
+ `girth=7` intersect `is_subgraph_free_bull=0` = 0
+ `girth=7` intersect `is_subgraph_free_bowtie=0` = 0
+ `girth=7` intersect `is_subgraph_free_diamond=0` = 0
+ `girth=7` intersect `is_subgraph_free_open_bowtie=0` = 0
+ `girth=7` intersect `is_hamiltonian=1` = 0
+ `girth=7` intersect `has_fractional_duality_gap_vertex_chromatic=0` = 0
+ `girth=7` intersect `maximal_independent_vertex_set=1` = 0
+ `girth=7` intersect `maximal_independent_vertex_set=2` = 0
+ `girth=7` intersect `maximal_independent_edge_set=1` = 0
+ `girth=7` intersect `maximal_independent_edge_set=2` = 0
+ `is_k_regular=0` intersect `maximal_independent_vertex_set=1` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=2` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=4` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=14` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=24` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=36` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=48` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=72` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=120` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=144` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=240` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=720` = 0
+ `is_k_regular=2` intersect `automorphism_group_n=5040` = 0
+ `is_k_regular=2` intersect `chromatic_number=4` = 0
+ `is_k_regular=2` intersect `chromatic_number=5` = 0
+ `is_k_regular=2` intersect `chromatic_number=6` = 0
+ `is_k_regular=2` intersect `chromatic_number=7` = 0
+ `is_k_regular=2` intersect `diameter=6` = 0
+ `is_k_regular=2` intersect `circumference=0` = 0
+ `is_k_regular=2` intersect `girth=0` = 0
+ `is_k_regular=2` intersect `is_planar=0` = 0
+ `is_k_regular=2` intersect `n_articulation_points=2` = 0
+ `is_k_regular=2` intersect `n_articulation_points=3` = 0
+ `is_k_regular=2` intersect `n_articulation_points=4` = 0
+ `is_k_regular=2` intersect `n_articulation_points=5` = 0
+ `is_k_regular=2` intersect `is_subgraph_free_K4=0` = 0
+ `is_k_regular=2` intersect `is_subgraph_free_K5=0` = 0
+ `is_k_regular=2` intersect `is_subgraph_free_C7=0` = 0
+ `is_k_regular=2` intersect `vertex_connectivity>2` = 0
+ `is_k_regular=2` intersect `vertex_connectivity>3` = 0
+ `is_k_regular=2` intersect `vertex_connectivity>4` = 0
+ `is_k_regular=2` intersect `vertex_connectivity>5` = 0
+ `is_k_regular=2` intersect `edge_connectivity=3` = 0
+ `is_k_regular=2` intersect `edge_connectivity=4` = 0
+ `is_k_regular=2` intersect `edge_connectivity=5` = 0
+ `is_k_regular=2` intersect `edge_connectivity=6` = 0
+ `is_k_regular=2` intersect `is_tree=1` = 0
+ `is_k_regular=2` intersect `k_max_clique=4` = 0
+ `is_k_regular=2` intersect `k_max_clique=5` = 0
+ `is_k_regular=2` intersect `k_max_clique=6` = 0
+ `is_k_regular=2` intersect `k_max_clique=7` = 0
+ `is_k_regular=2` intersect `is_subgraph_free_bull=0` = 0
+ `is_k_regular=2` intersect `is_subgraph_free_bowtie=0` = 0
+ `is_k_regular=2` intersect `is_subgraph_free_diamond=0` = 0
+ `is_k_regular=2` intersect `is_subgraph_free_open_bowtie=0` = 0
+ `is_k_regular=2` intersect `maximal_independent_vertex_set=6` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=1` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=10` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=14` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=24` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=36` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=144` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=240` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=720` = 0
+ `is_k_regular=3` intersect `automorphism_group_n=5040` = 0
+ `is_k_regular=3` intersect `chromatic_number=5` = 0
+ `is_k_regular=3` intersect `chromatic_number=6` = 0
+ `is_k_regular=3` intersect `chromatic_number=7` = 0
+ `is_k_regular=3` intersect `diameter=1` = 0
+ `is_k_regular=3` intersect `diameter=6` = 0
+ `is_k_regular=3` intersect `circumference=0` = 0
+ `is_k_regular=3` intersect `circumference=3` = 0
+ `is_k_regular=3` intersect `circumference=5` = 0
+ `is_k_regular=3` intersect `circumference=7` = 0
+ `is_k_regular=3` intersect `girth=0` = 0
+ `is_k_regular=3` intersect `girth=6` = 0
+ `is_k_regular=3` intersect `girth=7` = 0
+ `is_k_regular=3` intersect `radius=1` = 0
+ `is_k_regular=3` intersect `is_eulerian=1` = 0
+ `is_k_regular=3` intersect `n_articulation_points=1` = 0
+ `is_k_regular=3` intersect `n_articulation_points=3` = 0
+ `is_k_regular=3` intersect `n_articulation_points=4` = 0
+ `is_k_regular=3` intersect `n_articulation_points=5` = 0
+ `is_k_regular=3` intersect `is_subgraph_free_K4=0` = 0
+ `is_k_regular=3` intersect `is_subgraph_free_K5=0` = 0
+ `is_k_regular=3` intersect `vertex_connectivity>3` = 0
+ `is_k_regular=3` intersect `vertex_connectivity>4` = 0
+ `is_k_regular=3` intersect `vertex_connectivity>5` = 0
+ `is_k_regular=3` intersect `edge_connectivity=4` = 0
+ `is_k_regular=3` intersect `edge_connectivity=5` = 0
+ `is_k_regular=3` intersect `edge_connectivity=6` = 0
+ `is_k_regular=3` intersect `is_tree=1` = 0
+ `is_k_regular=3` intersect `k_max_clique=4` = 0
+ `is_k_regular=3` intersect `k_max_clique=5` = 0
+ `is_k_regular=3` intersect `k_max_clique=6` = 0
+ `is_k_regular=3` intersect `k_max_clique=7` = 0
+ `is_k_regular=3` intersect `is_subgraph_free_bowtie=0` = 0
+ `is_k_regular=3` intersect `is_subgraph_free_open_bowtie=0` = 0
+ `is_k_regular=3` intersect `maximal_independent_vertex_set=6` = 0
+ `is_k_regular=3` intersect `maximal_independent_edge_set=1` = 0
+ `is_k_regular=4` intersect `automorphism_group_n=6` = 0
+ `is_k_regular=4` intersect `automorphism_group_n=14` = 0
+ `is_k_regular=4` intersect `automorphism_group_n=24` = 0
+ `is_k_regular=4` intersect `automorphism_group_n=36` = 0
+ `is_k_regular=4` intersect `automorphism_group_n=720` = 0
+ `is_k_regular=4` intersect `automorphism_group_n=5040` = 0
+ `is_k_regular=4` intersect `chromatic_number=6` = 0
+ `is_k_regular=4` intersect `chromatic_number=7` = 0
+ `is_k_regular=4` intersect `diameter=4` = 0
+ `is_k_regular=4` intersect `diameter=5` = 0
+ `is_k_regular=4` intersect `diameter=6` = 0
+ `is_k_regular=4` intersect `circumference=0` = 0
+ `is_k_regular=4` intersect `circumference=3` = 0
+ `is_k_regular=4` intersect `circumference=4` = 0
+ `is_k_regular=4` intersect `girth=0` = 0
+ `is_k_regular=4` intersect `girth=5` = 0
+ `is_k_regular=4` intersect `girth=6` = 0
+ `is_k_regular=4` intersect `girth=7` = 0
+ `is_k_regular=4` intersect `is_eulerian=0` = 0
+ `is_k_regular=4` intersect `n_articulation_points=1` = 0
+ `is_k_regular=4` intersect `n_articulation_points=2` = 0
+ `is_k_regular=4` intersect `n_articulation_points=3` = 0
+ `is_k_regular=4` intersect `n_articulation_points=4` = 0
+ `is_k_regular=4` intersect `n_articulation_points=5` = 0
+ `is_k_regular=4` intersect `is_subgraph_free_C4=1` = 0
+ `is_k_regular=4` intersect `vertex_connectivity>4` = 0
+ `is_k_regular=4` intersect `vertex_connectivity>5` = 0
+ `is_k_regular=4` intersect `edge_connectivity=1` = 0
+ `is_k_regular=4` intersect `edge_connectivity=3` = 0
+ `is_k_regular=4` intersect `edge_connectivity=5` = 0
+ `is_k_regular=4` intersect `edge_connectivity=6` = 0
+ `is_k_regular=4` intersect `is_tree=1` = 0
+ `is_k_regular=4` intersect `k_max_clique=6` = 0
+ `is_k_regular=4` intersect `k_max_clique=7` = 0
+ `is_k_regular=4` intersect `is_hamiltonian=0` = 0
+ `is_k_regular=4` intersect `maximal_independent_vertex_set=6` = 0
+ `is_k_regular=4` intersect `maximal_independent_edge_set=1` = 0
+ `is_k_regular=6` intersect `automorphism_group_n=1` = 0
+ `is_k_regular=6` intersect `automorphism_group_n=10` = 0
+ `is_k_regular=6` intersect `automorphism_group_n=14` = 0
+ `is_k_regular=6` intersect `automorphism_group_n=24` = 0
+ `is_k_regular=6` intersect `automorphism_group_n=36` = 0
+ `is_k_regular=6` intersect `automorphism_group_n=144` = 0
+ `is_k_regular=6` intersect `automorphism_group_n=240` = 0
+ `is_k_regular=6` intersect `automorphism_group_n=720` = 0
+ `is_k_regular=6` intersect `chromatic_number=2` = 0
+ `is_k_regular=6` intersect `chromatic_number=6` = 0
+ `is_k_regular=6` intersect `diameter=3` = 0
+ `is_k_regular=6` intersect `diameter=4` = 0
+ `is_k_regular=6` intersect `diameter=5` = 0
+ `is_k_regular=6` intersect `diameter=6` = 0
+ `is_k_regular=6` intersect `circumference=0` = 0
+ `is_k_regular=6` intersect `circumference=3` = 0
+ `is_k_regular=6` intersect `circumference=4` = 0
+ `is_k_regular=6` intersect `circumference=5` = 0
+ `is_k_regular=6` intersect `circumference=6` = 0
+ `is_k_regular=6` intersect `girth=0` = 0
+ `is_k_regular=6` intersect `girth=4` = 0
+ `is_k_regular=6` intersect `girth=5` = 0
+ `is_k_regular=6` intersect `girth=6` = 0
+ `is_k_regular=6` intersect `girth=7` = 0
+ `is_k_regular=6` intersect `radius=3` = 0
+ `is_k_regular=6` intersect `is_eulerian=0` = 0
+ `is_k_regular=6` intersect `is_planar=1` = 0
+ `is_k_regular=6` intersect `is_bipartite=1` = 0
+ `is_k_regular=6` intersect `n_articulation_points=1` = 0
+ `is_k_regular=6` intersect `n_articulation_points=2` = 0
+ `is_k_regular=6` intersect `n_articulation_points=3` = 0
+ `is_k_regular=6` intersect `n_articulation_points=4` = 0
+ `is_k_regular=6` intersect `n_articulation_points=5` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_K3=1` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_C4=1` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_C5=1` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_C6=1` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_C7=1` = 0
+ `is_k_regular=6` intersect `edge_connectivity=1` = 0
+ `is_k_regular=6` intersect `edge_connectivity=2` = 0
+ `is_k_regular=6` intersect `edge_connectivity=3` = 0
+ `is_k_regular=6` intersect `edge_connectivity=4` = 0
+ `is_k_regular=6` intersect `edge_connectivity=5` = 0
+ `is_k_regular=6` intersect `is_tree=1` = 0
+ `is_k_regular=6` intersect `k_max_clique=2` = 0
+ `is_k_regular=6` intersect `k_max_clique=6` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_bull=1` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_bowtie=1` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_diamond=1` = 0
+ `is_k_regular=6` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `is_k_regular=6` intersect `is_hamiltonian=0` = 0
+ `is_k_regular=6` intersect `maximal_independent_vertex_set=5` = 0
+ `is_k_regular=6` intersect `maximal_independent_vertex_set=6` = 0
+ `is_k_regular=6` intersect `maximal_independent_edge_set=1` = 0
+ `is_k_regular=6` intersect `maximal_independent_edge_set=2` = 0
+ `is_strongly_regular=0` intersect `diameter=1` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=1` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=2` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=4` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=12` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=14` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=16` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=20` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=36` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=144` = 0
+ `is_strongly_regular=1` intersect `automorphism_group_n=240` = 0
+ `is_strongly_regular=1` intersect `diameter=3` = 0
+ `is_strongly_regular=1` intersect `diameter=4` = 0
+ `is_strongly_regular=1` intersect `diameter=5` = 0
+ `is_strongly_regular=1` intersect `diameter=6` = 0
+ `is_strongly_regular=1` intersect `girth=6` = 0
+ `is_strongly_regular=1` intersect `girth=7` = 0
+ `is_strongly_regular=1` intersect `radius=3` = 0
+ `is_strongly_regular=1` intersect `is_distance_regular=0` = 0
+ `is_strongly_regular=1` intersect `n_articulation_points=1` = 0
+ `is_strongly_regular=1` intersect `n_articulation_points=2` = 0
+ `is_strongly_regular=1` intersect `n_articulation_points=3` = 0
+ `is_strongly_regular=1` intersect `n_articulation_points=4` = 0
+ `is_strongly_regular=1` intersect `n_articulation_points=5` = 0
+ `is_strongly_regular=1` intersect `edge_connectivity=1` = 0
+ `is_strongly_regular=1` intersect `is_real_spectrum=1` = 0
+ `is_strongly_regular=1` intersect `maximal_independent_vertex_set=6` = 0
+ `radius=1` intersect `diameter=3` = 0
+ `radius=1` intersect `diameter=4` = 0
+ `radius=1` intersect `diameter=5` = 0
+ `radius=1` intersect `diameter=6` = 0
+ `radius=1` intersect `girth=5` = 0
+ `radius=1` intersect `girth=7` = 0
+ `radius=1` intersect `is_k_regular=3` = 0
+ `radius=1` intersect `n_articulation_points=2` = 0
+ `radius=1` intersect `n_articulation_points=3` = 0
+ `radius=1` intersect `n_articulation_points=4` = 0
+ `radius=1` intersect `n_articulation_points=5` = 0
+ `radius=2` intersect `diameter=1` = 0
+ `radius=2` intersect `diameter=5` = 0
+ `radius=2` intersect `diameter=6` = 0
+ `radius=2` intersect `girth=6` = 0
+ `radius=2` intersect `maximal_independent_edge_set=1` = 0
+ `radius=3` intersect `automorphism_group_n=720` = 0
+ `radius=3` intersect `automorphism_group_n=5040` = 0
+ `radius=3` intersect `chromatic_number=7` = 0
+ `radius=3` intersect `diameter=1` = 0
+ `radius=3` intersect `diameter=2` = 0
+ `radius=3` intersect `is_k_regular=6` = 0
+ `radius=3` intersect `is_strongly_regular=1` = 0
+ `radius=3` intersect `vertex_connectivity>4` = 0
+ `radius=3` intersect `vertex_connectivity>5` = 0
+ `radius=3` intersect `edge_connectivity=5` = 0
+ `radius=3` intersect `edge_connectivity=6` = 0
+ `radius=3` intersect `k_max_clique=7` = 0
+ `radius=3` intersect `maximal_independent_vertex_set=1` = 0
+ `radius=3` intersect `maximal_independent_vertex_set=2` = 0
+ `radius=3` intersect `maximal_independent_edge_set=2` = 0
+ `is_eulerian=0` intersect `is_k_regular=4` = 0
+ `is_eulerian=0` intersect `is_k_regular=6` = 0
+ `is_eulerian=1` intersect `circumference=0` = 0
+ `is_eulerian=1` intersect `girth=0` = 0
+ `is_eulerian=1` intersect `girth=7` = 0
+ `is_eulerian=1` intersect `is_k_regular=3` = 0
+ `is_eulerian=1` intersect `n_articulation_points=4` = 0
+ `is_eulerian=1` intersect `n_articulation_points=5` = 0
+ `is_eulerian=1` intersect `edge_connectivity=1` = 0
+ `is_eulerian=1` intersect `edge_connectivity=3` = 0
+ `is_eulerian=1` intersect `edge_connectivity=5` = 0
+ `is_eulerian=1` intersect `is_tree=1` = 0
+ `is_distance_regular=0` intersect `diameter=1` = 0
+ `is_distance_regular=0` intersect `is_strongly_regular=1` = 0
+ `is_distance_regular=1` intersect `automorphism_group_n=1` = 0
+ `is_distance_regular=1` intersect `automorphism_group_n=2` = 0
+ `is_distance_regular=1` intersect `automorphism_group_n=4` = 0
+ `is_distance_regular=1` intersect `automorphism_group_n=36` = 0
+ `is_distance_regular=1` intersect `automorphism_group_n=144` = 0
+ `is_distance_regular=1` intersect `diameter=6` = 0
+ `is_distance_regular=1` intersect `girth=7` = 0
+ `is_distance_regular=1` intersect `n_articulation_points=1` = 0
+ `is_distance_regular=1` intersect `n_articulation_points=2` = 0
+ `is_distance_regular=1` intersect `n_articulation_points=3` = 0
+ `is_distance_regular=1` intersect `n_articulation_points=4` = 0
+ `is_distance_regular=1` intersect `n_articulation_points=5` = 0
+ `is_distance_regular=1` intersect `edge_connectivity=1` = 0
+ `is_distance_regular=1` intersect `is_real_spectrum=1` = 0
+ `is_distance_regular=1` intersect `maximal_independent_vertex_set=6` = 0
+ `is_planar=0` intersect `circumference=3` = 0
+ `is_planar=0` intersect `circumference=4` = 0
+ `is_planar=0` intersect `girth=7` = 0
+ `is_planar=0` intersect `is_k_regular=2` = 0
+ `is_planar=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_planar=1` intersect `chromatic_number=6` = 0
+ `is_planar=1` intersect `chromatic_number=7` = 0
+ `is_planar=1` intersect `is_k_regular=6` = 0
+ `is_planar=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_planar=1` intersect `vertex_connectivity>4` = 0
+ `is_planar=1` intersect `vertex_connectivity>5` = 0
+ `is_planar=1` intersect `edge_connectivity=5` = 0
+ `is_planar=1` intersect `edge_connectivity=6` = 0
+ `is_planar=1` intersect `k_max_clique=5` = 0
+ `is_planar=1` intersect `k_max_clique=6` = 0
+ `is_planar=1` intersect `k_max_clique=7` = 0
+ `is_bipartite=1` intersect `automorphism_group_n=10` = 0
+ `is_bipartite=1` intersect `automorphism_group_n=14` = 0
+ `is_bipartite=1` intersect `chromatic_number=5` = 0
+ `is_bipartite=1` intersect `chromatic_number=6` = 0
+ `is_bipartite=1` intersect `chromatic_number=7` = 0
+ `is_bipartite=1` intersect `diameter=1` = 0
+ `is_bipartite=1` intersect `is_k_regular=6` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_K3=0` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_C5=0` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_C7=0` = 0
+ `is_bipartite=1` intersect `vertex_connectivity>5` = 0
+ `is_bipartite=1` intersect `edge_connectivity=6` = 0
+ `is_bipartite=1` intersect `k_max_clique=3` = 0
+ `is_bipartite=1` intersect `k_max_clique=4` = 0
+ `is_bipartite=1` intersect `k_max_clique=5` = 0
+ `is_bipartite=1` intersect `k_max_clique=6` = 0
+ `is_bipartite=1` intersect `k_max_clique=7` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_bull=0` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_bowtie=0` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_diamond=0` = 0
+ `is_bipartite=1` intersect `is_subgraph_free_open_bowtie=0` = 0
+ `n_articulation_points=0` intersect `diameter=6` = 0
+ `n_articulation_points=0` intersect `edge_connectivity=1` = 0
+ `n_articulation_points=1` intersect `diameter=1` = 0
+ `n_articulation_points=1` intersect `diameter=6` = 0
+ `n_articulation_points=1` intersect `is_k_regular=3` = 0
+ `n_articulation_points=1` intersect `is_k_regular=4` = 0
+ `n_articulation_points=1` intersect `is_k_regular=6` = 0
+ `n_articulation_points=1` intersect `is_strongly_regular=1` = 0
+ `n_articulation_points=1` intersect `is_distance_regular=1` = 0
+ `n_articulation_points=1` intersect `vertex_connectivity>1` = 0
+ `n_articulation_points=1` intersect `vertex_connectivity>2` = 0
+ `n_articulation_points=1` intersect `vertex_connectivity>3` = 0
+ `n_articulation_points=1` intersect `vertex_connectivity>4` = 0
+ `n_articulation_points=1` intersect `vertex_connectivity>5` = 0
+ `n_articulation_points=1` intersect `edge_connectivity=5` = 0
+ `n_articulation_points=1` intersect `edge_connectivity=6` = 0
+ `n_articulation_points=1` intersect `is_hamiltonian=1` = 0
+ `n_articulation_points=1` intersect `maximal_independent_vertex_set=1` = 0
+ `n_articulation_points=2` intersect `diameter=1` = 0
+ `n_articulation_points=2` intersect `diameter=2` = 0
+ `n_articulation_points=2` intersect `is_k_regular=2` = 0
+ `n_articulation_points=2` intersect `is_k_regular=4` = 0
+ `n_articulation_points=2` intersect `is_k_regular=6` = 0
+ `n_articulation_points=2` intersect `is_strongly_regular=1` = 0
+ `n_articulation_points=2` intersect `radius=1` = 0
+ `n_articulation_points=2` intersect `is_distance_regular=1` = 0
+ `n_articulation_points=2` intersect `vertex_connectivity>1` = 0
+ `n_articulation_points=2` intersect `vertex_connectivity>2` = 0
+ `n_articulation_points=2` intersect `vertex_connectivity>3` = 0
+ `n_articulation_points=2` intersect `vertex_connectivity>4` = 0
+ `n_articulation_points=2` intersect `vertex_connectivity>5` = 0
+ `n_articulation_points=2` intersect `edge_connectivity=4` = 0
+ `n_articulation_points=2` intersect `edge_connectivity=5` = 0
+ `n_articulation_points=2` intersect `edge_connectivity=6` = 0
+ `n_articulation_points=2` intersect `is_hamiltonian=1` = 0
+ `n_articulation_points=2` intersect `maximal_independent_edge_set=1` = 0
+ `n_articulation_points=3` intersect `automorphism_group_n=14` = 0
+ `n_articulation_points=3` intersect `automorphism_group_n=5040` = 0
+ `n_articulation_points=3` intersect `diameter=1` = 0
+ `n_articulation_points=3` intersect `diameter=2` = 0
+ `n_articulation_points=3` intersect `is_k_regular=2` = 0
+ `n_articulation_points=3` intersect `is_k_regular=3` = 0
+ `n_articulation_points=3` intersect `is_k_regular=4` = 0
+ `n_articulation_points=3` intersect `is_k_regular=6` = 0
+ `n_articulation_points=3` intersect `is_strongly_regular=1` = 0
+ `n_articulation_points=3` intersect `radius=1` = 0
+ `n_articulation_points=3` intersect `is_distance_regular=1` = 0
+ `n_articulation_points=3` intersect `vertex_connectivity>1` = 0
+ `n_articulation_points=3` intersect `vertex_connectivity>2` = 0
+ `n_articulation_points=3` intersect `vertex_connectivity>3` = 0
+ `n_articulation_points=3` intersect `vertex_connectivity>4` = 0
+ `n_articulation_points=3` intersect `vertex_connectivity>5` = 0
+ `n_articulation_points=3` intersect `edge_connectivity=3` = 0
+ `n_articulation_points=3` intersect `edge_connectivity=4` = 0
+ `n_articulation_points=3` intersect `edge_connectivity=5` = 0
+ `n_articulation_points=3` intersect `edge_connectivity=6` = 0
+ `n_articulation_points=3` intersect `is_hamiltonian=1` = 0
+ `n_articulation_points=3` intersect `maximal_independent_vertex_set=1` = 0
+ `n_articulation_points=3` intersect `maximal_independent_vertex_set=2` = 0
+ `n_articulation_points=3` intersect `maximal_independent_edge_set=1` = 0
+ `n_articulation_points=4` intersect `automorphism_group_n=14` = 0
+ `n_articulation_points=4` intersect `automorphism_group_n=20` = 0
+ `n_articulation_points=4` intersect `automorphism_group_n=144` = 0
+ `n_articulation_points=4` intersect `automorphism_group_n=240` = 0
+ `n_articulation_points=4` intersect `automorphism_group_n=720` = 0
+ `n_articulation_points=4` intersect `automorphism_group_n=5040` = 0
+ `n_articulation_points=4` intersect `chromatic_number=7` = 0
+ `n_articulation_points=4` intersect `diameter=1` = 0
+ `n_articulation_points=4` intersect `diameter=2` = 0
+ `n_articulation_points=4` intersect `girth=7` = 0
+ `n_articulation_points=4` intersect `is_k_regular=2` = 0
+ `n_articulation_points=4` intersect `is_k_regular=3` = 0
+ `n_articulation_points=4` intersect `is_k_regular=4` = 0
+ `n_articulation_points=4` intersect `is_k_regular=6` = 0
+ `n_articulation_points=4` intersect `is_strongly_regular=1` = 0
+ `n_articulation_points=4` intersect `radius=1` = 0
+ `n_articulation_points=4` intersect `is_eulerian=1` = 0
+ `n_articulation_points=4` intersect `is_distance_regular=1` = 0
+ `n_articulation_points=4` intersect `is_subgraph_free_C7=0` = 0
+ `n_articulation_points=4` intersect `vertex_connectivity>1` = 0
+ `n_articulation_points=4` intersect `vertex_connectivity>2` = 0
+ `n_articulation_points=4` intersect `vertex_connectivity>3` = 0
+ `n_articulation_points=4` intersect `vertex_connectivity>4` = 0
+ `n_articulation_points=4` intersect `vertex_connectivity>5` = 0
+ `n_articulation_points=4` intersect `edge_connectivity=2` = 0
+ `n_articulation_points=4` intersect `edge_connectivity=3` = 0
+ `n_articulation_points=4` intersect `edge_connectivity=4` = 0
+ `n_articulation_points=4` intersect `edge_connectivity=5` = 0
+ `n_articulation_points=4` intersect `edge_connectivity=6` = 0
+ `n_articulation_points=4` intersect `k_max_clique=7` = 0
+ `n_articulation_points=4` intersect `is_hamiltonian=1` = 0
+ `n_articulation_points=4` intersect `maximal_independent_vertex_set=1` = 0
+ `n_articulation_points=4` intersect `maximal_independent_vertex_set=2` = 0
+ `n_articulation_points=4` intersect `maximal_independent_edge_set=2` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=14` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=16` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=20` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=36` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=48` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=72` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=144` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=240` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=720` = 0
+ `n_articulation_points=5` intersect `automorphism_group_n=5040` = 0
+ `n_articulation_points=5` intersect `chromatic_number=6` = 0
+ `n_articulation_points=5` intersect `chromatic_number=7` = 0
+ `n_articulation_points=5` intersect `diameter=1` = 0
+ `n_articulation_points=5` intersect `diameter=2` = 0
+ `n_articulation_points=5` intersect `girth=6` = 0
+ `n_articulation_points=5` intersect `girth=7` = 0
+ `n_articulation_points=5` intersect `is_k_regular=2` = 0
+ `n_articulation_points=5` intersect `is_k_regular=3` = 0
+ `n_articulation_points=5` intersect `is_k_regular=4` = 0
+ `n_articulation_points=5` intersect `is_k_regular=6` = 0
+ `n_articulation_points=5` intersect `is_strongly_regular=1` = 0
+ `n_articulation_points=5` intersect `radius=1` = 0
+ `n_articulation_points=5` intersect `is_eulerian=1` = 0
+ `n_articulation_points=5` intersect `is_distance_regular=1` = 0
+ `n_articulation_points=5` intersect `is_subgraph_free_C6=0` = 0
+ `n_articulation_points=5` intersect `is_subgraph_free_C7=0` = 0
+ `n_articulation_points=5` intersect `is_integral=1` = 0
+ `n_articulation_points=5` intersect `vertex_connectivity>1` = 0
+ `n_articulation_points=5` intersect `vertex_connectivity>2` = 0
+ `n_articulation_points=5` intersect `vertex_connectivity>3` = 0
+ `n_articulation_points=5` intersect `vertex_connectivity>4` = 0
+ `n_articulation_points=5` intersect `vertex_connectivity>5` = 0
+ `n_articulation_points=5` intersect `edge_connectivity=2` = 0
+ `n_articulation_points=5` intersect `edge_connectivity=3` = 0
+ `n_articulation_points=5` intersect `edge_connectivity=4` = 0
+ `n_articulation_points=5` intersect `edge_connectivity=5` = 0
+ `n_articulation_points=5` intersect `edge_connectivity=6` = 0
+ `n_articulation_points=5` intersect `k_max_clique=6` = 0
+ `n_articulation_points=5` intersect `k_max_clique=7` = 0
+ `n_articulation_points=5` intersect `is_hamiltonian=1` = 0
+ `n_articulation_points=5` intersect `maximal_independent_vertex_set=1` = 0
+ `n_articulation_points=5` intersect `maximal_independent_vertex_set=2` = 0
+ `n_articulation_points=5` intersect `maximal_independent_edge_set=1` = 0
+ `n_articulation_points=5` intersect `maximal_independent_edge_set=2` = 0
+ `is_subgraph_free_K3=0` intersect `girth=7` = 0
+ `is_subgraph_free_K3=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_K3=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_K3=1` intersect `chromatic_number=5` = 0
+ `is_subgraph_free_K3=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_K3=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_K3=1` intersect `diameter=1` = 0
+ `is_subgraph_free_K3=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_K3=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_subgraph_free_K3=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_subgraph_free_K3=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_K3=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_K3=1` intersect `k_max_clique=3` = 0
+ `is_subgraph_free_K3=1` intersect `k_max_clique=4` = 0
+ `is_subgraph_free_K3=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_K3=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_K3=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_K3=1` intersect `is_subgraph_free_bull=0` = 0
+ `is_subgraph_free_K3=1` intersect `is_subgraph_free_bowtie=0` = 0
+ `is_subgraph_free_K3=1` intersect `is_subgraph_free_diamond=0` = 0
+ `is_subgraph_free_K3=1` intersect `is_subgraph_free_open_bowtie=0` = 0
+ `is_subgraph_free_K4=0` intersect `girth=5` = 0
+ `is_subgraph_free_K4=0` intersect `girth=6` = 0
+ `is_subgraph_free_K4=0` intersect `girth=7` = 0
+ `is_subgraph_free_K4=0` intersect `is_k_regular=2` = 0
+ `is_subgraph_free_K4=0` intersect `is_k_regular=3` = 0
+ `is_subgraph_free_K4=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_K4=0` intersect `is_subgraph_free_K3=1` = 0
+ `is_subgraph_free_K4=0` intersect `is_subgraph_free_C4=1` = 0
+ `is_subgraph_free_K4=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_K4=0` intersect `k_max_clique=3` = 0
+ `is_subgraph_free_K4=0` intersect `is_subgraph_free_diamond=1` = 0
+ `is_subgraph_free_K4=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_K4=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_K4=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_K4=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_subgraph_free_K4=1` intersect `k_max_clique=4` = 0
+ `is_subgraph_free_K4=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_K4=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_K4=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_K5=0` intersect `chromatic_number=2` = 0
+ `is_subgraph_free_K5=0` intersect `circumference=0` = 0
+ `is_subgraph_free_K5=0` intersect `circumference=3` = 0
+ `is_subgraph_free_K5=0` intersect `circumference=4` = 0
+ `is_subgraph_free_K5=0` intersect `girth=0` = 0
+ `is_subgraph_free_K5=0` intersect `girth=4` = 0
+ `is_subgraph_free_K5=0` intersect `girth=5` = 0
+ `is_subgraph_free_K5=0` intersect `girth=6` = 0
+ `is_subgraph_free_K5=0` intersect `girth=7` = 0
+ `is_subgraph_free_K5=0` intersect `is_k_regular=2` = 0
+ `is_subgraph_free_K5=0` intersect `is_k_regular=3` = 0
+ `is_subgraph_free_K5=0` intersect `is_planar=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_subgraph_free_K3=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_subgraph_free_K4=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_subgraph_free_C4=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_subgraph_free_C5=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_tree=1` = 0
+ `is_subgraph_free_K5=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_K5=0` intersect `k_max_clique=3` = 0
+ `is_subgraph_free_K5=0` intersect `k_max_clique=4` = 0
+ `is_subgraph_free_K5=0` intersect `is_subgraph_free_bull=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_subgraph_free_bowtie=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_subgraph_free_diamond=1` = 0
+ `is_subgraph_free_K5=0` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `is_subgraph_free_K5=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_K5=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_K5=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_K5=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_K5=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_C4=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_C4=1` intersect `chromatic_number=5` = 0
+ `is_subgraph_free_C4=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_C4=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_C4=1` intersect `is_k_regular=4` = 0
+ `is_subgraph_free_C4=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_C4=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_subgraph_free_C4=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_subgraph_free_C4=1` intersect `vertex_connectivity>3` = 0
+ `is_subgraph_free_C4=1` intersect `vertex_connectivity>4` = 0
+ `is_subgraph_free_C4=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_C4=1` intersect `edge_connectivity=4` = 0
+ `is_subgraph_free_C4=1` intersect `edge_connectivity=5` = 0
+ `is_subgraph_free_C4=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_C4=1` intersect `k_max_clique=4` = 0
+ `is_subgraph_free_C4=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_C4=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_C4=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_C4=1` intersect `is_subgraph_free_diamond=0` = 0
+ `is_subgraph_free_C5=0` intersect `girth=7` = 0
+ `is_subgraph_free_C5=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_C5=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_C5=1` intersect `automorphism_group_n=10` = 0
+ `is_subgraph_free_C5=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_C5=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_C5=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_C5=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_subgraph_free_C5=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_C5=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_C5=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_C5=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_C5=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_C6=0` intersect `n_articulation_points=5` = 0
+ `is_subgraph_free_C6=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_C6=0` intersect `maximal_independent_edge_set=2` = 0
+ `is_subgraph_free_C6=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_C6=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_C6=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_C6=1` intersect `vertex_connectivity>4` = 0
+ `is_subgraph_free_C6=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_C6=1` intersect `edge_connectivity=5` = 0
+ `is_subgraph_free_C6=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_C6=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_C6=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_C7=0` intersect `circumference=0` = 0
+ `is_subgraph_free_C7=0` intersect `circumference=3` = 0
+ `is_subgraph_free_C7=0` intersect `girth=0` = 0
+ `is_subgraph_free_C7=0` intersect `is_k_regular=2` = 0
+ `is_subgraph_free_C7=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_C7=0` intersect `n_articulation_points=4` = 0
+ `is_subgraph_free_C7=0` intersect `n_articulation_points=5` = 0
+ `is_subgraph_free_C7=0` intersect `is_tree=1` = 0
+ `is_subgraph_free_C7=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_C7=0` intersect `maximal_independent_edge_set=2` = 0
+ `is_subgraph_free_C7=1` intersect `automorphism_group_n=14` = 0
+ `is_subgraph_free_C7=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_C7=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_C7=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_C7=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_C7=1` intersect `k_max_clique=7` = 0
+ `is_integral=0` intersect `diameter=1` = 0
+ `is_integral=1` intersect `automorphism_group_n=1` = 0
+ `is_integral=1` intersect `automorphism_group_n=10` = 0
+ `is_integral=1` intersect `automorphism_group_n=14` = 0
+ `is_integral=1` intersect `automorphism_group_n=20` = 0
+ `is_integral=1` intersect `automorphism_group_n=36` = 0
+ `is_integral=1` intersect `diameter=5` = 0
+ `is_integral=1` intersect `diameter=6` = 0
+ `is_integral=1` intersect `girth=7` = 0
+ `is_integral=1` intersect `n_articulation_points=5` = 0
+ `is_integral=1` intersect `is_real_spectrum=1` = 0
+ `vertex_connectivity>1` intersect `diameter=6` = 0
+ `vertex_connectivity>1` intersect `n_articulation_points=1` = 0
+ `vertex_connectivity>1` intersect `n_articulation_points=2` = 0
+ `vertex_connectivity>1` intersect `n_articulation_points=3` = 0
+ `vertex_connectivity>1` intersect `n_articulation_points=4` = 0
+ `vertex_connectivity>1` intersect `n_articulation_points=5` = 0
+ `vertex_connectivity>1` intersect `edge_connectivity=1` = 0
+ `vertex_connectivity>2` intersect `diameter=4` = 0
+ `vertex_connectivity>2` intersect `diameter=5` = 0
+ `vertex_connectivity>2` intersect `diameter=6` = 0
+ `vertex_connectivity>2` intersect `circumference=3` = 0
+ `vertex_connectivity>2` intersect `circumference=4` = 0
+ `vertex_connectivity>2` intersect `girth=6` = 0
+ `vertex_connectivity>2` intersect `girth=7` = 0
+ `vertex_connectivity>2` intersect `is_k_regular=2` = 0
+ `vertex_connectivity>2` intersect `n_articulation_points=1` = 0
+ `vertex_connectivity>2` intersect `n_articulation_points=2` = 0
+ `vertex_connectivity>2` intersect `n_articulation_points=3` = 0
+ `vertex_connectivity>2` intersect `n_articulation_points=4` = 0
+ `vertex_connectivity>2` intersect `n_articulation_points=5` = 0
+ `vertex_connectivity>2` intersect `edge_connectivity=1` = 0
+ `vertex_connectivity>2` intersect `edge_connectivity=2` = 0
+ `vertex_connectivity>2` intersect `maximal_independent_edge_set=1` = 0
+ `vertex_connectivity>3` intersect `diameter=4` = 0
+ `vertex_connectivity>3` intersect `diameter=5` = 0
+ `vertex_connectivity>3` intersect `diameter=6` = 0
+ `vertex_connectivity>3` intersect `circumference=0` = 0
+ `vertex_connectivity>3` intersect `circumference=3` = 0
+ `vertex_connectivity>3` intersect `circumference=4` = 0
+ `vertex_connectivity>3` intersect `girth=0` = 0
+ `vertex_connectivity>3` intersect `girth=5` = 0
+ `vertex_connectivity>3` intersect `girth=6` = 0
+ `vertex_connectivity>3` intersect `girth=7` = 0
+ `vertex_connectivity>3` intersect `is_k_regular=2` = 0
+ `vertex_connectivity>3` intersect `is_k_regular=3` = 0
+ `vertex_connectivity>3` intersect `n_articulation_points=1` = 0
+ `vertex_connectivity>3` intersect `n_articulation_points=2` = 0
+ `vertex_connectivity>3` intersect `n_articulation_points=3` = 0
+ `vertex_connectivity>3` intersect `n_articulation_points=4` = 0
+ `vertex_connectivity>3` intersect `n_articulation_points=5` = 0
+ `vertex_connectivity>3` intersect `is_subgraph_free_C4=1` = 0
+ `vertex_connectivity>3` intersect `edge_connectivity=1` = 0
+ `vertex_connectivity>3` intersect `edge_connectivity=2` = 0
+ `vertex_connectivity>3` intersect `edge_connectivity=3` = 0
+ `vertex_connectivity>3` intersect `is_tree=1` = 0
+ `vertex_connectivity>3` intersect `maximal_independent_edge_set=1` = 0
+ `vertex_connectivity>4` intersect `diameter=3` = 0
+ `vertex_connectivity>4` intersect `diameter=4` = 0
+ `vertex_connectivity>4` intersect `diameter=5` = 0
+ `vertex_connectivity>4` intersect `diameter=6` = 0
+ `vertex_connectivity>4` intersect `circumference=0` = 0
+ `vertex_connectivity>4` intersect `circumference=3` = 0
+ `vertex_connectivity>4` intersect `circumference=4` = 0
+ `vertex_connectivity>4` intersect `circumference=5` = 0
+ `vertex_connectivity>4` intersect `girth=0` = 0
+ `vertex_connectivity>4` intersect `girth=5` = 0
+ `vertex_connectivity>4` intersect `girth=6` = 0
+ `vertex_connectivity>4` intersect `girth=7` = 0
+ `vertex_connectivity>4` intersect `is_k_regular=2` = 0
+ `vertex_connectivity>4` intersect `is_k_regular=3` = 0
+ `vertex_connectivity>4` intersect `is_k_regular=4` = 0
+ `vertex_connectivity>4` intersect `radius=3` = 0
+ `vertex_connectivity>4` intersect `is_planar=1` = 0
+ `vertex_connectivity>4` intersect `n_articulation_points=1` = 0
+ `vertex_connectivity>4` intersect `n_articulation_points=2` = 0
+ `vertex_connectivity>4` intersect `n_articulation_points=3` = 0
+ `vertex_connectivity>4` intersect `n_articulation_points=4` = 0
+ `vertex_connectivity>4` intersect `n_articulation_points=5` = 0
+ `vertex_connectivity>4` intersect `is_subgraph_free_C4=1` = 0
+ `vertex_connectivity>4` intersect `is_subgraph_free_C6=1` = 0
+ `vertex_connectivity>4` intersect `edge_connectivity=1` = 0
+ `vertex_connectivity>4` intersect `edge_connectivity=2` = 0
+ `vertex_connectivity>4` intersect `edge_connectivity=3` = 0
+ `vertex_connectivity>4` intersect `edge_connectivity=4` = 0
+ `vertex_connectivity>4` intersect `is_tree=1` = 0
+ `vertex_connectivity>4` intersect `is_hamiltonian=0` = 0
+ `vertex_connectivity>4` intersect `maximal_independent_vertex_set=6` = 0
+ `vertex_connectivity>4` intersect `maximal_independent_edge_set=1` = 0
+ `vertex_connectivity>4` intersect `maximal_independent_edge_set=2` = 0
+ `vertex_connectivity>5` intersect `automorphism_group_n=14` = 0
+ `vertex_connectivity>5` intersect `automorphism_group_n=720` = 0
+ `vertex_connectivity>5` intersect `chromatic_number=2` = 0
+ `vertex_connectivity>5` intersect `diameter=3` = 0
+ `vertex_connectivity>5` intersect `diameter=4` = 0
+ `vertex_connectivity>5` intersect `diameter=5` = 0
+ `vertex_connectivity>5` intersect `diameter=6` = 0
+ `vertex_connectivity>5` intersect `circumference=0` = 0
+ `vertex_connectivity>5` intersect `circumference=3` = 0
+ `vertex_connectivity>5` intersect `circumference=4` = 0
+ `vertex_connectivity>5` intersect `circumference=5` = 0
+ `vertex_connectivity>5` intersect `circumference=6` = 0
+ `vertex_connectivity>5` intersect `girth=0` = 0
+ `vertex_connectivity>5` intersect `girth=4` = 0
+ `vertex_connectivity>5` intersect `girth=5` = 0
+ `vertex_connectivity>5` intersect `girth=6` = 0
+ `vertex_connectivity>5` intersect `girth=7` = 0
+ `vertex_connectivity>5` intersect `is_k_regular=2` = 0
+ `vertex_connectivity>5` intersect `is_k_regular=3` = 0
+ `vertex_connectivity>5` intersect `is_k_regular=4` = 0
+ `vertex_connectivity>5` intersect `radius=3` = 0
+ `vertex_connectivity>5` intersect `is_planar=1` = 0
+ `vertex_connectivity>5` intersect `is_bipartite=1` = 0
+ `vertex_connectivity>5` intersect `n_articulation_points=1` = 0
+ `vertex_connectivity>5` intersect `n_articulation_points=2` = 0
+ `vertex_connectivity>5` intersect `n_articulation_points=3` = 0
+ `vertex_connectivity>5` intersect `n_articulation_points=4` = 0
+ `vertex_connectivity>5` intersect `n_articulation_points=5` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_K3=1` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_C4=1` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_C5=1` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_C6=1` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_C7=1` = 0
+ `vertex_connectivity>5` intersect `edge_connectivity=1` = 0
+ `vertex_connectivity>5` intersect `edge_connectivity=2` = 0
+ `vertex_connectivity>5` intersect `edge_connectivity=3` = 0
+ `vertex_connectivity>5` intersect `edge_connectivity=4` = 0
+ `vertex_connectivity>5` intersect `edge_connectivity=5` = 0
+ `vertex_connectivity>5` intersect `is_tree=1` = 0
+ `vertex_connectivity>5` intersect `k_max_clique=2` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_bull=1` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_bowtie=1` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_diamond=1` = 0
+ `vertex_connectivity>5` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `vertex_connectivity>5` intersect `is_hamiltonian=0` = 0
+ `vertex_connectivity>5` intersect `maximal_independent_vertex_set=5` = 0
+ `vertex_connectivity>5` intersect `maximal_independent_vertex_set=6` = 0
+ `vertex_connectivity>5` intersect `maximal_independent_edge_set=1` = 0
+ `vertex_connectivity>5` intersect `maximal_independent_edge_set=2` = 0
+ `edge_connectivity=1` intersect `diameter=1` = 0
+ `edge_connectivity=1` intersect `is_k_regular=4` = 0
+ `edge_connectivity=1` intersect `is_k_regular=6` = 0
+ `edge_connectivity=1` intersect `is_strongly_regular=1` = 0
+ `edge_connectivity=1` intersect `is_eulerian=1` = 0
+ `edge_connectivity=1` intersect `is_distance_regular=1` = 0
+ `edge_connectivity=1` intersect `n_articulation_points=0` = 0
+ `edge_connectivity=1` intersect `vertex_connectivity>1` = 0
+ `edge_connectivity=1` intersect `vertex_connectivity>2` = 0
+ `edge_connectivity=1` intersect `vertex_connectivity>3` = 0
+ `edge_connectivity=1` intersect `vertex_connectivity>4` = 0
+ `edge_connectivity=1` intersect `vertex_connectivity>5` = 0
+ `edge_connectivity=1` intersect `is_hamiltonian=1` = 0
+ `edge_connectivity=2` intersect `automorphism_group_n=5040` = 0
+ `edge_connectivity=2` intersect `circumference=0` = 0
+ `edge_connectivity=2` intersect `girth=0` = 0
+ `edge_connectivity=2` intersect `is_k_regular=6` = 0
+ `edge_connectivity=2` intersect `n_articulation_points=4` = 0
+ `edge_connectivity=2` intersect `n_articulation_points=5` = 0
+ `edge_connectivity=2` intersect `vertex_connectivity>2` = 0
+ `edge_connectivity=2` intersect `vertex_connectivity>3` = 0
+ `edge_connectivity=2` intersect `vertex_connectivity>4` = 0
+ `edge_connectivity=2` intersect `vertex_connectivity>5` = 0
+ `edge_connectivity=2` intersect `is_tree=1` = 0
+ `edge_connectivity=3` intersect `automorphism_group_n=5040` = 0
+ `edge_connectivity=3` intersect `diameter=5` = 0
+ `edge_connectivity=3` intersect `diameter=6` = 0
+ `edge_connectivity=3` intersect `circumference=3` = 0
+ `edge_connectivity=3` intersect `girth=6` = 0
+ `edge_connectivity=3` intersect `girth=7` = 0
+ `edge_connectivity=3` intersect `is_k_regular=2` = 0
+ `edge_connectivity=3` intersect `is_k_regular=4` = 0
+ `edge_connectivity=3` intersect `is_k_regular=6` = 0
+ `edge_connectivity=3` intersect `is_eulerian=1` = 0
+ `edge_connectivity=3` intersect `n_articulation_points=3` = 0
+ `edge_connectivity=3` intersect `n_articulation_points=4` = 0
+ `edge_connectivity=3` intersect `n_articulation_points=5` = 0
+ `edge_connectivity=3` intersect `vertex_connectivity>3` = 0
+ `edge_connectivity=3` intersect `vertex_connectivity>4` = 0
+ `edge_connectivity=3` intersect `vertex_connectivity>5` = 0
+ `edge_connectivity=3` intersect `maximal_independent_vertex_set=1` = 0
+ `edge_connectivity=3` intersect `maximal_independent_edge_set=1` = 0
+ `edge_connectivity=4` intersect `automorphism_group_n=5040` = 0
+ `edge_connectivity=4` intersect `diameter=4` = 0
+ `edge_connectivity=4` intersect `diameter=5` = 0
+ `edge_connectivity=4` intersect `diameter=6` = 0
+ `edge_connectivity=4` intersect `circumference=0` = 0
+ `edge_connectivity=4` intersect `circumference=3` = 0
+ `edge_connectivity=4` intersect `circumference=4` = 0
+ `edge_connectivity=4` intersect `girth=0` = 0
+ `edge_connectivity=4` intersect `girth=5` = 0
+ `edge_connectivity=4` intersect `girth=6` = 0
+ `edge_connectivity=4` intersect `girth=7` = 0
+ `edge_connectivity=4` intersect `is_k_regular=2` = 0
+ `edge_connectivity=4` intersect `is_k_regular=3` = 0
+ `edge_connectivity=4` intersect `is_k_regular=6` = 0
+ `edge_connectivity=4` intersect `n_articulation_points=2` = 0
+ `edge_connectivity=4` intersect `n_articulation_points=3` = 0
+ `edge_connectivity=4` intersect `n_articulation_points=4` = 0
+ `edge_connectivity=4` intersect `n_articulation_points=5` = 0
+ `edge_connectivity=4` intersect `is_subgraph_free_C4=1` = 0
+ `edge_connectivity=4` intersect `vertex_connectivity>4` = 0
+ `edge_connectivity=4` intersect `vertex_connectivity>5` = 0
+ `edge_connectivity=4` intersect `is_tree=1` = 0
+ `edge_connectivity=4` intersect `maximal_independent_edge_set=1` = 0
+ `edge_connectivity=5` intersect `automorphism_group_n=5040` = 0
+ `edge_connectivity=5` intersect `diameter=3` = 0
+ `edge_connectivity=5` intersect `diameter=4` = 0
+ `edge_connectivity=5` intersect `diameter=5` = 0
+ `edge_connectivity=5` intersect `diameter=6` = 0
+ `edge_connectivity=5` intersect `circumference=0` = 0
+ `edge_connectivity=5` intersect `circumference=3` = 0
+ `edge_connectivity=5` intersect `circumference=4` = 0
+ `edge_connectivity=5` intersect `circumference=5` = 0
+ `edge_connectivity=5` intersect `girth=0` = 0
+ `edge_connectivity=5` intersect `girth=5` = 0
+ `edge_connectivity=5` intersect `girth=6` = 0
+ `edge_connectivity=5` intersect `girth=7` = 0
+ `edge_connectivity=5` intersect `is_k_regular=2` = 0
+ `edge_connectivity=5` intersect `is_k_regular=3` = 0
+ `edge_connectivity=5` intersect `is_k_regular=4` = 0
+ `edge_connectivity=5` intersect `is_k_regular=6` = 0
+ `edge_connectivity=5` intersect `radius=3` = 0
+ `edge_connectivity=5` intersect `is_eulerian=1` = 0
+ `edge_connectivity=5` intersect `is_planar=1` = 0
+ `edge_connectivity=5` intersect `n_articulation_points=1` = 0
+ `edge_connectivity=5` intersect `n_articulation_points=2` = 0
+ `edge_connectivity=5` intersect `n_articulation_points=3` = 0
+ `edge_connectivity=5` intersect `n_articulation_points=4` = 0
+ `edge_connectivity=5` intersect `n_articulation_points=5` = 0
+ `edge_connectivity=5` intersect `is_subgraph_free_C4=1` = 0
+ `edge_connectivity=5` intersect `is_subgraph_free_C6=1` = 0
+ `edge_connectivity=5` intersect `vertex_connectivity>5` = 0
+ `edge_connectivity=5` intersect `is_tree=1` = 0
+ `edge_connectivity=5` intersect `is_hamiltonian=0` = 0
+ `edge_connectivity=5` intersect `maximal_independent_vertex_set=6` = 0
+ `edge_connectivity=5` intersect `maximal_independent_edge_set=1` = 0
+ `edge_connectivity=5` intersect `maximal_independent_edge_set=2` = 0
+ `edge_connectivity=6` intersect `automorphism_group_n=14` = 0
+ `edge_connectivity=6` intersect `automorphism_group_n=720` = 0
+ `edge_connectivity=6` intersect `chromatic_number=2` = 0
+ `edge_connectivity=6` intersect `diameter=3` = 0
+ `edge_connectivity=6` intersect `diameter=4` = 0
+ `edge_connectivity=6` intersect `diameter=5` = 0
+ `edge_connectivity=6` intersect `diameter=6` = 0
+ `edge_connectivity=6` intersect `circumference=0` = 0
+ `edge_connectivity=6` intersect `circumference=3` = 0
+ `edge_connectivity=6` intersect `circumference=4` = 0
+ `edge_connectivity=6` intersect `circumference=5` = 0
+ `edge_connectivity=6` intersect `circumference=6` = 0
+ `edge_connectivity=6` intersect `girth=0` = 0
+ `edge_connectivity=6` intersect `girth=4` = 0
+ `edge_connectivity=6` intersect `girth=5` = 0
+ `edge_connectivity=6` intersect `girth=6` = 0
+ `edge_connectivity=6` intersect `girth=7` = 0
+ `edge_connectivity=6` intersect `is_k_regular=2` = 0
+ `edge_connectivity=6` intersect `is_k_regular=3` = 0
+ `edge_connectivity=6` intersect `is_k_regular=4` = 0
+ `edge_connectivity=6` intersect `radius=3` = 0
+ `edge_connectivity=6` intersect `is_planar=1` = 0
+ `edge_connectivity=6` intersect `is_bipartite=1` = 0
+ `edge_connectivity=6` intersect `n_articulation_points=1` = 0
+ `edge_connectivity=6` intersect `n_articulation_points=2` = 0
+ `edge_connectivity=6` intersect `n_articulation_points=3` = 0
+ `edge_connectivity=6` intersect `n_articulation_points=4` = 0
+ `edge_connectivity=6` intersect `n_articulation_points=5` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_K3=1` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_C4=1` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_C5=1` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_C6=1` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_C7=1` = 0
+ `edge_connectivity=6` intersect `is_tree=1` = 0
+ `edge_connectivity=6` intersect `k_max_clique=2` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_bull=1` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_bowtie=1` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_diamond=1` = 0
+ `edge_connectivity=6` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `edge_connectivity=6` intersect `is_hamiltonian=0` = 0
+ `edge_connectivity=6` intersect `maximal_independent_vertex_set=5` = 0
+ `edge_connectivity=6` intersect `maximal_independent_vertex_set=6` = 0
+ `edge_connectivity=6` intersect `maximal_independent_edge_set=1` = 0
+ `edge_connectivity=6` intersect `maximal_independent_edge_set=2` = 0
+ `is_tree=0` intersect `circumference=0` = 0
+ `is_tree=0` intersect `girth=0` = 0
+ `is_tree=1` intersect `automorphism_group_n=10` = 0
+ `is_tree=1` intersect `automorphism_group_n=14` = 0
+ `is_tree=1` intersect `automorphism_group_n=20` = 0
+ `is_tree=1` intersect `chromatic_number=3` = 0
+ `is_tree=1` intersect `chromatic_number=4` = 0
+ `is_tree=1` intersect `chromatic_number=5` = 0
+ `is_tree=1` intersect `chromatic_number=6` = 0
+ `is_tree=1` intersect `chromatic_number=7` = 0
+ `is_tree=1` intersect `circumference=3` = 0
+ `is_tree=1` intersect `circumference=4` = 0
+ `is_tree=1` intersect `circumference=5` = 0
+ `is_tree=1` intersect `circumference=6` = 0
+ `is_tree=1` intersect `circumference=7` = 0
+ `is_tree=1` intersect `girth=3` = 0
+ `is_tree=1` intersect `girth=4` = 0
+ `is_tree=1` intersect `girth=5` = 0
+ `is_tree=1` intersect `girth=6` = 0
+ `is_tree=1` intersect `girth=7` = 0
+ `is_tree=1` intersect `is_k_regular=2` = 0
+ `is_tree=1` intersect `is_k_regular=3` = 0
+ `is_tree=1` intersect `is_k_regular=4` = 0
+ `is_tree=1` intersect `is_k_regular=6` = 0
+ `is_tree=1` intersect `is_eulerian=1` = 0
+ `is_tree=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_tree=1` intersect `is_subgraph_free_C7=0` = 0
+ `is_tree=1` intersect `vertex_connectivity>3` = 0
+ `is_tree=1` intersect `vertex_connectivity>4` = 0
+ `is_tree=1` intersect `vertex_connectivity>5` = 0
+ `is_tree=1` intersect `edge_connectivity=2` = 0
+ `is_tree=1` intersect `edge_connectivity=4` = 0
+ `is_tree=1` intersect `edge_connectivity=5` = 0
+ `is_tree=1` intersect `edge_connectivity=6` = 0
+ `is_tree=1` intersect `k_max_clique=5` = 0
+ `is_tree=1` intersect `k_max_clique=6` = 0
+ `is_tree=1` intersect `k_max_clique=7` = 0
+ `is_tree=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `is_tree=1` intersect `maximal_independent_vertex_set=1` = 0
+ `is_chordal=0` intersect `diameter=1` = 0
+ `is_chordal=0` intersect `maximal_independent_vertex_set=1` = 0
+ `is_chordal=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_chordal=1` intersect `automorphism_group_n=14` = 0
+ `is_chordal=1` intersect `automorphism_group_n=20` = 0
+ `is_chordal=1` intersect `girth=6` = 0
+ `is_chordal=1` intersect `girth=7` = 0
+ `k_max_clique=2` intersect `chromatic_number=5` = 0
+ `k_max_clique=2` intersect `chromatic_number=6` = 0
+ `k_max_clique=2` intersect `chromatic_number=7` = 0
+ `k_max_clique=2` intersect `diameter=1` = 0
+ `k_max_clique=2` intersect `is_k_regular=6` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_K3=0` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_K4=0` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_K5=0` = 0
+ `k_max_clique=2` intersect `vertex_connectivity>5` = 0
+ `k_max_clique=2` intersect `edge_connectivity=6` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_bull=0` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_bowtie=0` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_diamond=0` = 0
+ `k_max_clique=2` intersect `is_subgraph_free_open_bowtie=0` = 0
+ `k_max_clique=3` intersect `chromatic_number=6` = 0
+ `k_max_clique=3` intersect `chromatic_number=7` = 0
+ `k_max_clique=3` intersect `girth=7` = 0
+ `k_max_clique=3` intersect `is_bipartite=1` = 0
+ `k_max_clique=3` intersect `is_subgraph_free_K3=1` = 0
+ `k_max_clique=3` intersect `is_subgraph_free_K4=0` = 0
+ `k_max_clique=3` intersect `is_subgraph_free_K5=0` = 0
+ `k_max_clique=4` intersect `automorphism_group_n=5040` = 0
+ `k_max_clique=4` intersect `chromatic_number=7` = 0
+ `k_max_clique=4` intersect `girth=5` = 0
+ `k_max_clique=4` intersect `girth=6` = 0
+ `k_max_clique=4` intersect `girth=7` = 0
+ `k_max_clique=4` intersect `is_k_regular=2` = 0
+ `k_max_clique=4` intersect `is_k_regular=3` = 0
+ `k_max_clique=4` intersect `is_bipartite=1` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_K3=1` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_K4=1` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_K5=0` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_C4=1` = 0
+ `k_max_clique=4` intersect `is_subgraph_free_diamond=1` = 0
+ `k_max_clique=4` intersect `maximal_independent_vertex_set=1` = 0
+ `k_max_clique=4` intersect `maximal_independent_edge_set=1` = 0
+ `k_max_clique=5` intersect `automorphism_group_n=5040` = 0
+ `k_max_clique=5` intersect `chromatic_number=2` = 0
+ `k_max_clique=5` intersect `chromatic_number=7` = 0
+ `k_max_clique=5` intersect `circumference=0` = 0
+ `k_max_clique=5` intersect `circumference=3` = 0
+ `k_max_clique=5` intersect `circumference=4` = 0
+ `k_max_clique=5` intersect `girth=0` = 0
+ `k_max_clique=5` intersect `girth=4` = 0
+ `k_max_clique=5` intersect `girth=5` = 0
+ `k_max_clique=5` intersect `girth=6` = 0
+ `k_max_clique=5` intersect `girth=7` = 0
+ `k_max_clique=5` intersect `is_k_regular=2` = 0
+ `k_max_clique=5` intersect `is_k_regular=3` = 0
+ `k_max_clique=5` intersect `is_planar=1` = 0
+ `k_max_clique=5` intersect `is_bipartite=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_K3=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_K4=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_K5=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_C4=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_C5=1` = 0
+ `k_max_clique=5` intersect `is_tree=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_bull=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_bowtie=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_diamond=1` = 0
+ `k_max_clique=5` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `k_max_clique=5` intersect `maximal_independent_edge_set=1` = 0
+ `k_max_clique=6` intersect `automorphism_group_n=10` = 0
+ `k_max_clique=6` intersect `automorphism_group_n=14` = 0
+ `k_max_clique=6` intersect `automorphism_group_n=20` = 0
+ `k_max_clique=6` intersect `automorphism_group_n=5040` = 0
+ `k_max_clique=6` intersect `chromatic_number=2` = 0
+ `k_max_clique=6` intersect `chromatic_number=3` = 0
+ `k_max_clique=6` intersect `chromatic_number=4` = 0
+ `k_max_clique=6` intersect `diameter=6` = 0
+ `k_max_clique=6` intersect `circumference=0` = 0
+ `k_max_clique=6` intersect `circumference=3` = 0
+ `k_max_clique=6` intersect `circumference=4` = 0
+ `k_max_clique=6` intersect `circumference=5` = 0
+ `k_max_clique=6` intersect `girth=0` = 0
+ `k_max_clique=6` intersect `girth=4` = 0
+ `k_max_clique=6` intersect `girth=5` = 0
+ `k_max_clique=6` intersect `girth=6` = 0
+ `k_max_clique=6` intersect `girth=7` = 0
+ `k_max_clique=6` intersect `is_k_regular=2` = 0
+ `k_max_clique=6` intersect `is_k_regular=3` = 0
+ `k_max_clique=6` intersect `is_k_regular=4` = 0
+ `k_max_clique=6` intersect `is_k_regular=6` = 0
+ `k_max_clique=6` intersect `is_planar=1` = 0
+ `k_max_clique=6` intersect `is_bipartite=1` = 0
+ `k_max_clique=6` intersect `n_articulation_points=5` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_K3=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_K4=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_K5=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_C4=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_C5=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_C6=1` = 0
+ `k_max_clique=6` intersect `is_tree=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_bull=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_bowtie=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_diamond=1` = 0
+ `k_max_clique=6` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `k_max_clique=6` intersect `maximal_independent_vertex_set=6` = 0
+ `k_max_clique=6` intersect `maximal_independent_edge_set=1` = 0
+ `k_max_clique=6` intersect `maximal_independent_edge_set=2` = 0
+ `k_max_clique=7` intersect `automorphism_group_n=10` = 0
+ `k_max_clique=7` intersect `automorphism_group_n=14` = 0
+ `k_max_clique=7` intersect `automorphism_group_n=20` = 0
+ `k_max_clique=7` intersect `chromatic_number=2` = 0
+ `k_max_clique=7` intersect `chromatic_number=3` = 0
+ `k_max_clique=7` intersect `chromatic_number=4` = 0
+ `k_max_clique=7` intersect `chromatic_number=5` = 0
+ `k_max_clique=7` intersect `chromatic_number=6` = 0
+ `k_max_clique=7` intersect `diameter=5` = 0
+ `k_max_clique=7` intersect `diameter=6` = 0
+ `k_max_clique=7` intersect `circumference=0` = 0
+ `k_max_clique=7` intersect `circumference=3` = 0
+ `k_max_clique=7` intersect `circumference=4` = 0
+ `k_max_clique=7` intersect `circumference=5` = 0
+ `k_max_clique=7` intersect `circumference=6` = 0
+ `k_max_clique=7` intersect `girth=0` = 0
+ `k_max_clique=7` intersect `girth=4` = 0
+ `k_max_clique=7` intersect `girth=5` = 0
+ `k_max_clique=7` intersect `girth=6` = 0
+ `k_max_clique=7` intersect `girth=7` = 0
+ `k_max_clique=7` intersect `is_k_regular=2` = 0
+ `k_max_clique=7` intersect `is_k_regular=3` = 0
+ `k_max_clique=7` intersect `is_k_regular=4` = 0
+ `k_max_clique=7` intersect `radius=3` = 0
+ `k_max_clique=7` intersect `is_planar=1` = 0
+ `k_max_clique=7` intersect `is_bipartite=1` = 0
+ `k_max_clique=7` intersect `n_articulation_points=4` = 0
+ `k_max_clique=7` intersect `n_articulation_points=5` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_K3=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_K4=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_K5=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_C4=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_C5=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_C6=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_C7=1` = 0
+ `k_max_clique=7` intersect `is_tree=1` = 0
+ `k_max_clique=7` intersect `is_real_spectrum=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_bull=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_bowtie=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_diamond=1` = 0
+ `k_max_clique=7` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `k_max_clique=7` intersect `maximal_independent_vertex_set=5` = 0
+ `k_max_clique=7` intersect `maximal_independent_vertex_set=6` = 0
+ `k_max_clique=7` intersect `maximal_independent_edge_set=1` = 0
+ `k_max_clique=7` intersect `maximal_independent_edge_set=2` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=6` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=10` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=12` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=14` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=16` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=20` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=24` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=36` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=48` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=72` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=120` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=144` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=240` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=720` = 0
+ `is_real_spectrum=1` intersect `automorphism_group_n=5040` = 0
+ `is_real_spectrum=1` intersect `chromatic_number=7` = 0
+ `is_real_spectrum=1` intersect `diameter=1` = 0
+ `is_real_spectrum=1` intersect `is_strongly_regular=1` = 0
+ `is_real_spectrum=1` intersect `is_distance_regular=1` = 0
+ `is_real_spectrum=1` intersect `is_integral=1` = 0
+ `is_real_spectrum=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_bull=0` intersect `girth=7` = 0
+ `is_subgraph_free_bull=0` intersect `is_k_regular=2` = 0
+ `is_subgraph_free_bull=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_bull=0` intersect `is_subgraph_free_K3=1` = 0
+ `is_subgraph_free_bull=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_bull=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_bull=1` intersect `chromatic_number=5` = 0
+ `is_subgraph_free_bull=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_bull=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_bull=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_bull=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_subgraph_free_bull=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_bull=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_bull=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_bull=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_bull=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_bowtie=0` intersect `girth=7` = 0
+ `is_subgraph_free_bowtie=0` intersect `is_k_regular=2` = 0
+ `is_subgraph_free_bowtie=0` intersect `is_k_regular=3` = 0
+ `is_subgraph_free_bowtie=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_bowtie=0` intersect `is_subgraph_free_K3=1` = 0
+ `is_subgraph_free_bowtie=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_bowtie=0` intersect `is_subgraph_free_open_bowtie=1` = 0
+ `is_subgraph_free_bowtie=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_bowtie=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_bowtie=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_bowtie=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_bowtie=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_subgraph_free_bowtie=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_bowtie=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_bowtie=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_bowtie=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_bowtie=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_diamond=0` intersect `girth=7` = 0
+ `is_subgraph_free_diamond=0` intersect `is_k_regular=2` = 0
+ `is_subgraph_free_diamond=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_diamond=0` intersect `is_subgraph_free_K3=1` = 0
+ `is_subgraph_free_diamond=0` intersect `is_subgraph_free_C4=1` = 0
+ `is_subgraph_free_diamond=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_diamond=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_diamond=1` intersect `chromatic_number=5` = 0
+ `is_subgraph_free_diamond=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_diamond=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_diamond=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_diamond=1` intersect `is_subgraph_free_K4=0` = 0
+ `is_subgraph_free_diamond=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_subgraph_free_diamond=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_diamond=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_diamond=1` intersect `k_max_clique=4` = 0
+ `is_subgraph_free_diamond=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_diamond=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_diamond=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_open_bowtie=0` intersect `girth=7` = 0
+ `is_subgraph_free_open_bowtie=0` intersect `is_k_regular=2` = 0
+ `is_subgraph_free_open_bowtie=0` intersect `is_k_regular=3` = 0
+ `is_subgraph_free_open_bowtie=0` intersect `is_bipartite=1` = 0
+ `is_subgraph_free_open_bowtie=0` intersect `is_subgraph_free_K3=1` = 0
+ `is_subgraph_free_open_bowtie=0` intersect `k_max_clique=2` = 0
+ `is_subgraph_free_open_bowtie=0` intersect `maximal_independent_edge_set=1` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `chromatic_number=5` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `chromatic_number=6` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `chromatic_number=7` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `is_k_regular=6` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `is_subgraph_free_K5=0` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `vertex_connectivity>5` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `edge_connectivity=6` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `k_max_clique=5` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `k_max_clique=6` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `k_max_clique=7` = 0
+ `is_subgraph_free_open_bowtie=1` intersect `is_subgraph_free_bowtie=0` = 0
+ `is_hamiltonian=0` intersect `diameter=1` = 0
+ `is_hamiltonian=0` intersect `is_k_regular=4` = 0
+ `is_hamiltonian=0` intersect `is_k_regular=6` = 0
+ `is_hamiltonian=0` intersect `vertex_connectivity>4` = 0
+ `is_hamiltonian=0` intersect `vertex_connectivity>5` = 0
+ `is_hamiltonian=0` intersect `edge_connectivity=5` = 0
+ `is_hamiltonian=0` intersect `edge_connectivity=6` = 0
+ `is_hamiltonian=1` intersect `diameter=6` = 0
+ `is_hamiltonian=1` intersect `girth=7` = 0
+ `is_hamiltonian=1` intersect `n_articulation_points=1` = 0
+ `is_hamiltonian=1` intersect `n_articulation_points=2` = 0
+ `is_hamiltonian=1` intersect `n_articulation_points=3` = 0
+ `is_hamiltonian=1` intersect `n_articulation_points=4` = 0
+ `is_hamiltonian=1` intersect `n_articulation_points=5` = 0
+ `is_hamiltonian=1` intersect `edge_connectivity=1` = 0
+ `is_hamiltonian=1` intersect `maximal_independent_vertex_set=6` = 0
+ `has_fractional_duality_gap_vertex_chromatic=0` intersect `girth=7` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `automorphism_group_n=720` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `automorphism_group_n=5040` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `chromatic_number=2` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `diameter=1` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `circumference=0` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `circumference=3` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `circumference=4` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `girth=0` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `is_tree=1` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `maximal_independent_vertex_set=1` = 0
+ `has_fractional_duality_gap_vertex_chromatic=1` intersect `maximal_independent_edge_set=1` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=1` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=4` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=8` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=10` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=12` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=14` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=16` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=20` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=24` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=36` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=48` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=72` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=144` = 0
+ `maximal_independent_vertex_set=1` intersect `automorphism_group_n=240` = 0
+ `maximal_independent_vertex_set=1` intersect `chromatic_number=2` = 0
+ `maximal_independent_vertex_set=1` intersect `diameter=2` = 0
+ `maximal_independent_vertex_set=1` intersect `diameter=4` = 0
+ `maximal_independent_vertex_set=1` intersect `diameter=5` = 0
+ `maximal_independent_vertex_set=1` intersect `diameter=6` = 0
+ `maximal_independent_vertex_set=1` intersect `circumference=0` = 0
+ `maximal_independent_vertex_set=1` intersect `girth=0` = 0
+ `maximal_independent_vertex_set=1` intersect `girth=4` = 0
+ `maximal_independent_vertex_set=1` intersect `girth=5` = 0
+ `maximal_independent_vertex_set=1` intersect `girth=6` = 0
+ `maximal_independent_vertex_set=1` intersect `girth=7` = 0
+ `maximal_independent_vertex_set=1` intersect `is_k_regular=0` = 0
+ `maximal_independent_vertex_set=1` intersect `radius=3` = 0
+ `maximal_independent_vertex_set=1` intersect `n_articulation_points=1` = 0
+ `maximal_independent_vertex_set=1` intersect `n_articulation_points=3` = 0
+ `maximal_independent_vertex_set=1` intersect `n_articulation_points=4` = 0
+ `maximal_independent_vertex_set=1` intersect `n_articulation_points=5` = 0
+ `maximal_independent_vertex_set=1` intersect `edge_connectivity=3` = 0
+ `maximal_independent_vertex_set=1` intersect `is_tree=1` = 0
+ `maximal_independent_vertex_set=1` intersect `is_chordal=0` = 0
+ `maximal_independent_vertex_set=1` intersect `k_max_clique=4` = 0
+ `maximal_independent_vertex_set=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `maximal_independent_vertex_set=2` intersect `diameter=5` = 0
+ `maximal_independent_vertex_set=2` intersect `diameter=6` = 0
+ `maximal_independent_vertex_set=2` intersect `girth=6` = 0
+ `maximal_independent_vertex_set=2` intersect `girth=7` = 0
+ `maximal_independent_vertex_set=2` intersect `radius=3` = 0
+ `maximal_independent_vertex_set=2` intersect `n_articulation_points=3` = 0
+ `maximal_independent_vertex_set=2` intersect `n_articulation_points=4` = 0
+ `maximal_independent_vertex_set=2` intersect `n_articulation_points=5` = 0
+ `maximal_independent_vertex_set=3` intersect `automorphism_group_n=5040` = 0
+ `maximal_independent_vertex_set=3` intersect `diameter=1` = 0
+ `maximal_independent_vertex_set=4` intersect `automorphism_group_n=5040` = 0
+ `maximal_independent_vertex_set=4` intersect `diameter=1` = 0
+ `maximal_independent_vertex_set=5` intersect `automorphism_group_n=14` = 0
+ `maximal_independent_vertex_set=5` intersect `automorphism_group_n=5040` = 0
+ `maximal_independent_vertex_set=5` intersect `chromatic_number=7` = 0
+ `maximal_independent_vertex_set=5` intersect `diameter=1` = 0
+ `maximal_independent_vertex_set=5` intersect `is_k_regular=6` = 0
+ `maximal_independent_vertex_set=5` intersect `vertex_connectivity>5` = 0
+ `maximal_independent_vertex_set=5` intersect `edge_connectivity=6` = 0
+ `maximal_independent_vertex_set=5` intersect `k_max_clique=7` = 0
+ `maximal_independent_vertex_set=6` intersect `automorphism_group_n=10` = 0
+ `maximal_independent_vertex_set=6` intersect `automorphism_group_n=14` = 0
+ `maximal_independent_vertex_set=6` intersect `automorphism_group_n=20` = 0
+ `maximal_independent_vertex_set=6` intersect `automorphism_group_n=5040` = 0
+ `maximal_independent_vertex_set=6` intersect `chromatic_number=6` = 0
+ `maximal_independent_vertex_set=6` intersect `chromatic_number=7` = 0
+ `maximal_independent_vertex_set=6` intersect `diameter=1` = 0
+ `maximal_independent_vertex_set=6` intersect `is_k_regular=2` = 0
+ `maximal_independent_vertex_set=6` intersect `is_k_regular=3` = 0
+ `maximal_independent_vertex_set=6` intersect `is_k_regular=4` = 0
+ `maximal_independent_vertex_set=6` intersect `is_k_regular=6` = 0
+ `maximal_independent_vertex_set=6` intersect `is_strongly_regular=1` = 0
+ `maximal_independent_vertex_set=6` intersect `is_distance_regular=1` = 0
+ `maximal_independent_vertex_set=6` intersect `vertex_connectivity>4` = 0
+ `maximal_independent_vertex_set=6` intersect `vertex_connectivity>5` = 0
+ `maximal_independent_vertex_set=6` intersect `edge_connectivity=5` = 0
+ `maximal_independent_vertex_set=6` intersect `edge_connectivity=6` = 0
+ `maximal_independent_vertex_set=6` intersect `k_max_clique=6` = 0
+ `maximal_independent_vertex_set=6` intersect `k_max_clique=7` = 0
+ `maximal_independent_vertex_set=6` intersect `is_hamiltonian=1` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=1` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=4` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=8` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=10` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=12` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=14` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=16` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=20` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=36` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=48` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=72` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=144` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=240` = 0
+ `maximal_independent_edge_set=1` intersect `automorphism_group_n=720` = 0
+ `maximal_independent_edge_set=1` intersect `chromatic_number=4` = 0
+ `maximal_independent_edge_set=1` intersect `chromatic_number=5` = 0
+ `maximal_independent_edge_set=1` intersect `chromatic_number=6` = 0
+ `maximal_independent_edge_set=1` intersect `chromatic_number=7` = 0
+ `maximal_independent_edge_set=1` intersect `diameter=3` = 0
+ `maximal_independent_edge_set=1` intersect `diameter=4` = 0
+ `maximal_independent_edge_set=1` intersect `diameter=6` = 0
+ `maximal_independent_edge_set=1` intersect `circumference=4` = 0
+ `maximal_independent_edge_set=1` intersect `circumference=5` = 0
+ `maximal_independent_edge_set=1` intersect `circumference=6` = 0
+ `maximal_independent_edge_set=1` intersect `circumference=7` = 0
+ `maximal_independent_edge_set=1` intersect `girth=4` = 0
+ `maximal_independent_edge_set=1` intersect `girth=5` = 0
+ `maximal_independent_edge_set=1` intersect `girth=6` = 0
+ `maximal_independent_edge_set=1` intersect `girth=7` = 0
+ `maximal_independent_edge_set=1` intersect `is_k_regular=3` = 0
+ `maximal_independent_edge_set=1` intersect `is_k_regular=4` = 0
+ `maximal_independent_edge_set=1` intersect `is_k_regular=6` = 0
+ `maximal_independent_edge_set=1` intersect `radius=2` = 0
+ `maximal_independent_edge_set=1` intersect `is_planar=0` = 0
+ `maximal_independent_edge_set=1` intersect `n_articulation_points=2` = 0
+ `maximal_independent_edge_set=1` intersect `n_articulation_points=3` = 0
+ `maximal_independent_edge_set=1` intersect `n_articulation_points=5` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_K4=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_K5=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_C4=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_C5=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_C6=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_C7=0` = 0
+ `maximal_independent_edge_set=1` intersect `vertex_connectivity>2` = 0
+ `maximal_independent_edge_set=1` intersect `vertex_connectivity>3` = 0
+ `maximal_independent_edge_set=1` intersect `vertex_connectivity>4` = 0
+ `maximal_independent_edge_set=1` intersect `vertex_connectivity>5` = 0
+ `maximal_independent_edge_set=1` intersect `edge_connectivity=3` = 0
+ `maximal_independent_edge_set=1` intersect `edge_connectivity=4` = 0
+ `maximal_independent_edge_set=1` intersect `edge_connectivity=5` = 0
+ `maximal_independent_edge_set=1` intersect `edge_connectivity=6` = 0
+ `maximal_independent_edge_set=1` intersect `is_chordal=0` = 0
+ `maximal_independent_edge_set=1` intersect `k_max_clique=4` = 0
+ `maximal_independent_edge_set=1` intersect `k_max_clique=5` = 0
+ `maximal_independent_edge_set=1` intersect `k_max_clique=6` = 0
+ `maximal_independent_edge_set=1` intersect `k_max_clique=7` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_bull=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_bowtie=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_diamond=0` = 0
+ `maximal_independent_edge_set=1` intersect `is_subgraph_free_open_bowtie=0` = 0
+ `maximal_independent_edge_set=1` intersect `has_fractional_duality_gap_vertex_chromatic=1` = 0
+ `maximal_independent_edge_set=2` intersect `automorphism_group_n=1` = 0
+ `maximal_independent_edge_set=2` intersect `automorphism_group_n=14` = 0
+ `maximal_independent_edge_set=2` intersect `automorphism_group_n=20` = 0
+ `maximal_independent_edge_set=2` intersect `chromatic_number=6` = 0
+ `maximal_independent_edge_set=2` intersect `chromatic_number=7` = 0
+ `maximal_independent_edge_set=2` intersect `diameter=5` = 0
+ `maximal_independent_edge_set=2` intersect `diameter=6` = 0
+ `maximal_independent_edge_set=2` intersect `girth=6` = 0
+ `maximal_independent_edge_set=2` intersect `girth=7` = 0
+ `maximal_independent_edge_set=2` intersect `is_k_regular=6` = 0
+ `maximal_independent_edge_set=2` intersect `radius=3` = 0
+ `maximal_independent_edge_set=2` intersect `n_articulation_points=4` = 0
+ `maximal_independent_edge_set=2` intersect `n_articulation_points=5` = 0
+ `maximal_independent_edge_set=2` intersect `is_subgraph_free_C6=0` = 0
+ `maximal_independent_edge_set=2` intersect `is_subgraph_free_C7=0` = 0
+ `maximal_independent_edge_set=2` intersect `vertex_connectivity>4` = 0
+ `maximal_independent_edge_set=2` intersect `vertex_connectivity>5` = 0
+ `maximal_independent_edge_set=2` intersect `edge_connectivity=5` = 0
+ `maximal_independent_edge_set=2` intersect `edge_connectivity=6` = 0
+ `maximal_independent_edge_set=2` intersect `k_max_clique=6` = 0
+ `maximal_independent_edge_set=2` intersect `k_max_clique=7` = 0
