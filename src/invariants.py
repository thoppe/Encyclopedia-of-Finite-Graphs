import numpy as np
import ast,itertools, os
#from subprocess import Popen, PIPE, STDOUT
import subprocess
import networkx as nx
import graph_tool.topology
import graph_tool.draw

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

######################### Special invariant code #################

def compress_input(val):
    return str(val).replace(' ','')

def special_cycle_basis(adj,**args):
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
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
    # is_tree == n_cycle_basis=0
    cycle_b = ast.literal_eval(args["special_cycle_basis"])
    return len(cycle_b)

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

def diameter(adj,**args):
    if args["N"]==1: return 0
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return nx.diameter(g)

def radius(adj,**args):
    if args["N"]==1: return 0
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return nx.radius(g)

def is_eulerian(adj,**args):
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
    return nx.is_eulerian(g)

def is_distance_regular(adj,**args):
    A = convert_to_numpy(adj,**args)
    g = nx.from_numpy_matrix(A)
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
        s.append("e {} {}".format(i+1,j+1))
    s_echo = '"%s"'%('\n'.join(s))
    cmd = "echo %s | src/bliss/bliss" % s_echo
    proc = subprocess.Popen([cmd],stdout=subprocess.PIPE,shell=True)
    for line in proc.stdout:
        if "|Aut|" in line:
            return int(line.split()[-1])

    err = "BLISS failed with adj: "+adj
    raise ValueError(err)
    
if __name__ == "__main__":

    def viz_graph(g):
        pos = graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
        graph_tool.draw.graph_draw(g,pos)

    # Function testing here

    N = 7
    adj = 14781504
    args= {"N":N}

    print "AUT: ", automorphism_group_n(adj,**args)
    
    p = special_polynomial_tutte(adj, **args)
    args["special_polynomial_tutte"] = p
    print "Chromatic number: ", chromatic_number(adj, **args)

    A  = convert_to_numpy(adj,**args)    
    gx = nx.from_numpy_matrix(A)
    g = graph_tool_representation(adj,**args)

    #print "n_cycle_basis:",n_cycle_basis(adj,**args)
    print "is_planar",is_planar(adj,**args), is_bipartite(adj,**args)
    print "n_articulation_points",n_articulation_points(adj,**args)
    viz_graph(g)
    

