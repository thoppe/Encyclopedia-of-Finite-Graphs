--select count(*) from invariant_integer where invariant_id=27

/*use the largest graphn ("nmax") database to create ref_invariant_val and use these id's across
  all databases. This is not 100% perfect - there may be an (invariant_id,value) pair
  that exists in a n < nmax database but not in nmax, so this method would miss it. 
  But our best bet is to hope that most possibilities exist in  I'm using this 
  assumption so that the id's are easily standardized across all databases.
Maybe a more straightforward way to say this is: a sequence will only be stored
if its n = nmax term is not zero.

*/
/* 
Create ref_invariant, ref_query and query_count in the query database. 
*/
/*
drop table A_equals_B;
drop table A_subsetof_B;
drop table exclude_invariant_val;
drop table query_count;
drop table query_graph;
drop table ref_invariant_val;
drop table ref_query;
drop table temp;
drop table tempcount;

*/

--if n==nmax 
create table ref_invariant_val(
invariant_val_id integer primary key autoincrement,
invariant_id integer,
value integer
);

insert into ref_invariant_val(invariant_id, value)
select invariant_id, value
from invariant_integer
group by 1,2
;
--end if 

create table invariant_integer_2(
graph_id integer not null,
invariant_val_id integer not null
)
;

insert  into invariant_integer_2
select b.graph_id, a.invariant_val_id
from ref_invariant_val  as a
join invariant_integer as b
on a.invariant_id = b.invariant_id
and a.value  = b.value
;

alter table invariant_integer rename to drop_invariant_integer;
alter table invariant_integer_2 rename to invariant_integer;

--drop index idx_invariant_integer;
create unique index idx_invariant_integer on invariant_integer(graph_id asc, invariant_val_id asc);

create table exclude_invariant_val(
invariant_val_id integer primary key
);
insert into exclude_invariant_val
select invariant_val_id 
from ref_invariant_val as a
join (
  select invariant_id
  from ref_invariant_integer
  where function_name in('n_vertex','n_edge')
  )as b
  on a.invariant_id = b.invariant_id
;

/*queries are defined recursively:
for query_level = 1, (query_id,<null>,invariant_val_id) means all graphs with given invariant_val_id
for query_level > 1, (query_id,prev_query_id,invariant_val_id) means all graphs matching prev_query_id and with given invariant_val_id
*/
create table ref_query( 
query_id integer primary key autoincrement,
prev_query_id integer,
query_level integer,
invariant_val_id integer
);

insert into ref_query(query_level, invariant_val_id)
select 1, invariant_val_id
from invariant_integer
where invariant_val_id not in (select invariant_val_id from exclude_invariant_val)
group by 2
;

create unique index idx_ref_query on ref_query(prev_query_id, invariant_val_id);
create index idx_query_level on ref_query(query_level);


--query_count and ref_query will have one row for every possible query
create table query_count(
query_id integer primary key,
query_count_1 integer,
query_count_2 integer,
query_count_3 integer,
query_count_4 integer,
query_count_5 integer,
query_count_6 integer,
query_count_7 integer,
query_count_8 integer,
query_count_9 integer,
query_count_10 integer,
query_count_11 integer,
query_count_12 integer
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
join invariant_integer as b
 on a.invariant_val_id = b.invariant_val_id
;

create index idx_temp_init on temp(graph_id asc, invariant_val_id asc)
;

--create query_graph table 
create table query_graph(
query_id integer ,
prev_query_id integer,
query_level integer,
graph_id integer 
) ;
create unique index idx_query_graph on query_graph(graph_id,query_id)
;
create index idx_query_graph_prev on query_graph(prev_query_id)
;

insert into query_graph
select query_id, null as prev_query_id, 1 as query_level, graph_id
from temp
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

UPDATE query_count SET query_count_{n} =
 (SELECT query_count_nbr from tempcount as a
 where a.query_id = query_count.query_id)
;
delete from tempcount;


--  begin loop over levels j = 2..4 (you'll have to replace the j's below with actual numbers)
create table temp2 (
query_id integer null,
prev_query_id integer,
graph_id integer,
invariant_val_id integer
);


/*this leaves the query_id blank in temp2. inserting into ref_query will take care of the auto-incrementing*/
insert into temp2(prev_query_id, invariant_val_id, graph_id)
select a.query_id as prev_query_id,  b.invariant_val_id, a.graph_id
from temp as a
join invariant_integer as b
  on a.graph_id = b.graph_id
 and a.invariant_val_id < b.invariant_val_id
where b.invariant_val_id not in (select invariant_val_id from exclude_invariant_val)
;
create unique index idx_temp2 on temp2(prev_query_id, invariant_val_id, graph_id);


--insert the new queries from temp2 into ref_query, which will generate a new query_id for them
insert into ref_query(prev_query_id, invariant_val_id, query_level)
select prev_query_id, invariant_val_id, {j} as query_level
from temp2
group by 1,2
;
  
-- now that ref_query has created query_id, update temp2
UPDATE temp2 SET query_id =
 (SELECT query_id
 FROM ref_query
 WHERE ref_query.prev_query_id = temp2.prev_query_id
 AND ref_query.invariant_val_id = temp2.invariant_val_id)
; -- can take a while

--update query_graph
insert into query_graph
select query_id, prev_query_id, {j} as query_level, graph_id
from temp2
;


-- update the counts table
-- if n == nmax
insert into query_count(query_id)
select query_id
from ref_query
where query_level = {j}
; 
-- end if


insert into tempcount
SELECT query_id, count(graph_id) as qc
 FROM temp2
 group by 1
;


UPDATE query_count SET query_count_{n} =   (
 select query_count_nbr from tempcount as a
 where a.query_id = query_count.query_id
 )
where exists (
 select query_count_nbr from tempcount as a
 where a.query_id = query_count.query_id
 )
;
delete from tempcount;

drop table temp;

alter table temp2 rename to temp; 
drop index idx_temp2;
create index idx_temp on temp(invariant_val_id, graph_id);



--end loop over levels



drop table tempcount;




