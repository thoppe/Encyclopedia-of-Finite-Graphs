## Unit tests for N={3, ..., 9}

**FAILED**  : `is_integral=1`
OEIS        : [`[1, 2, 3, 6, 7, 22, 24]`](http://oeis.org/A064731)
received    : `[1, 2, 3, 6, 7, 22, 25]`


*passed*  : `n_vertex>0`
OEIS      : [`[2, 6, 21, 112, 853, 11117, 261080]`](https://oeis.org/A001349)
received  :  `[2, 6, 21, 112, 853, 11117, 261080]`


*passed*  : `n_edge=10`
OEIS      : [`[0, 0, 1, 14, 132, 486, 797]`](https://oeis.org/A054923)
received  :  `[0, 0, 1, 14, 132, 486, 797]`


*passed*  : `automorphism_group_n=1`
OEIS      : [`[0, 0, 0, 8, 144, 3552, 131452]`](http://oeis.org/A124059)
received  :  `[0, 0, 0, 8, 144, 3552, 131452]`


*passed*  : `vertex_connectivity>=0`
OEIS      : [`[2, 6, 21, 112, 853, 11117, 261080]`](https://oeis.org/A001349)
received  :  `[2, 6, 21, 112, 853, 11117, 261080]`


*passed*  : `vertex_connectivity>1`
OEIS      : [`[1, 3, 10, 56, 468, 7123, 194066]`](http://oeis.org/A002218)
received  :  `[1, 3, 10, 56, 468, 7123, 194066]`


*passed*  : `vertex_connectivity>2`
OEIS      : [`[0, 1, 3, 17, 136, 2388, 80890]`](http://oeis.org/A006290)
received  :  `[0, 1, 3, 17, 136, 2388, 80890]`


*passed*  : `vertex_connectivity>3`
OEIS      : [`[0, 0, 1, 4, 25, 384, 14480]`](http://oeis.org/A086216)
received  :  `[0, 0, 1, 4, 25, 384, 14480]`


*passed*  : `vertex_connectivity>4`
OEIS      : [`[0, 0, 0, 1, 4, 39, 1051]`](http://oeis.org/A086217)
received  :  `[0, 0, 0, 1, 4, 39, 1051]`


*passed*  : `is_subgraph_free_C4=1`
OEIS      : [`[2, 3, 8, 19, 57, 186, 740]`](http://oeis.org/A077269)
received  :  `[2, 3, 8, 19, 57, 186, 740]`


*passed*  : `is_subgraph_free_K3=1`
OEIS      : [`[1, 3, 6, 19, 59, 267, 1380]`](http://oeis.org/A024607)
received  :  `[1, 3, 6, 19, 59, 267, 1380]`


*passed*  : `is_subgraph_free_K4=1`
OEIS      : [`[2, 5, 17, 82, 536, 5606, 95915]`](http://oeis.org/A079574)
received  :  `[2, 5, 17, 82, 536, 5606, 95915]`


*passed*  : `is_bipartite=1`
OEIS      : [`[1, 3, 5, 17, 44, 182, 730]`](http://oeis.org/A005142)
received  :  `[1, 3, 5, 17, 44, 182, 730]`


*passed*  : `is_planar=1`
OEIS      : [`[2, 6, 20, 99, 646, 5974, 71885]`](http://oeis.org/A003094)
received  :  `[2, 6, 20, 99, 646, 5974, 71885]`


*passed*  : `n_cycle_basis=1`
OEIS      : [`[1, 2, 5, 13, 33, 89, 240]`](http://oeis.org/A001429)
received  :  `[1, 2, 5, 13, 33, 89, 240]`


*passed*  : `n_cycle_basis=0`
OEIS      : [`[1, 2, 3, 6, 11, 23, 47]`](http://oeis.org/A000055)
received  :  `[1, 2, 3, 6, 11, 23, 47]`


*passed*  : `n_articulation_points=0`
OEIS      : [`[1, 3, 10, 56, 468, 7123, 194066]`](http://oeis.org/A002218)
received  :  `[1, 3, 10, 56, 468, 7123, 194066]`


*passed*  : `is_planar=1`
OEIS      : [`[2, 6, 20, 99, 646, 5974, 71885]`](https://oeis.org/A003094)
received  :  `[2, 6, 20, 99, 646, 5974, 71885]`


*passed*  : `n_endpoints=0`
OEIS      : [`[1, 3, 11, 61, 507, 7442, 197772]`](https://oeis.org/A004108)
received  :  `[1, 3, 11, 61, 507, 7442, 197772]`


*passed*  : `chromatic_number=2`
OEIS      : [`[1, 3, 5, 17, 44, 182, 730]`](http://oeis.org/A005142)
received  :  `[1, 3, 5, 17, 44, 182, 730]`


*passed*  : `chromatic_number=3`
OEIS      : [`[1, 2, 12, 64, 475, 5036, 80947]`](http://oeis.org/A126737)
received  :  `[1, 2, 12, 64, 475, 5036, 80947]`


*passed*  : `chromatic_number=4`
OEIS      : [`[0, 1, 3, 26, 282, 5009, 149551]`](http://oeis.org/A126738)
received  :  `[0, 1, 3, 26, 282, 5009, 149551]`


*passed*  : `chromatic_number=5`
OEIS      : [`[0, 0, 1, 4, 46, 809, 27794]`](http://oeis.org/A126739)
received  :  `[0, 0, 1, 4, 46, 809, 27794]`


*passed*  : `chromatic_number=6`
OEIS      : [`[0, 0, 0, 1, 5, 74, 1940]`](http://oeis.org/A126740)
received  :  `[0, 0, 0, 1, 5, 74, 1940]`


*passed*  : `is_strongly_regular=1`
OEIS      : [`[1, 2, 2, 3, 1, 3, 3]`](http://oeis.org/A088741)
received  :  `[1, 2, 2, 3, 1, 3, 3]`


*passed*  : `is_tree=1`
OEIS      : [`[1, 2, 3, 6, 11, 23, 47]`](http://oeis.org/A000055)
received  :  `[1, 2, 3, 6, 11, 23, 47]`


*passed*  : `is_eulerian=1`
OEIS      : [`[1, 1, 4, 8, 37, 184, 1782]`](http://oeis.org/A003049)
received  :  `[1, 1, 4, 8, 37, 184, 1782]`


*passed*  : `is_k_regular=3`
OEIS      : [`[0, 1, 0, 2, 0, 5, 0]`](http://oeis.org/A002851)
received  :  `[0, 1, 0, 2, 0, 5, 0]`


*passed*  : `is_k_regular=4`
OEIS      : [`[0, 0, 1, 1, 2, 6, 16]`](http://oeis.org/A006820)
received  :  `[0, 0, 1, 1, 2, 6, 16]`


*passed*  : `is_k_regular=5`
OEIS      : [`[0, 0, 0, 1, 0, 3, 0]`](http://oeis.org/A006820)
received  :  `[0, 0, 0, 1, 0, 3, 0]`


*passed*  : `is_k_regular=6`
OEIS      : [`[0, 0, 0, 0, 1, 1, 4]`](http://oeis.org/A006822)
received  :  `[0, 0, 0, 0, 1, 1, 4]`


*passed*  : `is_k_regular=7`
OEIS      : [`[0, 0, 0, 0, 0, 1, 0]`](http://oeis.org/A014377)
received  :  `[0, 0, 0, 0, 0, 1, 0]`


*passed*  : `is_k_regular=8`
OEIS      : [`[0, 0, 0, 0, 0, 0, 1]`](http://oeis.org/A014378)
received  :  `[0, 0, 0, 0, 0, 0, 1]`


