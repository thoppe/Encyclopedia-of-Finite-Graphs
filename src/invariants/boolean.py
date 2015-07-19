import numpy as np
import networkx as nx
import graph_tool as gt

import itertools
import os

from base_invariant import graph_invariant

_script_dir = os.path.dirname(os.path.realpath(__file__))

class boolean_invariant(graph_invariant):
    dtype = np.bool
    def shape(self, **kwargs): return 1

######################################################################

class has_fractional_chromatic_gap(boolean_invariant):
    '''
    Returns True if the fraction chromatic number differs
    from the tradtional chromatic number.
    '''
    invariant_requirements = ["chromatic_number",
                              "fractional_chromatic_number"]
        
    import_requirements = ["fractions"]        
    # No conversion needed
    output_type = None

    def calculate(self, chromatic_number,
                  fractional_chromatic_number, **kwargs):

        chi = chromatic_number[0]
        chi_f = fractional_chromatic_number
        chi_f = self.imports["fractions"].Fraction(*chi_f)

        return chi != chi_f
    

######################################################################

class is_strongly_regular(boolean_invariant):

    def calculate(self, A, N, **kwargs):
        # Check with http://oeis.org/A088741
        # Returns the value of k if it is k strongly regular, otherwise 0
        # Strongly regular graphs satisfy AJ = kJ, where J is a ones matrix
        # Assume that N=1,2 is are strongly regular to match with OEIS
        if N <= 2:
            return True

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

######################################################################

def _poly_factorable_over_field(p, domain, sympy):
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


class is_integral(boolean_invariant):
    import_requirements = ["sympy"]

    def calculate(self, A, **kwargs):
        # Check with http://oeis.org/A064731
        # Symbolically determine if char poly factors over Z
        sympy = self.imports["sympy"]
        M = sympy.Matrix(A)
        p = M.charpoly()
        return _poly_factorable_over_field(p, "ZZ", sympy)


class is_rational(boolean_invariant):
    import_requirements = ["sympy"]
    # Like is_integral, checks if the char. poly factors over Q instead of Z

    def calculate(self, A, **kwargs):
        sympy = self.imports["sympy"]
        M = sympy.Matrix(A)
        p = M.charpoly()
        return _poly_factorable_over_field(p, "QQ", sympy)

class is_distinct_spectrum(boolean_invariant):
    import_requirements = ["sympy"]
    # Checks if all eigenvalues are unique
    
    def calculate(self, A, N, **kwargs):
        sympy = self.imports["sympy"]

        M = sympy.Matrix(A)
        p = M.charpoly()
        return p.rep.count_real_roots() == N
    
######################################################################

class is_chordal(boolean_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        return nx.is_chordal(gx)

class is_eulerian(boolean_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        return nx.is_eulerian(gx)

class is_distance_regular(boolean_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        return nx.is_distance_regular(gx)

class is_tree(boolean_invariant):
    # Trees have no cycles
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        return len(nx.cycle_basis(gx)) == 0

class is_planar(boolean_invariant):
    output_type = "graph_tool"
    import_requirements = ["graph_tool.topology"]
    
    def calculate(self, gtx, **kwargs):
        gtop = self.imports["graph_tool.topology"]
        return gtop.is_planar(gtx)

class is_bipartite(boolean_invariant):
    output_type = "graph_tool"
    import_requirements = ["graph_tool.topology"]
    
    def calculate(self, gtx, **kwargs):
        gtop = self.imports["graph_tool.topology"]
        return gtop.is_bipartite(gtx)

    
####################################################################

def _is_connected_edge_list(prob, N, gtop):
    # Checks if an edge_solution from PuLP is connected
    edge_solution = [e for e in prob.variables() if e.varValue]

    g_sol = gt.Graph(directed=False)
    g_sol.add_vertex(N)
    for edge in edge_solution:
        _, e0, e1 = edge.name.split('_')
        e0 = int(e0[1:-1])
        e1 = int(e1[:-1])
        g_sol.add_edge(e0, e1)

    conn = gtop.label_largest_component(g_sol)
    return conn.a.all()


    
class is_hamiltonian(boolean_invariant):
    #output_type = "graph_tool"
    import_requirements = ["pulp", "graph_tool.topology"]

    def calculate(self, A, N, **kwargs):
        
        if N == 1:
            return True

        pulp = self.imports["pulp"]
        gtop = self.imports["graph_tool.topology"]

        edges = zip(*np.where(A))
        edges = set([edge for edge in edges if edge[0] >= edge[1]])

        prob = pulp.LpProblem("hamiltonian_cycle",
                            pulp.LpMinimize)


        # For each edge, create a binary variable.
        # If it is part of the path/cycle then it will be 1
        edge_strings = [(e0, e1) for e0, e1 in edges]
        e_vars = pulp.LpVariable.dicts("edge", (edge_strings,),
                                    0, 1, pulp.LpInteger)

        # Arbitrary objective function
        # (since we are trying to uniquely find sol)
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
        while not _is_connected_edge_list(prob, N, gtop):

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
