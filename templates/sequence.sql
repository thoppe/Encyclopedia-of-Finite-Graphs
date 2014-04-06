-- Keeps tracks of all unique values for each invariant
CREATE TABLE IF NOT EXISTS unique_invariant_val(
  invariant_id integer primary key autoincrement,
  invariant_val_id integer,
  value integer
);

--- Tracks if various terms have been computed to save time
CREATE TABLE IF NOT EXISTS computed(
  function_name STRING PRIMARY KEY,  
  has_computed TINYINT DEFAULT false
);

CREATE TABLE IF NOT EXISTS exclude_invariant_val(
  invariant_val_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE IF NOT EXISTS ref_query( 
  query_id INTEGER PRIMARY KEY AUTOINCREMENT,
  prev_query_id INTEGER,
  query_level INTEGER,
  invariant_val_id INTEGER
);
