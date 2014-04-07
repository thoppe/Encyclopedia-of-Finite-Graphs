-- Keeps tracks of all unique values for each invariant
CREATE TABLE IF NOT EXISTS unique_invariant_val(
  unique_invariant_id integer primary key autoincrement,
  invariant_val_id integer,
  value integer
);

--- Tracks if various sequence terms have been computed
--- for now this only tracks the unique invariants
CREATE TABLE IF NOT EXISTS ref_computed(
  function_name STRING PRIMARY KEY,  
  has_computed TINYINT DEFAULT false
);


CREATE TABLE IF NOT EXISTS exclude_invariant_val(
  unique_invariant_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE IF NOT EXISTS ref_query( 
  query_id INTEGER PRIMARY KEY AUTOINCREMENT,
  prev_query_id INTEGER,
  query_level INTEGER,
  invariant_val_id INTEGER
);
