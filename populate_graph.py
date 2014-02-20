import sqlite3, subprocess

args = {"N":4}
database_name = "graph{N}".format(**args)
conn = sqlite3.connect('database/{}.db'.format(database_name))

def nauty_simple_graph_itr(N):
    ''' Creates a generator for all simple graphs using nauty '''

    cmd = "geng {N} -cq | showg -eq -l0"
    cmd = cmd.format(**args)

    proc = subprocess.Popen([cmd],stdout=subprocess.PIPE,shell=True)
    while True:
        header_line = proc.stdout.readline()
        edge_line   = proc.stdout.readline()
        yield edge_line.strip()
        
        if not header_line: break

for k,edge_list in enumerate(nauty_simple_graph_itr(**args)):
    print edge_list


