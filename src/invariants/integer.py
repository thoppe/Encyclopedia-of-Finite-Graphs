import numpy as np
import os
import subprocess

from base_invariant import graph_invariant

_script_dir = os.path.dirname(os.path.realpath(__file__))

class integer_invariant(graph_invariant):
    def shape(self, **kwargs): return 1

class automorphism_group_n(integer_invariant):
    ''' Calls the BLISS program from the command line '''

    def calculate(self, A, N, **kwargs):
        
        edges = np.where(A)
        s = ["p edge {} {}".format(N, A.sum() / 2, **kwargs)]
        for i, j in zip(*edges):
            if i <= j:
                s.append("e {} {}".format(i + 1, j + 1))
        s_echo = '"%s"' % ('\n'.join(s))
        bliss_exec = os.path.join(_script_dir,
                                  'bliss', 'bliss')

        cmd = "echo %s | %s" % (s_echo, bliss_exec)
        
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
        for line in proc.stdout:
            if "|Aut|" in line:
                return int(line.split()[-1])

        err = "BLISS failed with adj: " + A
        raise ValueError(err)

class n_edge(integer_invariant):
    # This is only valid for undirected graphs
       
    def calculate(self, A, **kwargs):
        return np.triu(A).sum()

class n_endpoints(integer_invariant):
    # This is only valid for undirected graphs
       
    def calculate(self, A, **kwargs):
        return (A.sum(axis=0)==2).sum()

class k_regular(integer_invariant):
    # Returns the value of k if it is k regular, otherwise 0
    # Note that the singular graph is 0_regular
    # Cubic graphs are related to http://oeis.org/A002851
    
    invariant_requirements = ["polynomial degree_sequence"]
       
    def calculate(self, A, **kwargs):
        seq = self.invariants["degree_sequence"](A)
        
        if len(set(seq)) == 1:
            return seq[0]
        else:
            return 0

'''

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

'''


if __name__ == "__main__":
    B = automorphism_group_n()
    item = {"twos_representation":474, "N":4}
    print B(item)
    print B.shape(**item)
