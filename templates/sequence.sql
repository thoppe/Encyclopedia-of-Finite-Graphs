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

-- This needs to be as long as max N

CREATE TABLE IF NOT EXISTS sequence(
  sequence_id INTEGER,  
  query_level INTEGER,
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

  UNIQUE (sequence_id, query_level)
);  

/* There can be more than on entry with a given sequence_id,
this is how multi-levels are recorded */

CREATE TABLE IF NOT EXISTS ref_sequence_level1( 
  sequence_id INTEGER PRIMARY KEY AUTOINCREMENT,

  unique_invariant_id INTEGER,
  conditional STRING NOT NULL,
  invariant_val_id NOT NULL,
  value INTEGER NOT NULL,

  UNIQUE (invariant_val_id, value, conditional)
);

CREATE TABLE IF NOT EXISTS ref_sequence_level2( 
  sequence_id INTEGER PRIMARY KEY AUTOINCREMENT,

  unique_invariant_id1 INTEGER,
  conditional1 STRING1 NOT NULL,
  invariant_val_id1 NOT NULL,
  value1 INTEGER NOT NULL,

  unique_invariant_id2 INTEGER,
  conditional2 STRING NOT NULL,
  invariant_val_id2 NOT NULL,
  value2 INTEGER NOT NULL,

  UNIQUE (invariant_val_id1, value1, conditional1,
          invariant_val_id2, value2, conditional2)
);


CREATE TABLE IF NOT EXISTS stat_sequence( 
  sequence_id INTEGER PRIMARY KEY,
  query_level INTEGER NOT NULL,
  non_zero_terms INTEGER, 
  UNIQUE (sequence_id, query_level)
);

--DROP TABLE IF EXISTS relations;

CREATE TABLE IF NOT EXISTS relations( 
  relation_id INTEGER PRIMARY KEY AUTOINCREMENT,
  s1_id INTEGER NOT NULL,
  s2_id INTEGER NOT NULL,
  subset     TINYINT,
  exclusive  TINYINT,
  equal      TINYINT,
  UNIQUE (s1_id, s2_id)
);


