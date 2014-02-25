-- Base sequence values

CREATE TABLE IF NOT EXISTS ref_invariant_integer_unique(
    max_n INTEGER PRIMARY KEY
);

-- Default arguments
INSERT OR IGNORE INTO ref_invariant_integer_unique (max_n) VALUES (0);


CREATE TABLE IF NOT EXISTS invariant_integer_unique(
    invariant_id INTEGER,
    unique_value INTEGER,
    PRIMARY KEY (invariant_id, unique_value)
);

CREATE TABLE IF NOT EXISTS invariant_integer_sequence(
    seq_id    INTEGER PRIMARY KEY AUTOINCREMENT,   
    query     TEXT,
    seq       TEXT NULL,  
    max_n     INTEGER DEFAULT 0,  
    OEIS_search TEXT NULL,
    UNIQUE(query)
);

