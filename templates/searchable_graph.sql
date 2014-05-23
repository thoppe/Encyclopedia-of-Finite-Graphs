CREATE TABLE IF NOT EXISTS graph_search(
       graph_id INTEGER PRIMARY KEY
);

CREATE TABLE IF NOT EXISTS computed(
  function_name STRING PRIMARY KEY,
  is_computed   TINYINT DEFAULT 0
);
