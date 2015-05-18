-- Graph (with fixed N) object for database

CREATE TABLE IF NOT EXISTS graph(
       graph_id   INTEGER PRIMARY KEY AUTOINCREMENT,
       adj        UNSIGNED BIG INT NOT NULL UNIQUE
);

-- Invariant table for integers

CREATE TABLE IF NOT EXISTS invariant_integer(
      graph_id   INTEGER PRIMARY KEY
);

-- Marks if an invariant has been computed

CREATE TABLE IF NOT EXISTS computed(
  function_name TEXT PRIMARY KEY
);
