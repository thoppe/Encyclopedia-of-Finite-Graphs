-- Invariant table

CREATE TABLE IF NOT EXISTS ref_invariant_integer(
    invariant_id INTEGER PRIMARY KEY,  
    function_name TEXT
);

CREATE TABLE IF NOT EXISTS invariant_integer(
    graph_id INTEGER,
    invariant_id INTEGER,
    value INTEGER
);

INSERT OR IGNORE INTO ref_invariant_integer (function_name) VALUES 
    ("diameter"), 
    ("n_edge");


