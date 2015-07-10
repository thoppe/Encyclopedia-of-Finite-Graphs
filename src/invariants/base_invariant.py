import os
from functools import wraps

from type_convert import type_conversion_funcs

import networkx as nx
import numpy as np

#import sympy
#import pulp
#_imported_list = []
#_script_dir = os.path.dirname(os.path.realpath(__file__))

class graph_invariant(object):
    import_requirements = []
    input_type  = 'twos'
    output_type = 'numpy'
    dtype = np.int32

    def __init__(self): pass

    def shape(self, N, **kwargs):
        return 1

    def convert_types(self, args):
        key = (self.input_type, self.output_type)
        func,name = type_conversion_funcs[key]
        args[name] = func(**args)

    def calculate(self,A,N,**kwargs):
        return None

    def __call__(self, args):
        self.convert_types(args)
        return self.calculate(**args)


if __name__ == "__main__":
    # Example invariant
    
    class edges(graph_invariant):
        def calculate(self,A,N,**kwargs):
            return A.sum()/2

    B = edges()
    item = {"twos_representation":474, "N":4}
    print B(item)

