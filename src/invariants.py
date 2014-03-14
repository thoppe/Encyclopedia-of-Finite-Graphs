import numpy as np
import ast,itertools, os
import subprocess
import networkx as nx
import graph_tool.topology
import graph_tool.draw

import connectivity.connectivity as nx_extra
import sympy

######################### Conversion code ######################### 

def convert_to_numpy(adj,**args):
    N = args["N"]

    possible_edges = (N*(N+1))/2
    edge_map = np.binary_repr(adj, possible_edges)
    edge_int = map(int, edge_map)

    idx = np.triu_indices(N)
    A = np.zeros((N,N),dtype=np.int)
    
    A[idx] = edge_int

    # Works for loopless graphs only
    A += A.T
    return A

def graph_tool_representation(adj, **args):
    A = convert_to_numpy(adj,**args)
    g = graph_tool.Graph(directed=False)
    g.add_vertex(args["N"])
    for edge in zip(*np.where(A)):
        n0, n1 = edge
        if n0>n1:
            g.add_edge(n0,n1)
    return g

def networkx_representation(adj, **args):
    A = convert_to_numpy(adj,**args)
    return nx.from_numpy_matrix(A)

######################### Special invariant code #################

def compress_input(val):
    return str(val).replace(' ','')

def special_cycle_basis(adj,**args):
    g = networkx_representation(adj,**args)
    val = nx.cycle_basis(g)
    return compress_input(val)

def special_degree_sequence(adj,**args):
    A = convert_to_numpy(adj,**args)
    deg = A.sum(axis=0)
    deg.sort()
    return compress_input(deg.tolist())

def special_polynomial_tutte(adj,**args):
    A = convert_to_numpy(adj,**args)
    cmd = os.path.join('src','tutte','tutte_bhkk')
    tutte_args = ' '.join(map(str, [args["N"],] + A.ravel().tolist()))
    cmd += ' ' + tutte_args
    proc = subprocess.Popen([cmd],stdout=subprocess.PIPE,shell=True)
    sval = [[int(x) for x in line.split()] for line in proc.stdout]
    return compress_input(sval)

######################### Invariant code ######################### 

def n_vertex(adj,**args):
    return args["N"]

def n_cycle_basis(adj, **args):
    cycle_b = ast.literal_eval(args["special_cycle_basis"])
    return len(cycle_b)

def is_tree(adj, **args):
    # Trees have no cycles
    cycle_b = ast.literal_eval(args["special_cycle_basis"])
    return len(cycle_b)==0

def girth(adj,**args):
    # Since the cycle basis is the minimal set of fundemental cycles
    # the girth has to be the length of the smallest of these cycles
    # Graphs with no cycles have girth=0 (defined) as placeholder for infinity
    cycle_b = ast.literal_eval(args["special_cycle_basis"])
    if not cycle_b: return 0

    return min(map(len,cycle_b))

def circumference(adj,**args):
    # The circumference is found from the cycle_basis be the largest 
    # direct combination of terms 
    # Graphs with no cycles have cir=0 (defined) as placeholder for infinity
    cycle_b = ast.literal_eval(args["special_cycle_basis"])
    if not cycle_b: return 0

    N = args["N"]

    def combine_cycle(C):
        idx = np.zeros(N,dtype=int)
        for c in C: idx[c] = 1
        return np.where(idx)[0].tolist()
    
    return len(combine_cycle(cycle_b))


def n_edge(adj,**args):
    # Defined this way for loopless simple graphs
    deg = ast.literal_eval(args["special_degree_sequence"])
    return sum(deg) / 2

def n_endpoints(adj,**args):
    # Defined this way for loopless simple graphs
    deg = ast.literal_eval(args["special_degree_sequence"])
    return sum([True for d in deg if d==1])

