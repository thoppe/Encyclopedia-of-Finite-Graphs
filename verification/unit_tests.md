## Unit tests for N={3, ..., 8}

*passed*  : `is_integral=1`
OEIS      : [`[1, 2, 3, 6, 7, 22]`](http://oeis.org/A064731)
received  :  `[1, 2, 3, 6, 7, 22]`


*passed*  : `n_vertex>0`
OEIS      : [`[2, 6, 21, 112, 853, 11117]`](https://oeis.org/A001349)
received  :  `[2, 6, 21, 112, 853, 11117]`


*passed*  : `n_edge=10`
OEIS      : [`[0, 0, 1, 14, 132, 486]`](https://oeis.org/A054923)
received  :  `[0, 0, 1, 14, 132, 486]`


*passed*  : `automorphism_group_n=1`
OEIS      : [`[0, 0, 0, 8, 144, 3552]`](http://oeis.org/A124059)
received  :  `[0, 0, 0, 8, 144, 3552]`


*passed*  : `edge_connectivity>0`
OEIS      : [`[2, 6, 21, 112, 853, 11117]`](https://oeis.org/A001349)
received  :  `[2, 6, 21, 112, 853, 11117]`


*passed*  : `edge_connectivity>1`
OEIS      : [`[1, 3, 11, 60, 502, 7403]`](http://oeis.org/A007146)
received  :  `[1, 3, 11, 60, 502, 7403]`


*passed*  : `vertex_connectivity>=0`
OEIS      : [`[2, 6, 21, 112, 853, 11117]`](https://oeis.org/A001349)
received  :  `[2, 6, 21, 112, 853, 11117]`


*passed*  : `vertex_connectivity>1`
OEIS      : [`[1, 3, 10, 56, 468, 7123]`](http://oeis.org/A002218)
received  :  `[1, 3, 10, 56, 468, 7123]`


*passed*  : `vertex_connectivity>2`
OEIS      : [`[0, 1, 3, 17, 136, 2388]`](http://oeis.org/A006290)
received  :  `[0, 1, 3, 17, 136, 2388]`


*passed*  : `vertex_connectivity>3`
OEIS      : [`[0, 0, 1, 4, 25, 384]`](http://oeis.org/A086216)
received  :  `[0, 0, 1, 4, 25, 384]`


*passed*  : `vertex_connectivity>4`
OEIS      : [`[0, 0, 0, 1, 4, 39]`](http://oeis.org/A086217)
received  :  `[0, 0, 0, 1, 4, 39]`


*passed*  : `is_subgraph_free_C4=1`
OEIS      : [`[2, 3, 8, 19, 57, 186]`](http://oeis.org/A077269)
received  :  `[2, 3, 8, 19, 57, 186]`


*passed*  : `is_subgraph_free_K3=1`
OEIS      : [`[1, 3, 6, 19, 59, 267]`](http://oeis.org/A024607)
received  :  `[1, 3, 6, 19, 59, 267]`


*passed*  : `is_subgraph_free_K4=1`
OEIS      : [`[2, 5, 17, 82, 536, 5606]`](http://oeis.org/A079574)
received  :  `[2, 5, 17, 82, 536, 5606]`


*passed*  : `is_bipartite=1`
OEIS      : [`[1, 3, 5, 17, 44, 182]`](http://oeis.org/A005142)
received  :  `[1, 3, 5, 17, 44, 182]`


*passed*  : `is_planar=1`
OEIS      : [`[2, 6, 20, 99, 646, 5974]`](http://oeis.org/A003094)
received  :  `[2, 6, 20, 99, 646, 5974]`


*passed*  : `n_cycle_basis=1`
OEIS      : [`[1, 2, 5, 13, 33, 89]`](http://oeis.org/A001429)
received  :  `[1, 2, 5, 13, 33, 89]`


*passed*  : `n_cycle_basis=0`
OEIS      : [`[1, 2, 3, 6, 11, 23]`](http://oeis.org/A000055)
received  :  `[1, 2, 3, 6, 11, 23]`


*passed*  : `n_articulation_points=0`
OEIS      : [`[1, 3, 10, 56, 468, 7123]`](http://oeis.org/A002218)
received  :  `[1, 3, 10, 56, 468, 7123]`


*passed*  : `is_planar=1`
OEIS      : [`[2, 6, 20, 99, 646, 5974]`](https://oeis.org/A003094)
received  :  `[2, 6, 20, 99, 646, 5974]`


*passed*  : `is_chordal=1`
OEIS      : [`[2, 5, 15, 58, 272, 1614]`](http://oeis.org/A048192)
received  :  `[2, 5, 15, 58, 272, 1614]`


*passed*  : `n_endpoints=0`
OEIS      : [`[1, 3, 11, 61, 507, 7442]`](https://oeis.org/A004108)
received  :  `[1, 3, 11, 61, 507, 7442]`


*passed*  : `chromatic_number=2`
OEIS      : [`[1, 3, 5, 17, 44, 182]`](http://oeis.org/A005142)
received  :  `[1, 3, 5, 17, 44, 182]`


*passed*  : `chromatic_number=3`
OEIS      : [`[1, 2, 12, 64, 475, 5036]`](http://oeis.org/A126737)
received  :  `[1, 2, 12, 64, 475, 5036]`


*passed*  : `chromatic_number=4`
OEIS      : [`[0, 1, 3, 26, 282, 5009]`](http://oeis.org/A126738)
received  :  `[0, 1, 3, 26, 282, 5009]`


*passed*  : `chromatic_number=5`
OEIS      : [`[0, 0, 1, 4, 46, 809]`](http://oeis.org/A126739)
received  :  `[0, 0, 1, 4, 46, 809]`


*passed*  : `chromatic_number=6`
OEIS      : [`[0, 0, 0, 1, 5, 74]`](http://oeis.org/A126740)
received  :  `[0, 0, 0, 1, 5, 74]`


*passed*  : `is_strongly_regular=1`
OEIS      : [`[1, 2, 2, 3, 1, 3]`](http://oeis.org/A088741)
received  :  `[1, 2, 2, 3, 1, 3]`


*passed*  : `is_tree=1`
OEIS      : [`[1, 2, 3, 6, 11, 23]`](http://oeis.org/A000055)
received  :  `[1, 2, 3, 6, 11, 23]`


*passed*  : `is_eulerian=1`
OEIS      : [`[1, 1, 4, 8, 37, 184]`](http://oeis.org/A003049)
received  :  `[1, 1, 4, 8, 37, 184]`


*passed*  : `is_k_regular=3`
OEIS      : [`[0, 1, 0, 2, 0, 5]`](http://oeis.org/A002851)
received  :  `[0, 1, 0, 2, 0, 5]`


*passed*  : `is_k_regular=4`
OEIS      : [`[0, 0, 1, 1, 2, 6]`](http://oeis.org/A006820)
received  :  `[0, 0, 1, 1, 2, 6]`


