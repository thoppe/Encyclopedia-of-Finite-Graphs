from base_invariant import graph_invariant

class degree_sequence(graph_invariant):
    def shape(self, N, **kwargs): return N

    def calculate(self, A, **kwargs):
        deg = sorted(A.sum(axis=0))
        return deg

if __name__ == "__main__":

    B = degree_sequence()
    item = {"twos_representation":474, "N":4}
    print B(item)
    print B.shape(**item)
