import itertools
import os
import sys
import fractions
import subprocess
import collections

import networkx as nx
import numpy as np
import sympy
import pulp

from functools import wraps
from helper_functions import require_arguments


try:
    import graph_tool.topology
    import graph_tool.draw
except ImportError:
    print "ERROR: The module graph_tool must be installed externally."
    sys.exit(1)

__script_dir = os.path.dirname(os.path.realpath(__file__))

####################### Invariant requirements ####################
# Next to each function define any extra requirements needed to be passed
invariant_requirements = collections.defaultdict(list)

######################### Conversion code #########################

def viz_graph(g, pos=None, **kwargs):
    if pos is None:
        pos = graph_tool.draw.sfdp_layout(g, cooling_step=0.99)
    graph_tool.draw.graph_draw(g, pos, **kwargs)

@require_arguments("N", "twos_representation")
def graph_tool_representation(twos_representation, N):
    A = convert_to_numpy(twos_representation, N)
    g = graph_tool.Graph(directed=False)
    g.add_vertex(N)
    for edge in zip(*np.where(A)):
        n0, n1 = edge
        if n0 > n1:
            g.add_edge(n0, n1)
    return g

######################### Special invariant code #################

@build_representation("numpy")
@require_arguments("A", "N")
def special_tutte_polynomial(A, N):

    cmd = os.path.join(__script_dir, 'tutte', 'tutte_bhkk')
    tutte_args = ' '.join(map(str, [N,] + A.ravel().tolist()))
    cmd += ' ' + tutte_args
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    
    sval = [[int(x) for x in line.split()] for line in proc.stdout]
    return sval
    print sval

    terms = []
    tpoly = np.zeros((N+1,N+1),dtype='int32')
    
    for xi in range(len(sval)):
        for yi in range(len(sval[xi])):
            val = sval[xi][yi]
            print xi,yi, val
    
            if val:
                tpoly[xi][yi] = sval[xi][yi]

    return tpoly.ravel()


@build_representation("networkx")
def special_cycle_basis(g, **kwargs):
    cycles = nx.cycle_basis(g)
    sorted_cycles = tuple(sorted([tuple(sorted(c)) for c in cycles]))

    terms = []
    for cycle_k in range(len(sorted_cycles)):
        for idx in sorted_cycles[cycle_k]:
            terms.append((cycle_k, idx))
    if not terms:
        return ((None, None),)
    return tuple(terms)


@require_arguments("N")
def special_independent_vertex_sets(adj, **kwargs):
    cmd_idep = "main {N} {adj}".format(adj=adj, **kwargs)
    cmd = os.path.join(__script_dir, 'independent_vertex_sets', cmd_idep)
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    # Convert to two's representation
    independent_sets = [int(line, 2) for line in proc.stdout]
    return tuple([(x,) for x in independent_sets])

@require_arguments("N")
def special_independent_edge_sets(adj, **kwargs):
    cmd_idep = "main {N} {adj}".format(adj=adj, **kwargs)
    cmd = os.path.join(__script_dir, 'independent_edge_sets', cmd_idep)
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    # Already in two's representation
    independent_sets = [int(line) for line in proc.stdout]
    return tuple([(x,) for x in independent_sets])


#invariant_requirements["chromatic_polynomial"].append("tutte_polynomial")
@require_arguments("twos_representation","N")
def special_chromatic_polynomial(twos_representation,N):
    '''
    This is the chromatic polynomial, derived from the Tutte polynomial
    The chromatic polynomial for a connected graphs evaluates T(x,y)
    at C(k) = T(x=1-k,y=0)*(-1)**N*(1-k)*N
    '''
    repack = {"twos_representation":twos_representation,"N":N}
    T = special_tutte_polynomial(repack)

    # Extract only the x component of the tutte poly
    from sympy.abc import x
    p = 0
    for power,row in enumerate(T):
        if row and row[0]:
            p += row[0] * x ** power

    C = (-1) ** (N - 1) * x * p.subs(x, 1 - x)
    C = sympy.poly(C)
    coeffs = C.all_coeffs()

    # Resize coeffs to match desired length
    coeffs = [0,]*(N+1-len(coeffs)) + coeffs
    return np.array(coeffs).astype(np.int32)


######################### REQUIRES [degree_sequence] #################

@require_arguments("degree_sequence")
def n_edge(adj, degree_sequence, **kwargs):
    # Defined this way for loopless simple graphs
    return sum(degree_sequence) / 2

