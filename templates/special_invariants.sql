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

CREATE TABLE IF NOT EXISTS laplacian_polynomial(
    graph_id   INTEGER,
    x_degree   UNSIGNED INTEGER,
    coeff      BIG INTEGER
);

CREATE TABLE IF NOT EXISTS characteristic_polynomial(
    graph_id   INTEGER,
    x_degree   UNSIGNED INTEGER,
    coeff      BIG INTEGER
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

