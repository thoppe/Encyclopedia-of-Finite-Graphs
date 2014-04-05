
-- Keeps tracks of all unique values for each invariant

CREATE TABLE IF NOT EXISTS unique_invariant_val(
  unique_invariant_id integer primary key autoincrement,
  invariant_id integer,
  value integer
);

CREATE TABLE IF NOT EXISTS computed(
  function_name STRING PRIMARY KEY,  
  has_computed TINYINT DEFAULT false
);

