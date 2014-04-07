import sqlite3, logging, argparse, os, collections, ast
import subprocess, itertools
import numpy as np
from helper_functions import load_graph_database, grab_all, grab_scalar
from helper_functions import attach_ref_table, load_sql_script, grab_vector
from helper_functions import attach_table, generate_database_name
import pyparsing as pypar

desc   = "Verify the sequences produced are the correct ones"
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('n',type=int,default=5,
                    help="Maximum graph size n to compute sequences")
parser.add_argument('-f','--force',default=False,action='store_true')
cargs = vars(parser.parse_args())

excluded_terms = ["n_vertex","n_edge","n_endpoints",
                  "is_subgraph_free_C6","is_subgraph_free_C7",
                  "is_subgraph_free_C8","is_subgraph_free_C9",
                  "is_subgraph_free_C10",]

# Start the logger
logging.root.setLevel(logging.INFO)

# Connect to the database and add structure info
f_seq_database = "database/sequence.db"
seq_conn = sqlite3.connect(f_seq_database, check_same_thread=False)
attach_ref_table(seq_conn)

# Load the template
f_sequence_template = "templates/sequence.sql"
load_sql_script(seq_conn, f_sequence_template)

# Attach the invariant database to the sequence database
# use only the n'th db for now
#f_db = generate_database_name(cargs["n"])
#attach_table(seq_conn, f_db, "graph{n}".format(**cargs))

# Load the invariant database files
graph_conn = collections.OrderedDict()
for n in range(1, cargs["n"]+1):
    graph_conn[n] = load_graph_database(n)
    attach_ref_table(graph_conn[n])

cmd_invar = '''SELECT invariant_id,function_name FROM ref_invariant_integer'''
invariant_dict = dict(grab_all(graph_conn[1],cmd_invar))

# Find out what has been computed
cmd_select_compute = '''SELECT * FROM computed'''
compute_dict = dict(grab_all(seq_conn, cmd_select_compute))
if cargs["force"]: compute_dict = {}

# Find and update the unique invariant values

cmd_find_unique = '''
SELECT invariant_id, value FROM invariant_integer
GROUP BY 1,2;'''

cmd_insert_unique = '''
INSERT OR REPLACE INTO unique_invariant_val(invariant_val_id, value)
VALUES (?,?)'''

cmd_mark_unique_computed = '''
INSERT OR REPLACE INTO computed VALUES 
("unique_invariant_val", "1")'''

name = "unique_invariant_val"

if (name not in compute_dict or 
    not compute_dict[name]):
    
    for n,gc in graph_conn.items():
        msg = '''Updating {} for graph set {}'''
        logging.info(msg.format(name,n))
        items = grab_all(gc, cmd_find_unique)
        seq_conn.executemany(cmd_insert_unique, items)

    seq_conn.execute(cmd_mark_unique_computed)
    seq_conn.commit()

# Clear the previous marked excluded terms
seq_conn.execute("DELETE FROM exclude_invariant_val")

# Attach the graph database to the sequence database
#f_db = generate_database_name(cargs["n"])
#attach_table(seq_conn, f_db, "graph")

# Mark the excluded terms
cmd_exclude = '''
INSERT INTO exclude_invariant_val
SELECT unique_invariant_id 
FROM unique_invariant_val as a
JOIN (
  SELECT invariant_id FROM ref_invariant_integer
  WHERE function_name IN ({})
  ) AS b
ON a.invariant_val_id = b.invariant_id;'''

excluded_string = str(excluded_terms)[1:-1]
logging.info("Ignoring invariants %s"%excluded_string)
seq_conn.execute(cmd_exclude.format(excluded_string))
seq_conn.commit()

# Get known lvl 1 sequences
cmd_select_known_lvl1 = '''
SELECT unique_invariant_id FROM ref_sequence
WHERE query_level = 1'''
known_lvl1 = set(grab_vector(seq_conn,cmd_select_known_lvl1))

# WORKING HERE
# Get all level n>1 sequences that need to be computed
cmd_select_nlvl_sequence = '''
SELECT sequence_id FROM ref_sequence 
WHERE query_level={} AND non_zero_terms>=4'''
#n = 2
#valid_previous = grab_all(seq_conn, cmd_select_nlvl_sequence.format(n-1))
#for 
#def get_n_level_sequence(n):
#print known_lvl1
#exit()


