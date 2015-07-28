import numpy as np
import polynomial
from base_invariant import graph_invariant

class polynomial_zero_finder(graph_invariant):

    dtype = np.float64
    import_requirements = ["mpmath"]

    def __init__(self):
        super(polynomial_zero_finder,self).__init__()
        self.poly_func = self.base_poly_invariant()

    def shape(self,**kwargs):
        # Use the same shape as the input polynomial
        return self.poly_func.shape(**kwargs)

    def validiate_roots(self,roots):
        # Check if roots are real, etc...
        return True

    def convert_roots(self,roots):
        # Return roots in a python readable list
        return map(self.dtype, roots)

    def calculate(self,**kwargs):        
        # Find the polynomial in the kwargs
        poly_key = self.required_invariants[0]
        poly_n = self.shape(**kwargs)

        # Alias for mpmath
        mpmath = self.imports["mpmath"]
        mpmath.dps = 200
        
        p = kwargs[poly_key]
        print p

        # If needed, try to convert numpy array into a standard python list
        try:
            p = map(float,p.tolist())
        except:
            pass

        roots = mpmath.polyroots(p,maxsteps=2000,extraprec=2000)

        # Check roots
        assert(self.validiate_roots(roots))

        # Return nicely formated roots
        return self.convert_roots(roots)


class real_polynomial_zero_finder(polynomial_zero_finder):
    
    def validiate_roots(self,roots):
        for x in roots:
            if x.imag !=0:
                return False
        return True

############################################################################

class chromatic_polynomial_zeros(real_polynomial_zero_finder):
    base_poly_invariant = polynomial.chromatic_polynomial
    required_invariants = ["chromatic_polynomial"]

class laplacian_polynomial_zeros(real_polynomial_zero_finder):
    base_poly_invariant = polynomial.laplacian_polynomial
    required_invariants = ["laplacian_polynomial"]

class characteristic_polynomial_zeros(real_polynomial_zero_finder):
    base_poly_invariant = polynomial.characteristic_polynomial
    required_invariants = ["characteristic_polynomial"]


############################################################################


if __name__ == "__main__":
    item = {"twos_representation":474, "N":4}

    item["chromatic_polynomial"] = polynomial.chromatic_polynomial()(item)
    func = chromatic_polynomial_zeros()
    print func(item)

    item["laplacian_polynomial"] = polynomial.laplacian_polynomial()(item)    
    func = laplacian_polynomial_zeros()
    print func(item)

    item["characteristic_polynomial"] = polynomial.characteristic_polynomial()(item)
    func = characteristic_polynomial_zeros()
    print func(item)


    
