/*
If A and B are equal queries, you may want to review what they actually mean. This is a simple way to view their plain English definitions
*/

select query_id, prev_query_id, function_name, value 
from ref_query as q
join ref_invariant_val as v
on q.invariant_val_id = v.invariant_val_id
join ref_invariant_integer as i
on v.invariant_id = i.invariant_id
where query_id in (1, 65)
;
