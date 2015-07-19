import os
import subprocess

import numpy as np
import networkx as nx

__script_dir = os.path.dirname(os.path.realpath(__file__))

# Helper functions, and invariants that do not follow
# a fixed size (e.g. independent edge sets, tutte poly...).
# These will not be saved.

def tutte_polynomial(A, N):

    cmd = os.path.join(__script_dir, 'tutte', 'tutte_bhkk')
    tutte_args = ' '.join(map(str, [N,] + A.ravel().tolist()))
    cmd += ' ' + tutte_args
    proc = subprocess.Popen([cmd], stdout=subprocess.PIPE, shell=True)
    
    sval = [[int(x) for x in line.split()] for line in proc.stdout]
    return sval
