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
pos = gt.draw.fruchterman_reingold_layout(g,a=20,scale=1.,circular=True)
inv.viz_graph(g, output=f_png)
