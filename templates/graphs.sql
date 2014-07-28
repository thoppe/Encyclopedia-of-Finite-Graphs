-- Graph (with fixed N) object for database

CREATE TABLE IF NOT EXISTS graph(
       graph_id   INTEGER PRIMARY KEY AUTOINCREMENT,
       adj    UNSIGNED BIG INT NOT NULL
);

-- Invariant table for integers

CREATE TABLE IF NOT EXISTS invariant_integer(
      graph_id   INTEGER PRIMARY KEY
);

--CREATE UNIQUE INDEX IF NOT EXISTS "idx_invariant_integer" 
--ON "invariant_integer" ("graph_id" ASC, "invariant_id" ASC);
--CREATE INDEX IF NOT EXISTS "idx_invariant_integer_values" 
--ON "invariant_integer" ("invariant_id" ASC, "value" ASC);

-- Marks if an invariant has been computed

CREATE TABLE IF NOT EXISTS computed(
  function_name TEXT PRIMARY KEY
);
