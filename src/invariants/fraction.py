import subprocess
import os
import fractions
import numpy as np

from base_invariant import graph_invariant

_script_dir = os.path.dirname(os.path.realpath(__file__))

class fraction_invariant(graph_invariant):
    def shape(self, **kwargs):
        return 2

class fractional_chromatic_number(fraction_invariant):

    import_requirements = ["pulp"]

    # No conversion needed
    output_type = None

    def calculate(self, twos_representation, N, **kwargs):
        pulp = self.imports["pulp"]
        
        # As a check, the cycle graph should return 2.5 = 5/2

        
        cmd_idep = os.path.join(_script_dir,
                                "independent_vertex_sets",
                                "main {N} {twos_rep}")
        
        cmd = cmd_idep.format(N=N, twos_rep=twos_representation)
        
        proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
        independent_sets = [line.strip() for line in proc.stdout]

        prob = pulp.LpProblem("fractional_chrom",
                              pulp.LpMinimize)

        K = len(independent_sets)

        iset_vars = pulp.LpVariable.dicts("iset", range(K),
                                          lowBound=0)

        prob += pulp.lpSum(iset_vars), "Objective"

        for idx in range(N):
            isets_with_vertex = [iset_vars[k] for k in range(K)
                                 if independent_sets[k][idx] == "1"]
            prob += pulp.lpSum(isets_with_vertex) >= 1

        status = prob.solve()

        if status == 1:
            sol = [x.value() for x in prob.variables()]
            f_sol = map(fractions.Fraction, sol)
            sol = sum([x.limit_denominator(20 * N * K) for x in f_sol])
            a, b = sol.numerator, sol.denominator
            val = np.array([a,b],dtype=np.int32)
            return val
        else:
            err_msg = "ERROR IN FRACTIONAL CHROMATIC! rep: {}"
            raise ValueError(err_msg.format(twos_representation))

if __name__ == "__main__":
    B = fractional_chromatic_number()
    item = {"twos_representation":474, "N":4}
    print B(item)
    print B.shape(**item)
