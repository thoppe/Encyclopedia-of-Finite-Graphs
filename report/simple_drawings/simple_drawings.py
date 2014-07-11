import itertools
import graph_tool as gt
import graph_tool.draw
import src.invariants as inv
import numpy as np

# Combines disjoint graphs
def add_to(g,a):
    offset = len(list(g.vertices()))
    n_a = len(list(a.vertices()))
    g.add_vertex(n_a)
    for edge in a.edges():
        i,j = map(int, [edge.source(), edge.target()])
        g.add_edge(i+offset, j+offset)

g = gt.Graph(directed=False)    

input_g = [inv._diamond_graph,
           inv._bowtie_graph,
           inv._open_bowtie_graph,
           inv._bull_graph]

for h in input_g:
    add_to(g,h)

pos = gt.draw.sfdp_layout(g, cooling_step=0.99)


'''
counter = 0
spacing = 3

for hn, h in enumerate(input_g):
    h_pos = gt.draw.sfdp_layout(h, cooling_step=0.99)
    hp = np.array([h_pos[x] for x in h.vertices()])
    hp -= hp.mean(axis=0)
    
    for k in h.vertices():       
        pos[g.vertex(counter)] = hp[int(k)] + [hn*spacing,0]
        counter += 1
'''

f_png = "combined_subgraphs.png"
pos = gt.draw.sfdp_layout(g, cooling_step=0.99)

graph_tool.draw.graph_draw(g,pos,output=f_png)
graph_tool.draw.graph_draw(g,pos)

