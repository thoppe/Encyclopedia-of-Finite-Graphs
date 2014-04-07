CREATE TABLE IF NOT EXISTS exclude_invariant_val(
  unique_invariant_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE IF NOT EXISTS ref_query( 
  query_id INTEGER PRIMARY KEY AUTOINCREMENT,
  prev_query_id INTEGER,
  query_level INTEGER,
  invariant_val_id INTEGER
);
