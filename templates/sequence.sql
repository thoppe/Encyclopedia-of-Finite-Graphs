-- Keeps tracks of all unique values for each invariant
CREATE TABLE IF NOT EXISTS unique_invariant_val(
  unique_invariant_id integer primary key autoincrement,
  invariant_val_id integer,
  value integer
);

--- Tracks if various items have been computed
CREATE TABLE IF NOT EXISTS computed(
  function_name STRING,
  compute_type  STRING, 
  has_computed TINYINT DEFAULT false
);

/*
--- Tracks if various sequence terms have been computed
--- for now this only tracks the unique invariants
CREATE TABLE IF NOT EXISTS computed(
  function_name STRING PRIMARY KEY,  
  has_computed TINYINT DEFAULT false
);


CREATE TABLE IF NOT EXISTS exclude_invariant_val(
  unique_invariant_id INTEGER PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE IF NOT EXISTS ref_sequence( 
  sequence_id INTEGER PRIMARY KEY AUTOINCREMENT,
  prev_query_id INTEGER,
  query_level INTEGER NOT NULL,
  unique_invariant_id INTEGER,
  conditional STRING NOT NULL,
  value INTEGER NOT NULL,

  non_zero_terms INTEGER
);

-- This needs to be as long as max N
CREATE TABLE IF NOT EXISTS sequence(
  sequence_id INTEGER PRIMARY KEY,
  s1  INTEGER,
  s2  INTEGER,
  s3  INTEGER,
  s4  INTEGER,
  s5  INTEGER,
  s6  INTEGER,
  s7  INTEGER,
  s8  INTEGER,
  s9  INTEGER,
  s10 INTEGER,

  hash TEXT
);  
*/