@require_arguments("degree_sequence")
def n_endpoints(adj, degree_sequence, **kwargs):
    # Defined this way for loopless simple graphs
    return sum([True for d in degree_sequence if d == 1])

@require_arguments("degree_sequence")
def is_k_regular(adj, degree_sequence, **kwargs):
    # Returns the value of k if it is k regular, otherwise 0
    # Note that the singular graph is 0_regular
    # Cubic graphs are related to http://oeis.org/A002851

    if len(set(degree_sequence)) == 1:
        return degree_sequence[0]
    else:
        return 0

######################### REQUIRES [cycle_basis] #################

@require_arguments("cycle_basis")
def n_cycle_basis(adj, cycle_basis, **kwargs):
    return len(cycle_basis)

@require_arguments("cycle_basis")
def is_tree(adj, cycle_basis, **kwargs):
    # Trees have no cycles
    return int(len(cycle_basis) == 0)

@require_arguments("cycle_basis")
def girth(adj, cycle_basis, **kwargs):
    # Since the cycle basis is the minimal set of fundemental cycles
    # the girth has to be the length of the smallest of these cycles
    # Graphs with no cycles have girth=0 (defined) as placeholder for infinity
    if not cycle_basis:
        return 0

    return min(map(len, cycle_basis))

@require_arguments("N", "cycle_basis")
def circumference(adj, cycle_basis, N, **kwargs):
    # The circumference is found from the cycle_basis be the largest
    # direct combination of terms
    # Graphs with no cycles have cir=0 (defined) as placeholder for infinity

    if not cycle_basis:
        return 0

    def combine_cycle(C):
        idx = np.zeros(N, dtype=int)
        for c in C:
            idx[c] = 1
        return np.where(idx)[0].tolist()

    return len(combine_cycle(cycle_basis))

######################### REQUIRES [polynomial_tutte] #################


def eval_chromatic_from_tutte(z, N, tutte_poly):
    # First adjust the indices, and remove those where k>0 in y**k
    tutte_adjust = [(coeff, xd - 1) for xd, yd, coeff in tutte_poly if yd == 1]

    # The chromatic polynomial for a connected graphs evaluates T(x,y)
    # at C(k) = T(x=1-k,y=0)*(-1)**N*(1-k)*k

    # Testing against sympy
    '''
    from sympy.abc import x
    p = 0
    for (coeff,power) in tutte_adjust: p += coeff*x**power
    C = (-1)**(N-1)*x*p.subs(x,1-x).factor()
    print (C.factor())
    print (C.subs(x,z))
    '''

    terms = [coeff * (1 - z) ** xd for coeff, xd in tutte_adjust]
    chi = sum(terms) * ((-1) ** (N - 1)) * z

    return chi

@require_arguments("N", "tutte_polynomial")
def chromatic_number(adj, N, tutte_polynomial, **kwargs):
    # Return 0 for the singleton graph (it's really infinity)
    if N == 1:
        return 0

    for k in range(1, N + 1):
        if eval_chromatic_from_tutte(k, N, tutte_polynomial) != 0:
            return k

    msg = "Should have exited by now"
    raise ValueError(msg)

######################### Invariant code #########################

@require_arguments("N")
def n_vertex(adj, N, **kwargs):
    return N

@require_arguments("N")
@build_representation("numpy")
def is_strongly_regular(A, N, **kwargs):
    # Check with http://oeis.org/A088741
    # Returns the value of k if it is k strongly regular, otherwise 0
    # Strongly regular graphs satisfy AJ = kJ, where J is a ones matrix
    # Assume that N=1,2 is are strongly regular to match with OEIS
    if N <= 2:
        return 1

    K = A.sum(axis=0)

    if len(set(K)) != 1:
        return False

    L, V = None, None

    for v0, v1 in itertools.combinations(range(N), 2):
        common = (A[v0] * A[v1]).sum()
        if A[v0, v1]:
            if L is None:
                L = common
            if L and common != L:
                return False
        if not A[v0, v1]:
            if V is None:
                V = common
            if V and common != V:
                return False
    return True

@require_arguments("N")
@build_representation("networkx")
def diameter(g, N, **kwargs):
    if N == 1: return 0
    return nx.diameter(g)

@require_arguments("N")
@build_representation("networkx")
def radius(g, N, **kwargs):
    if N == 1: return 0
    return nx.radius(g)

@build_representation("networkx")
def k_max_clique(g, **kwargs):
    return nx.graph_clique_number(g)

@build_representation("networkx")
def is_chordal(g, **kwargs):
    return nx.is_chordal(g)

