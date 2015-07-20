CREATE TABLE IF NOT EXISTS distinct_sequence(
    function_name STRING,
    N             INTEGER,
    coeff         INTEGER,
    UNIQUE (function_name, N)
);