# Cubic graphs are related to http://oeis.org/A002851
def is_k_regular(adj, **args):
   # Returns the value of k if it is k regular, otherwise 0
    deg = ast.literal_eval(args["special_degree_sequence"])

    if len(set(deg)) == 1:
        return deg[0]
    else:
        return 0

def is_strongly_regular(adj, **args):
    # Check with http://oeis.org/A088741
    # Returns the value of k if it is k strongly regular, otherwise 0
    # Strongly regular graphs satisfy AJ = kJ, where J is a ones matrix
    # Assume that N=1,2 is NOT strongly regular
    N = args["N"]
    if N<=2: return 0
    
    A = convert_to_numpy(adj,**args)
    connections = zip(*np.triu_indices(N,1))

    K = A.sum(axis=0)

    if len(set(K)) != 1:
        return False

    L, V = None, None
   
    for v0,v1 in itertools.combinations(range(N),2):
        common = (A[v0] * A[v1]).sum()
        if A[v0,v1]:
            if L == None: L = common
            if L and common != L: return False
        if not A[v0,v1]:
            if V == None: V = common
            if V and common != V: return False
    return True

def diameter(adj,**args):
    if args["N"]==1: return 0
    g = networkx_representation(adj,**args)
    return nx.diameter(g)

def radius(adj,**args):
    if args["N"]==1: return 0
    g = networkx_representation(adj,**args)
    return nx.radius(g)

def is_eulerian(adj,**args):
    g = networkx_representation(adj,**args)
    return nx.is_eulerian(g)

def is_distance_regular(adj,**args):
    g = networkx_representation(adj,**args)
    return nx.is_distance_regular(g)

def is_planar(adj,**args):
    g = graph_tool_representation(adj,**args)
    return graph_tool.topology.is_planar(g)

def is_bipartite(adj,**args):
    g = graph_tool_representation(adj,**args)
    return graph_tool.topology.is_bipartite(g)

def n_articulation_points(adj,**args):
    g = graph_tool_representation(adj,**args)
    bicomp, art, nc = graph_tool.topology.label_biconnected_components(g)
    return sum(art.a)

def vertex_connectivity(adj,**args):
    g = networkx_representation(adj,**args)
    return nx_extra.global_vertex_connectivity(g)

def edge_connectivity(adj,**args):
    g = networkx_representation(adj,**args)
    return nx_extra.global_edge_connectivity(g)

def is_integral(adj, **args):
    # Check with http://oeis.org/A064731
    # Symbolically determine the char poly and evaluate it on
    # the rounded eigenvalues. A non-zero result is a non-intergral eigenvalue
    # this avoids the "all_close" condition

    A = convert_to_numpy(adj,**args)
    N = args["N"]
    M = sympy.Matrix(A)
    p = M.charpoly()

    # Integer roots
    z_roots = sympy.polys.polyroots.roots(p, filter="Z", multiple=True)
    return N == len(z_roots)

######################### Subgraph code ######################### 

def __generate_KN(n):
    g = graph_tool.Graph(directed=False)
    g.add_vertex(n)
    for i,j in itertools.combinations(range(n),2):
        g.add_edge(i,j)
    return g

def __generate_CN(n):
    g = graph_tool.Graph(directed=False)
    g.add_vertex(n)
    labels = range(n)
    for i in range(-1,n-1):
        g.add_edge(labels[i],labels[i+1])
    return g

_complete_graphs = [__generate_KN(n) for n in xrange(0, 15)]
_cycle_graphs    = [__generate_CN(n) for n in xrange(0, 15)]
_has_subgraph = graph_tool.topology.subgraph_isomorphism

def _is_subgraph_free(subg):
    subg_n = len([x for x in subg.vertices()])
    
    def f(adj,**args):
        # Early breakout if input graph is too small
        if args["N"] < subg_n: return 1
        g = graph_tool_representation(adj,**args)
        return len(_has_subgraph(subg,g)[0])==0
    return f