@build_representation("networkx")
def is_eulerian(g, **kwargs):
    return nx.is_eulerian(g)

@build_representation("networkx")
def is_distance_regular(g, **kwargs):
    return nx.is_distance_regular(g)

@build_representation("graph_tool")
def is_planar(g, **kwargs):
    return graph_tool.topology.is_planar(g)

@build_representation("graph_tool")
def is_bipartite(g, **kwargs):
    return graph_tool.topology.is_bipartite(g)

@build_representation("graph_tool")
def n_articulation_points(g, **kwargs):
    bicomp, art, nc = graph_tool.topology.label_biconnected_components(g)
    return sum(art.a)

@build_representation("networkx")
def vertex_connectivity(g, **kwargs):
    return nx.node_connectivity(g)

@build_representation("networkx")
def edge_connectivity(g, **kwargs):
    return nx.edge_connectivity(g)

def _poly_factorable_over_field(p, domain):
    # Factor the char poly over the integers
    pz = sympy.factor(p, domain=domain)

    # Change expression like (a+b)**n -> (a+b)
    def reduce_power(fp):
        try:
            return fp.base
        except:
            return fp

    # Loop over the factors
    for term in pz.as_ordered_factors():
        term_poly = sympy.poly(reduce_power(term))
        # Check if the base factors are not linear
        # indicates can't be factored over choosen domain
        if term_poly.degree() > 1:
            return False
    return True

@build_representation("numpy")
def is_integral(A, **kwargs):
    # Check with http://oeis.org/A064731
    # Symbolically determine if char poly factors over Z
    M = sympy.Matrix(A)
    p = M.charpoly()
    return _poly_factorable_over_field(p, "ZZ")

@build_representation("numpy")
def is_rational_spectrum(A, **kwargs):
    # Like is_integral, checks if the char. poly factors over Q instead of Z
    M = sympy.Matrix(A)
    p = M.charpoly()
    return _poly_factorable_over_field(p, "QQ")

@require_arguments("N")
@build_representation("numpy")
def is_distinct_spectrum(A, N, **kwargs):
    # Checks if all eigenvalues are unique
    M = sympy.Matrix(A)
    p = M.charpoly()
    return p.rep.count_real_roots() == N

######################### Subgraph code #########################


def __generate_KN(n):
    g = graph_tool.Graph(directed=False)
    g.add_vertex(n)
    for i, j in itertools.combinations(range(n), 2):
        g.add_edge(i, j)
    return g


def __generate_CN(n):
    g = graph_tool.Graph(directed=False)
    g.add_vertex(n)
    labels = range(n)
    for i in range(-1, n - 1):
        g.add_edge(labels[i], labels[i + 1])
    return g

_complete_graphs = [__generate_KN(n) for n in range(0, 15)]
_cycle_graphs = [__generate_CN(n) for n in range(0, 15)]
_has_subgraph = graph_tool.topology.subgraph_isomorphism


def _is_subgraph_free(subg):
    subg_n = len([x for x in subg.vertices()])

    def f(adj, **kwargs):
        # Early breakout if input graph is too small
        if kwargs["N"] < subg_n:
            return 1
        g = graph_tool_representation(adj, **kwargs)

        return len(_has_subgraph(subg, g, max_n=1))==0

    return f

# is_subgraph_free_K3=1, OEIS:A024607
is_subgraph_free_K3 = _is_subgraph_free(_complete_graphs[3])
is_subgraph_free_K4 = _is_subgraph_free(_complete_graphs[4])
is_subgraph_free_K5 = _is_subgraph_free(_complete_graphs[5])

is_subgraph_free_C4 = _is_subgraph_free(_cycle_graphs[4])
is_subgraph_free_C5 = _is_subgraph_free(_cycle_graphs[5])

# zero_func = lambda x,**args:0
is_subgraph_free_C6 = _is_subgraph_free(_cycle_graphs[6])
is_subgraph_free_C7 = _is_subgraph_free(_cycle_graphs[7])
is_subgraph_free_C8 = _is_subgraph_free(_cycle_graphs[8])
is_subgraph_free_C9 = _is_subgraph_free(_cycle_graphs[9])
is_subgraph_free_C10 = _is_subgraph_free(_cycle_graphs[10])

_bull_graph = _cycle_graphs[3].copy()
_bull_graph_v1 = _bull_graph.add_vertex()
_bull_graph_v2 = _bull_graph.add_vertex()
_bull_graph.add_edge(_bull_graph_v1, _bull_graph.vertex(0))
_bull_graph.add_edge(_bull_graph_v2, _bull_graph.vertex(1))
is_subgraph_free_bull = _is_subgraph_free(_bull_graph)

