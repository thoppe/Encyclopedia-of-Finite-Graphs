-- Graph (with fixed N) object for database

CREATE TABLE IF NOT EXISTS graph(
       graph_id   INTEGER PRIMARY KEY AUTOINCREMENT,
       adj        UNSIGNED BIG INT NOT NULL UNIQUE
);

-- Invariant table for integers
CREATE TABLE IF NOT EXISTS invariant_integer(
    graph_id      INTEGER NOT NULL,
    invariant_id  INTEGER NOT NULL,
    value         INTEGER,
    PRIMARY KEY (graph_id, invariant_id)
);

-- Integer invariant function names
CREATE TABLE IF NOT EXISTS invariant_integer_functions (
    invariant_id INTEGER PRIMARY KEY AUTOINCREMENT,
    function_name TEXT UNIQUE,
    -- Marks if an invariant has been computed
    is_computed BOOL DEFAULT 0
);
