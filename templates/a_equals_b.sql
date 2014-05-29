/*
Two queries are "equal" if they return the same set of graphs. This script finds equal queries **for a given n**. A seperate code would be needed to see if A=B across all n. 
*/
create table A_equals_B(
a_query_id integer,
b_query_id integer
)
;

--create an "augmented" version of ref_query with a few additional useful columns 
create table ref_query_aug(
query_id integer primary key,
prev_query_id integer,
query_level integer, 
invariant_val_id integer, 
invariant_id integer, 
prev_invariant_val_id integer,
prev_invariant_id integer 
)
;
insert into ref_query_aug
select Q.*, invariant_id, null, null
from ref_query as Q
join ref_invariant_val as i 
on Q.invariant_val_id = i.invariant_val_id
where query_level = 1
;
insert into ref_query_aug
select Q.*, P.invariant_val_id, P.invariant_id
from (select q.*, invariant_id from ref_query as q join ref_invariant_val as i on q.invariant_val_id = i.invariant_val_id) as Q 
join (select q.query_id, q.invariant_val_id, invariant_id from ref_query as q join ref_invariant_val as i on q.invariant_val_id = i.invariant_val_id) as P  
on Q.prev_query_id = P.query_id
where Q.query_level > 1
;
 
/*
try_pairs contains candidate matches for A=B based on the following criteria:
(1) A and B must have the same number of graphs
(2) The first level should not be comparing the same invariant (ie  a graph can't have radius = 4 and radius = 5)
*/
create table try_pairs(
a_query_id integer,
b_query_id integer 
)
;
insert into try_pairs
select a.query_id as a_query_id, b.query_id as b_query_id
from 
(select q.query_id, q.query_count_1, invariant_id, prev_invariant_id
from query_count as q
join ref_query_aug as r 
on q.query_id = r.query_id
) as a
join
(select q.query_id, q.query_count_1, invariant_id, prev_invariant_id
from query_count as q
join ref_query_aug as r 
on q.query_id = r.query_id
) as b
on a.query_id<> b.query_id
and a.query_count_{n} = b.query_count_{n}
and coalesce(a.prev_invariant_id,a.invariant_id) <> coalesce(b.prev_invariant_id,b.invariant_id)
; --this coalesce statement wouldn't be valid for levels > 2 


create unique index idx_try_pairs on try_pairs(a_query_id, b_query_id)
;


/*
We know that if (a,b) \in try_pairs, then if all values in a match to a value in b,
then a = b. 
*/
insert into A_equals_B
select a_query_id, b_query_id
from 
(select p.rowid, a_query_id, b_query_id, graph_id
from try_pairs as p 
join query_graph as g 
on p.a_query_id = g.query_id
) as A
left join query_graph as B 
on A.b_query_id = B.query_id 
and A.graph_id = B.graph_id
group by 1,2 
having sum(case when B.query_id is null then 1 else 0 end) == 0
;
--1.2 min graph 8 

drop table ref_query_aug
;