_open_bowtie_graph = _cycle_graphs[3].copy()
_open_bowtie_graph_v1 = _open_bowtie_graph.add_vertex()
_open_bowtie_graph_v2 = _open_bowtie_graph.add_vertex()
_open_bowtie_graph.add_edge(_open_bowtie_graph_v1,
                            _open_bowtie_graph.vertex(0))
_open_bowtie_graph.add_edge(_open_bowtie_graph_v2,
                            _open_bowtie_graph.vertex(0))
is_subgraph_free_open_bowtie = _is_subgraph_free(_open_bowtie_graph)

_bowtie_graph = _cycle_graphs[3].copy()
_bowtie_graph_v1 = _bowtie_graph.add_vertex()
_bowtie_graph_v2 = _bowtie_graph.add_vertex()
_bowtie_graph.add_edge(_bowtie_graph_v1, _bowtie_graph.vertex(0))
_bowtie_graph.add_edge(_bowtie_graph_v2, _bowtie_graph.vertex(0))
_bowtie_graph.add_edge(_bowtie_graph_v2, _bowtie_graph_v1)
is_subgraph_free_bowtie = _is_subgraph_free(_bowtie_graph)

_diamond_graph = _cycle_graphs[4].copy()
_diamond_graph.add_edge(_diamond_graph.vertex(0), _diamond_graph.vertex(2))
is_subgraph_free_diamond = _is_subgraph_free(_diamond_graph)

_paw_graph = _cycle_graphs[3].copy()
_paw_graph_v1 = _paw_graph.add_vertex()
_paw_graph.add_edge(_paw_graph_v1, _paw_graph.vertex(0))
is_subgraph_free_paw = _is_subgraph_free(_paw_graph)

_banner_graph = _cycle_graphs[4].copy()
_banner_graph_v1 = _banner_graph.add_vertex()
_banner_graph.add_edge(_banner_graph_v1, _banner_graph.vertex(0))
is_subgraph_free_banner = _is_subgraph_free(_banner_graph)

######################### Bliss code #########################


######################### PuLP code (Integer programming) ###

def _is_connected_edge_list(prob, N):
    # Checks if an edge_solution from PuLP is connected
    edge_solution = [e for e in prob.variables() if e.varValue]

    g_sol = graph_tool.Graph(directed=False)
    g_sol.add_vertex(N)
    for edge in edge_solution:
        _, e0, e1 = edge.name.split('_')
        e0 = int(e0[1:-1])
        e1 = int(e1[:-1])
        g_sol.add_edge(e0, e1)

    conn = graph_tool.topology.label_largest_component(g_sol)
    return conn.a.all()

@require_arguments("N")
@build_representation("numpy")
def is_hamiltonian(A, N, **kwargs):

    if N == 1:
        return True

    edges = zip(*np.where(A))
    edges = set([edge for edge in edges if edge[0] >= edge[1]])

    prob = pulp.LpProblem("hamiltonian_cycle",
                          pulp.LpMinimize)

    # For each edge, create a binary variable.
    # If it is part of the path/cycle then it will be 1
    edge_strings = [(e0, e1) for e0, e1 in edges]
    e_vars = pulp.LpVariable.dicts("edge", (edge_strings,),
                                   0, 1, pulp.LpInteger)

    # Arbitrary objective function (since we are trying to uniquely find sol)
    prob += pulp.lpSum(e_vars), "TSP objective"

    # Find unique vertices
    verts = set()
    for e0, e1 in edges:
        verts.add(e0)
        verts.add(e1)

    # For each vertex, add the constraint that is must appear exactly twice
    # e.g. each vertex in a Ham. cycle has an inbound and outbound edge

    for v in verts:
        # Find all edges that contain this vert
        edge_match = []
        for e in e_vars:
            if v in e:
                edge_match.append(e)

        prob += pulp.lpSum([e_vars[x] for x in edge_match]) == 2, ""

    # Add the constaint the exactly n edges must be selected
    prob += pulp.lpSum([e_vars[x] for x in e_vars]) == N, "total_edges"

    sol = prob.solve()

    # PuLP returns -1 if solution is infeasible
    if sol == -1 or sol == -3:
        return False

    if sol != 1:
        print ("PuLP failed with", sol, pulp.LpStatus[prob.status])
        print (prob.writeLP("debug_save.lp"))

    # If there is cycle, make sure it is connected
    while not _is_connected_edge_list(prob, N):

        # A disjoint solution was found, add it to the list of constaints
        edge_solution = [e for e in prob.variables() if e.varValue]
        prob += pulp.lpSum(edge_solution) <= N - 1, ""
        sol = prob.solve()

        # No solution possible
        if sol == -1 or sol == -3:
            return False

    if sol != 1:
        print ("PuLP failed with", sol, pulp.LpStatus[prob.status])
        print (prob.writeLP("debug_save.lp"))

    return True

