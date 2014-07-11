import itertools
import graph_tool as gt
import graph_tool.draw
import src.invariants as inv

# Combines disjoint graphs
def add_to(g,a):
    offset = len(list(g.vertices()))
    n_a = len(list(a.vertices()))
    g.add_vertex(n_a)
    for edge in a.edges():
        i,j = map(int, [edge.source(), edge.target()])
        g.add_edge(i+offset, j+offset)

g = gt.Graph(directed=False)    
add_to(g,inv._bowtie_graph)
add_to(g,inv._diamond_graph)
add_to(g,inv._open_bowtie_graph)
add_to(g,inv._bull_graph)

f_png = "combined_subgraphs.png"
pos = gt.draw.sfdp_layout(g, cooling_step=0.99)
help( gt.draw.sfdp_layout )

print pos.a, pos.fa, pos.ma
exit()
print pos.get_array()
help(pos)

for n in pos:
    print n

for n in g.vertices():
    print dir(g.vertex(n))
#graph_tool.draw.graph_draw(g,pos,output=f_png)
