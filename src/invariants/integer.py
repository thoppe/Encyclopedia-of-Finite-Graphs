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


if __name__ == "__main__":
    B = automorphism_group_n()
    item = {"twos_representation":474, "N":4}
    print B(item)
    print B.shape(**item)