# is_subgraph_free_K3=1, OEIS:A024607
is_subgraph_free_K3 = _is_subgraph_free(_complete_graphs[3])
is_subgraph_free_K4 = _is_subgraph_free(_complete_graphs[4])
is_subgraph_free_K5 = _is_subgraph_free(_complete_graphs[5])

is_subgraph_free_C4 = _is_subgraph_free(_cycle_graphs[4])
is_subgraph_free_C5 = _is_subgraph_free(_cycle_graphs[5])
is_subgraph_free_C6 = _is_subgraph_free(_cycle_graphs[6])
is_subgraph_free_C7 = _is_subgraph_free(_cycle_graphs[7])
is_subgraph_free_C8 = _is_subgraph_free(_cycle_graphs[8])
is_subgraph_free_C9 = _is_subgraph_free(_cycle_graphs[9])
is_subgraph_free_C10= _is_subgraph_free(_cycle_graphs[10])

def chromatic_number(adj,**args):
    # Return 0 for the singleton graph (it's really infinity)
    if args["N"]==1: return 0

    # Read in the tutte poly
    string_T =  args["special_polynomial_tutte"]
    T = ast.literal_eval(string_T)
    C = [row[0] if row else 0 for row in T]

    def eval_chromatic(T,k):
        # The chromatic polynomial use y=0, so only the top row
        # and evaluates T(x,y) at C(k) = T(x=1-k,y=0)*(-1)**N*(1-k)
        terms = [c*(1-k)**exponent for exponent,c in enumerate(C)]
        c = sum(terms)*(-1)**(args["N"])*(1-k)
        return c   

    for k in range(1,args["N"]+1):
        if eval_chromatic(T,k) != 0:
            return k

    msg = "Should have exited by now"
    raise ValueError(msg)

######################### Bliss code ######################### 

def automorphism_group_n(adj,**args):
    ''' Calls the BLISS program from the command line '''

    A = convert_to_numpy(adj,**args)
    edges = np.where(A)
    s = ["p edge {N} {}".format(A.sum()/2,**args)]
    for i,j in zip(*edges):
        if i<=j:
            s.append("e {} {}".format(i+1,j+1))
    s_echo = '"%s"'%('\n'.join(s))
    cmd = "echo %s | src/bliss/bliss" % s_echo
    proc = subprocess.Popen([cmd],stdout=subprocess.PIPE,shell=True)
    for line in proc.stdout:
        if "|Aut|" in line:
            return int(line.split()[-1])

    err = "BLISS failed with adj: "+adj
    raise ValueError(err)


######################### Test code ######################### 
    
if __name__ == "__main__":

    # Function testing here

    N = 7
    adj = 14781504
    args= {"N":N}

    args["special_cycle_basis"] = special_cycle_basis(adj,**args)
    print "n_cycle_basis:",n_cycle_basis(adj,**args)
    print "Girth: ", girth(adj, **args)
    print "Circumference: ", circumference(adj, **args)

    print "Vertex connectivity: ", vertex_connectivity(adj, **args)
    print "Edge   connectivity: ", edge_connectivity(adj, **args)

    print "is_strongly_regular: ", is_strongly_regular(adj, **args)
    print "is_integral:", is_integral(adj, **args)
    print "AUT: ", automorphism_group_n(adj,**args)
    print "is_integral: ", is_integral(adj, **args)

    p = special_polynomial_tutte(adj, **args)
    args["special_polynomial_tutte"] = p
    print "Chromatic number: ", chromatic_number(adj, **args)

    A  = convert_to_numpy(adj,**args) 
    gx = networkx_representation(adj,**args)
    gt = graph_tool_representation(adj,**args)

    print "is_planar",is_planar(adj,**args), is_bipartite(adj,**args)
    print "n_articulation_points",n_articulation_points(adj,**args)

    def viz_graph(g):
        pos = graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
        graph_tool.draw.graph_draw(g,pos)

    viz_graph(gt)
    

