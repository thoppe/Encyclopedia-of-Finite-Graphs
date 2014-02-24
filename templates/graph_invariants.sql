-- Invariant reference table for integers

CREATE TABLE IF NOT EXISTS ref_invariant_integer(
    invariant_id INTEGER PRIMARY KEY,  
    function_name TEXT, 
    UNIQUE (function_name)
);


-- Invariant table for integers

CREATE TABLE IF NOT EXISTS invariant_integer(
    graph_id INTEGER,
    invariant_id INTEGER,
    value INTEGER
);

-- List of invariants

INSERT OR IGNORE INTO ref_invariant_integer (function_name) VALUES 
    ("diameter"), 
    ("n_edge");


