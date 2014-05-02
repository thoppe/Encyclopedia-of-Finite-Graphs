-- Invariant reference table for integers

CREATE TABLE IF NOT EXISTS ref_invariant_integer(
    invariant_id INTEGER PRIMARY KEY,  
    function_name TEXT,

    UNIQUE (function_name),
    UNIQUE (invariant_id)
);

-- List of invariants
-- DO NOT CHANGE THE INDEXING, they are to be constant across versions
-- For this reason there may be gaps

INSERT OR IGNORE INTO ref_invariant_integer 
(function_name, invariant_id) VALUES 

  ("automorphism_group_n", 1),

  ("chromatic_number",2),
  ("n_vertex", 3),

  ("diameter",4), 
  ("n_cycle_basis",5),
  ("circumference",6),
  ("girth",7),

  ("n_edge",8),
  ("n_endpoints",9),

  ("is_k_regular",10),
  ("is_strongly_regular",11),

  ("radius",12),
  ("is_eulerian",13),
  ("is_distance_regular",14),    
  ("is_planar",15),
  ("is_bipartite",16),

  ("n_articulation_points",17),
  ("is_subgraph_free_K3",18),
  ("is_subgraph_free_K4",19),
  ("is_subgraph_free_K5",20),
  ("is_subgraph_free_C4",21),
  ("is_subgraph_free_C5",22),
  ("is_subgraph_free_C6",23),
  ("is_subgraph_free_C7",24),
  ("is_subgraph_free_C8",25),
  ("is_subgraph_free_C9",26),
  ("is_subgraph_free_C10",27),

  ("is_integral",28),

  ("vertex_connectivity",29),
  ("edge_connectivity",30),

  ("is_tree",31),
  ("is_chordal",32),

  ("k_max_clique",33),

  ("is_rational_spectrum",34),
  ("is_real_spectrum",35),

  ("is_subgraph_free_bull",36),
  ("is_subgraph_free_bowtie",37),
  ("is_subgraph_free_diamond",38),

  ("is_subgraph_free_paw",39),
  ("is_subgraph_free_banner",40),
;
