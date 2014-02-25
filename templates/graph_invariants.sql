-- Invariant reference table for integers

CREATE TABLE IF NOT EXISTS ref_invariant_integer(
    invariant_id INTEGER PRIMARY KEY,  
    function_name TEXT,
    computed TINYINY DEFAULT false,
    UNIQUE (function_name)
);


-- Invariant table for integers

CREATE TABLE IF NOT EXISTS invariant_integer(
    graph_id INTEGER,
    invariant_id INTEGER,
    value INTEGER,
    PRIMARY KEY (graph_id, invariant_id)
);

-- List of invariants

INSERT OR IGNORE INTO ref_invariant_integer (function_name) VALUES 
    ("diameter"), 
    ("n_edge"),
    ("radius"),
    ("is_eulerian"), 
    ("is_distance_regular"),    
    ("is_planar"),
    ("is_bipartite"),
    ("n_articulation_points");

