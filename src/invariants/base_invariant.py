import os
import logging

from functools import wraps

from type_convert import type_conversion_funcs

import networkx as nx
import numpy as np

#import sympy
#_imported_list = []
#_script_dir = os.path.dirname(os.path.realpath(__file__))

class graph_invariant(object):
    '''
    Generic invariant. All import_requirements will be load on the first
    instantiation in the dictionary self.imports. The default input type
    and output type (for automatic conversion) and dtype can be overridden.

    If another invariant is required from these libraries, place it in
    invariant_requirements.
    '''
    
    _has_imported = False
    import_requirements = []
    imports = {}

    invariant_requirements = []
    invariants = {}
    
    input_type  = 'twos'
    output_type = 'numpy'
    dtype = np.int32

    def __init__(self):
        if not self._has_imported:
            for key in self.import_requirements:
                logging.info("Importing {}".format(key))
                line = "import {}".format(key)
                exec line
                self.imports[key] = eval(key)

            self._has_imported = True
        pass

    def shape(self, **kwargs):
        return 1

    def convert_types(self, args):
        key = (self.input_type, self.output_type)

        if self.output_type is not None:
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

