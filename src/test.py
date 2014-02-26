import helper_functions

cmd1 = '''
SELECT COUNT(*) FROM invariant_integer WHERE
(invariant_id=7 AND value=1) AND 
(invariant_id=6 AND value=1) AND 
(invariant_id=2 AND value>=10)
'''
conn = helper_functions.load_graph_database(7)
conn.execute(cmd1)



print conn
