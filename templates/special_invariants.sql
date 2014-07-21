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

-- Note that this is not a true invariant (as it can change on reindexing)
CREATE TABLE IF NOT EXISTS cycle_basis(
    graph_id   INTEGER,
    cycle_k    UNSIGNED INTEGER,
    idx        UNSIGNED INTEGER
);

CREATE INDEX IF NOT EXISTS "idx_tutte_polynomial"
ON "tutte_polynomial" ("graph_id");

CREATE INDEX IF NOT EXISTS "idx_degree_sequence" 
ON "degree_sequence" ("graph_id");

