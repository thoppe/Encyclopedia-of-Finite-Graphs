CREATE TABLE IF NOT EXISTS degree_sequence(
    graph_id   INTEGER,
    degree     INTEGER  
);

CREATE TABLE IF NOT EXISTS tutte_polynomial(
    graph_id   INTEGER,
    x_degree   UNSIGNED INTEGER,
    y_degree   UNSIGNED INTEGER,
    coeff      INTEGER
);

CREATE TABLE IF NOT EXISTS fractional_chromatic_number(
    graph_id   INTEGER,
    a          INTEGER,
    b          INTEGER
);

CREATE TABLE IF NOT EXISTS independent_vertex_sets(
    graph_id   INTEGER,
    vertex_map UNSIGNED BIG INTEGER
);

CREATE TABLE IF NOT EXISTS independent_edge_sets(
    graph_id   INTEGER,
    edge_map UNSIGNED BIG INTEGER
);

-- Note that this is not a true invariant (as it can change on reindexing)
CREATE TABLE IF NOT EXISTS cycle_basis(
    graph_id   INTEGER,
    cycle_k    UNSIGNED INTEGER,
    idx        UNSIGNED INTEGER
);

-- Marks if an invariant has been computed

CREATE TABLE IF NOT EXISTS computed(
  function_name TEXT PRIMARY KEY
);


-- Create indices for faster searching

DROP INDEX IF EXISTS "idx_ independent_vertex_sets";
DROP INDEX IF EXISTS "idx_ independent_edge_sets";

CREATE INDEX IF NOT EXISTS "idx_independent_vertex_sets"
ON "independent_vertex_sets" ("graph_id");

CREATE INDEX IF NOT EXISTS "idx_independent_edge_sets"
ON "independent_edge_sets" ("graph_id");

CREATE INDEX IF NOT EXISTS "idx_fractional_chromatic_number"
ON "fractional_chromatic_number" ("graph_id");

CREATE INDEX IF NOT EXISTS "idx_tutte_polynomial"
ON "tutte_polynomial" ("graph_id");

CREATE INDEX IF NOT EXISTS "idx_degree_sequence" 
ON "degree_sequence" ("graph_id");

CREATE INDEX IF NOT EXISTS "idx_cycle_basis" 
ON "cycle_basis" ("graph_id");



