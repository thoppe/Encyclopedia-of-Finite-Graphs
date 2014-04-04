-- Graph (with fixed N) object for database

CREATE TABLE IF NOT EXISTS graph(
       graph_id   INTEGER PRIMARY KEY AUTOINCREMENT,
       adj        UNSIGNED BIG INT NOT NULL,
 
       special_cycle_basis STRING,
       special_degree_sequence STRING,
       special_polynomial_tutte STRING
);

-- Special invariants reference table (to mark computation)
CREATE TABLE IF NOT EXISTS ref_special_invariant(
    function_name STRING PRIMARY KEY,  
    computed TINYINT DEFAULT false
);

INSERT OR IGNORE INTO ref_special_invariant (function_name) VALUES 
    ("special_cycle_basis"),
    ("special_degree_sequence"),
    ("special_polynomial_tutte");

-- Invariant table for integers

CREATE TABLE IF NOT EXISTS invariant_integer(
    graph_id INTEGER,
    invariant_id INTEGER,
    value INTEGER
    --PRIMARY KEY (graph_id, invariant_id)
);

CREATE UNIQUE INDEX IF NOT EXISTS "idx_invariant_integer" 
ON "invariant_integer" ("graph_id" ASC, "invariant_id" ASC);

CREATE INDEX IF NOT EXISTS "idx_invariant_integer_values" 
ON "invariant_integer" ("invariant_id" ASC, "value" ASC);

-- Marks if an invariant has been computed

CREATE TABLE IF NOT EXISTS computed(
  function_name TEXT PRIMARY KEY
);
