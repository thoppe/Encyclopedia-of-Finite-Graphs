-- Graph (with fixed N) object for database

CREATE TABLE IF NOT EXISTS graph(
       graph_id   INTEGER PRIMARY KEY AUTOINCREMENT,
       adj        UNSIGNED BIG INT NOT NULL
);


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
    value INTEGER
    --PRIMARY KEY (graph_id, invariant_id)
);

CREATE UNIQUE INDEX IF NOT EXISTS "idx_invariant_integer" 
ON "invariant_integer" ("graph_id" ASC, "invariant_id" ASC);

CREATE UNIQUE INDEX IF NOT EXISTS "idx_ref_invariant_integer" 
ON "ref_invariant_integer" ("invariant_id" ASC);


-- Unique values for the invariants, needed as separate table for combinations
CREATE TABLE IF NOT EXISTS invariant_integer_unique(
    invariant_id INTEGER,
    unique_value INTEGER,
    PRIMARY KEY (invariant_id, unique_value)
);

-- List of invariants

INSERT OR IGNORE INTO ref_invariant_integer (function_name) VALUES 
    ("n_vertex"),
    ("diameter"), 
    ("n_edge"),
    ("radius"),
    ("is_eulerian"), 
    ("is_distance_regular"),    
    ("is_planar"),
    ("is_bipartite"),
    ("n_articulation_points");