cmd_select_lvl_1 = '''
SELECT unique_invariant_id, invariant_val_id, value
FROM unique_invariant_val
WHERE 
unique_invariant_id NOT IN
(SELECT unique_invariant_id FROM exclude_invariant_val);'''

seq_lvl1 = grab_all(seq_conn, cmd_select_lvl_1)
seq_lvl1 = [x for x in seq_lvl1 if x[0] not in known_lvl1]

msg = "Computing {} new level one sequences"
logging.info(msg.format(len(seq_lvl1)))

# Compute these sequences

cmd_count = '''
SELECT COUNT(*) FROM invariant_integer as a 
LEFT JOIN ref_invariant_integer as b
ON  a.invariant_id  = b.invariant_id 
WHERE b.function_name = "{function_name}" 
AND a.value {conditional} {value}
'''

def grab_sequence(**args):
    cmd = cmd_count.format(**args)

    vec = []
    for n in graph_conn:
        sol = grab_scalar(graph_conn[n], cmd)
        vec.append(sol)

    return vec

insert_text = ','.join(["s%i"%n for n in graph_conn])
cmd_insert_sequence = '''
INSERT INTO sequence (sequence_id, %s) VALUES ({seq_id},{seq})'''%insert_text
cmd_insert_ref_sequence = '''
INSERT INTO ref_sequence 
(query_level, unique_invariant_id, conditional, value, non_zero_terms) 
VALUES (1, {unique_id}, "{conditional}", {value}, {non_zero})'''

for unique_id, invariant_id, value in seq_lvl1:

    args = {
        "unique_id":unique_id,
        "conditional":"=",
        "function_name":invariant_dict[invariant_id],
        "value":value}

    seq = grab_sequence(**args)

    args["non_zero"] = len([1 for x in seq if x])

    cursor = seq_conn.execute(cmd_insert_ref_sequence.format(**args))

    args["seq_id"] = cursor.lastrowid
    args["seq"] = str(seq)[1:-1]

    seq_conn.execute(cmd_insert_sequence.format(**args))
    
    msg = "New sequence id({seq_id:d}), {function_name}{conditional}{value}, ({seq})"
    logging.info(msg.format(**args))

    seq_conn.commit()

    
exit()

########################################################################

exit()

# Fill up ref_query
cmd_push_into_ref_q = '''
drop table if exists invariant_integer_x;

create table invariant_integer_x(
   graph_id integer not null,
   invariant_val_id integer not null,
   value integer not null
);

insert into invariant_integer_x
select b.graph_id, a.invariant_val_id, b.value
from unique_invariant_val  as a
join invariant_integer as b
on a.invariant_val_id = b.invariant_id
and a.value  = b.value;

--alter table invariant_integer rename to drop_invariant_integer;
--alter table invariant_integer_2 rename to invariant_integer_x;

--drop index idx_invariant_integer;
create unique index idx_invariant_integer_x on invariant_integer_x
(graph_id asc, invariant_val_id asc);

insert into ref_query(query_level, invariant_val_id)
select 1, invariant_val_id
from invariant_integer_x
where invariant_val_id not in 
(select unique_invariant_id from exclude_invariant_val)
group by invariant_val_id;


create unique index idx_ref_query on ref_query(prev_query_id, invariant_val_id);
create index idx_query_level on ref_query(query_level);

--query_count and ref_query will have one row for every possible query
create table query_count(
query_id integer primary key,
query_count_1 integer,
query_count_2 integer,
query_count_3 integer,
query_count_4 integer,
query_count_5 integer
);


insert into query_count(query_id) --starts off having just the level 1 queries
select query_id
from ref_query
;

create unique index idx_query_count on query_count (query_id)
;


create table temp (
query_id integer,
invariant_val_id integer,
graph_id integer
);

insert into temp
select query_id, a.invariant_val_id, graph_id
from ref_query as a
join invariant_integer_x as b
 on a.invariant_val_id = b.invariant_val_id
;

create index idx_temp_init on temp(graph_id asc, invariant_val_id asc)
;

-- update the counts table
create table tempcount(
query_id integer primary key, 
query_count_nbr integer
);
insert into tempcount
SELECT query_id, count(graph_id)
 FROM temp
 group by 1
;
create unique index idx_tempcount on tempcount(query_id);

UPDATE query_count SET query_count_1 =
 (SELECT query_count_nbr from tempcount as a
 where a.query_id = query_count.query_id);
;
--drop table tempcount;


'''
seq_conn.executescript(cmd_push_into_ref_q)
seq_conn.commit()