########## Independent set iterator/Fractional programs #################

@require_arguments("fractional_chromatic_number")
def has_fractional_duality_gap_vertex_chromatic(adj, 
                                                fractional_chromatic_number,
                                                **kwargs):
    chi  = chromatic_number(adj, **kwargs)
    a, b = fractional_chromatic_number
    chi_f = fractions.Fraction(a, b)
    return chi != chi_f


@require_arguments("independent_vertex_sets")
def n_independent_vertex_sets(adj, independent_vertex_sets, **kwargs):
    return len(independent_vertex_sets)

@require_arguments("independent_vertex_sets")
def maximal_independent_vertex_set(adj, independent_vertex_sets, **kwargs):
    active = [bin(x[0]).count('1') for x in independent_vertex_sets]
    return max(active)

@require_arguments("independent_edge_sets")
def n_independent_edge_sets(adj, independent_edge_sets, **kwargs):
    return len(independent_edge_sets)

@require_arguments("independent_edge_sets")
def maximal_independent_edge_set(adj, independent_edge_sets, **kwargs):
    active = [bin(x[0]).count('1') for x in independent_edge_sets]
    return max(active)

######################### Test code #########################

def convert_nx_to_adj(g):
    edges = g.edges()
    N = len(g.nodes())
    idx = zip(*edges)

    # Since graph in undirected assign both sides
    A = np.zeros((N, N), dtype=int)
    A[idx[0], idx[1]] = 1

    __upper_matrix_index = np.triu_indices(N)
    # The string representation of the upper triangular adj matrix
    au = ''.join(map(str, A[__upper_matrix_index]))

    # Convert the binary string to an int
    int_index = int(au, 2)

    return int_index

if __name__ == "__main__":
    import logging

    # Start the logger
    logging.root.setLevel(logging.INFO)
    logging.info("Testing the Petersen graph for all the invariants")

    logging.info("Creating the graph.")
    g = nx.petersen_graph()

    logging.info("Converting to adj. format")
    adj = convert_nx_to_adj(g)

    N = 10
    args = {"N": N}

    logging.info("Converting to numpy format")
    A = convert_to_numpy(adj, **args)

    logging.info("Converting to networkx format")
    gx = networkx_representation(adj, **args)

    logging.info("Converting to graph-tool format")
    gt = graph_tool_representation(adj, **args)

    logging.info("Computing the Tutte polynomial")
    p = special_polynomial_tutte(adj, **args)
    args["tutte_polynomial"] = p
    print (p)

    logging.info("Computing the chromatic polynomial")
    p = special_chromatic_polynomial(adj, **args)
    args["chromatic_polynomial"] = p
    print (p)

    logging.info("Computing the degree sequence")
    p = special_degree_sequence(adj, **args)
    args["degree_sequence"] = np.array(p).ravel()

    logging.info("Computing the fractional chromatic number")
    p = fractional_chromatic_number(adj, **args)
    args["fractional_chromatic_number"] = p[0]
    print (p)

    logging.info("Computing the characteristic polynomial")
    p = special_characteristic_polynomial(adj, **args)
    args["characteristic_polynomial"] = p
    print (p)

    logging.info("Computing the laplacian polynomial")
    p = special_laplacian_polynomial(adj, **args)
    args["laplacian_polynomial"] = p
    print (p)

    logging.info("Computing the independent vertex sets")
    p = special_independent_vertex_sets(adj, **args)
    args["independent_vertex_sets"] = p
    print (p)

    logging.info("Computing the independent edge sets")
    p = special_independent_edge_sets(adj, **args)
    args["independent_edge_sets"] = p
    print (p)

    logging.info("Computing the cycle basis")
    import collections
    p = special_cycle_basis(adj, **args)
    cb = collections.defaultdict(list)
    for cycle_k, idx in p:
        cb[cycle_k].append(idx)
    args["cycle_basis"] = cb.values()

    from helper_functions import load_options
    options = load_options()

    for func in options["invariant_function_names"]:
        logging.info("Computing {}".format(func))
        x = eval(func)(adj, **args)
        print (x)

    viz_graph(gt)
