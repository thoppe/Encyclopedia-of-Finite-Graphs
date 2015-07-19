import numpy as np
import networkx as nx

import os
import subprocess

from base_invariant import graph_invariant

_script_dir = os.path.dirname(os.path.realpath(__file__))

class integer_invariant(graph_invariant):
    def shape(self, **kwargs): return 1


####################################################################

class chromatic_number(integer_invariant):
    ''' Evaluates the chromatic number from the chromatic polynomial. '''
    invariant_requirements = ["chromatic_polynomial"]

    # No conversion needed
    output_type = None

    def calculate(self, N, chromatic_polynomial, **kwargs):
        if N==1: return 0
    
        cpoly = np.poly1d(chromatic_polynomial)
        
        for k in range(1, N + 1):
            if cpoly(k) != 0:
                return k

        msg = "Chromatic polynomial calculation failed"
        raise ValueError(msg)
        

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
        assert((A==A.T).all())
        return np.triu(A).sum()

class n_endpoints(integer_invariant):
    # This is only valid for undirected graphs
       
    def calculate(self, A, **kwargs):
        assert((A==A.T).all())
        return (A.sum(axis=0)==2).sum()

class k_regular(integer_invariant):
    # Returns the value of k if it is k regular, otherwise 0
    # Note that the singular graph is 0_regular
    # Cubic graphs are related to http://oeis.org/A002851
    
    invariant_requirements = ["degree_sequence"]
       
    def calculate(self, A, degree_sequence, **kwargs):                
        if len(set(degree_sequence)) == 1:
            return degree_sequence[0]
        else:
            return 0


class diameter(integer_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, N, **kwargs):
        if N == 1:
            return 0
        return nx.diameter(gx)


class radius(integer_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, N, **kwargs):
        if N == 1:
            return 0
        return nx.radius(gx)

class k_max_clique(integer_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        return nx.graph_clique_number(gx)

class vertex_connectivity(integer_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        return nx.node_connectivity(gx)

class edge_connectivity(integer_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        return nx.edge_connectivity(gx)


class n_cycle_basis(integer_invariant):
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        return len(nx.cycle_basis(gx))

class girth(integer_invariant):
    '''
    Since the cycle basis is the minimal set of fundemental cycles
    the girth has to be the length of the smallest of these cycles.
    Graphs with no cycles have girth=0 (defined) as placeholder for infinity.
    '''
    output_type = "networkx"
    
    def calculate(self, gx, **kwargs):
        CB = nx.cycle_basis(gx)
        if not CB: return 0
        return min(map(len, CB))
    

class circumference(integer_invariant):
    '''
    The circumference is found from the cycle_basis be the largest
    direct combination of terms. Graphs with no cycles have
    cir=0 (defined) as placeholder for infinity.
    '''
    output_type = "networkx"
    
    
    def calculate(self, gx, N, **kwargs):

        CB = nx.cycle_basis(gx)
        if not CB: return 0

        def combine_cycle(C):
            idx = np.zeros(N, dtype=int)
            for c in C:
                idx[c] = 1
            return np.where(idx)[0].tolist()

        return len(combine_cycle(CB))



class n_articulation_points(integer_invariant):
    output_type = "graph_tool"
    import_requirements = ["graph_tool.topology"]
    
    def calculate(self, gtx, **kwargs):
        gtop = self.imports["graph_tool.topology"]
        bicomp, art, nc = gtop.label_biconnected_components(gtx)
        return sum(art.a)    



if __name__ == "__main__":
    B = automorphism_group_n()
    item = {"twos_representation":474, "N":4}
    print B(item)
    print B.shape(**item)
