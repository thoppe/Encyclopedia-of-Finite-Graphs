## Unit tests for N={3, ..., 7}

*passed*  : `is_integral=1`
OEIS      : [`[1, 2, 3, 6, 7]`](http://oeis.org/A064731)
received  :  `[1, 2, 3, 6, 7]`


**FAILED**  : `n_vertex>0`
OEIS        : [`[2, 6, 21, 112, 853]`](https://oeis.org/A001349)
received    :  `[0, 6, 0, 0, 0]`


**FAILED**  : `n_edge=10`
OEIS        : [`[0, 0, 1, 14, 132]`](https://oeis.org/A054923)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `automorphism_group_n=1`
OEIS        : [`[0, 0, 0, 8, 144]`](http://oeis.org/A124059)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `edge_connectivity>0`
OEIS        : [`[2, 6, 21, 112, 853]`](https://oeis.org/A001349)
received    :  `[0, 6, 0, 0, 0]`


**FAILED**  : `edge_connectivity>1`
OEIS        : [`[1, 3, 11, 60, 502]`](http://oeis.org/A007146)
received    :  `[0, 3, 0, 0, 0]`


**FAILED**  : `vertex_connectivity>=0`
OEIS        : [`[2, 6, 21, 112, 853]`](https://oeis.org/A001349)
received    :  `[0, 6, 0, 0, 0]`


**FAILED**  : `vertex_connectivity>1`
OEIS        : [`[1, 3, 10, 56, 468]`](http://oeis.org/A002218)
received    :  `[0, 3, 0, 0, 0]`


**FAILED**  : `vertex_connectivity>2`
OEIS        : [`[0, 1, 3, 17, 136]`](http://oeis.org/A006290)
received    :  `[0, 1, 0, 0, 0]`


**FAILED**  : `vertex_connectivity>3`
OEIS        : [`[0, 0, 1, 4, 25]`](http://oeis.org/A086216)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `vertex_connectivity>4`
OEIS        : [`[0, 0, 0, 1, 4]`](http://oeis.org/A086217)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `is_subgraph_free_C4=1`
OEIS        : [`[2, 3, 8, 19, 57]`](http://oeis.org/A077269)
received    :  `[0, 3, 0, 0, 0]`


**FAILED**  : `is_subgraph_free_K3=1`
OEIS        : [`[1, 3, 6, 19, 59]`](http://oeis.org/A024607)
received    :  `[0, 3, 0, 0, 0]`


**FAILED**  : `is_subgraph_free_K4=1`
OEIS        : [`[2, 5, 17, 82, 536]`](http://oeis.org/A079574)
received    :  `[0, 5, 0, 0, 0]`


**FAILED**  : `is_bipartite=1`
OEIS        : [`[1, 3, 5, 17, 44]`](http://oeis.org/A005142)
received    :  `[0, 3, 0, 0, 0]`


**FAILED**  : `is_planar=1`
OEIS        : [`[2, 6, 20, 99, 646]`](http://oeis.org/A003094)
received    :  `[0, 6, 0, 0, 0]`


**FAILED**  : `n_cycle_basis=1`
OEIS        : [`[1, 2, 5, 13, 33]`](http://oeis.org/A001429)
received    :  `[0, 2, 0, 0, 0]`


**FAILED**  : `n_cycle_basis=0`
OEIS        : [`[1, 2, 3, 6, 11]`](http://oeis.org/A000055)
received    :  `[0, 2, 0, 0, 0]`


**FAILED**  : `n_articulation_points=0`
OEIS        : [`[1, 3, 10, 56, 468]`](http://oeis.org/A002218)
received    :  `[0, 3, 0, 0, 0]`


**FAILED**  : `is_planar=1`
OEIS        : [`[2, 6, 20, 99, 646]`](https://oeis.org/A003094)
received    :  `[0, 6, 0, 0, 0]`


**FAILED**  : `is_chordal=1`
OEIS        : [`[2, 5, 15, 58, 272]`](http://oeis.org/A048192)
received    :  `[0, 5, 0, 0, 0]`


**FAILED**  : `n_endpoints=0`
OEIS        : [`[1, 3, 11, 61, 507]`](https://oeis.org/A004108)
received    :  `[0, 3, 0, 0, 0]`


**FAILED**  : `chromatic_number=2`
OEIS        : [`[1, 3, 5, 17, 44]`](http://oeis.org/A005142)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `chromatic_number=3`
OEIS        : [`[1, 2, 12, 64, 475]`](http://oeis.org/A126737)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `chromatic_number=4`
OEIS        : [`[0, 1, 3, 26, 282]`](http://oeis.org/A126738)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `chromatic_number=5`
OEIS        : [`[0, 0, 1, 4, 46]`](http://oeis.org/A126739)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `chromatic_number=6`
OEIS        : [`[0, 0, 0, 1, 5]`](http://oeis.org/A126740)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `is_strongly_regular=1`
OEIS        : [`[1, 2, 2, 3, 1]`](http://oeis.org/A088741)
received    :  `[0, 2, 0, 0, 0]`


**FAILED**  : `is_tree=1`
OEIS        : [`[1, 2, 3, 6, 11]`](http://oeis.org/A000055)
received    :  `[0, 2, 0, 0, 0]`


**FAILED**  : `is_eulerian=1`
OEIS        : [`[1, 1, 4, 8, 37]`](http://oeis.org/A003049)
received    :  `[0, 1, 0, 0, 0]`


**FAILED**  : `is_k_regular=3`
OEIS        : [`[0, 1, 0, 2, 0]`](http://oeis.org/A002851)
received    :  `[0, 1, 0, 0, 0]`


**FAILED**  : `is_k_regular=4`
OEIS        : [`[0, 0, 1, 1, 2]`](http://oeis.org/A006820)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `is_k_regular=5`
OEIS        : [`[0, 0, 0, 1, 0]`](http://oeis.org/A006820)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `is_k_regular=6`
OEIS        : [`[0, 0, 0, 0, 1]`](http://oeis.org/A006822)
received    :  `[0, 0, 0, 0, 0]`


*passed*  : `is_k_regular=7`
OEIS      : [`[0, 0, 0, 0, 0]`](http://oeis.org/A014377)
received  :  `[0, 0, 0, 0, 0]`


*passed*  : `is_k_regular=8`
OEIS      : [`[0, 0, 0, 0, 0]`](http://oeis.org/A014378)
received  :  `[0, 0, 0, 0, 0]`


**FAILED**  : `k_max_clique=2`
OEIS        : [`[1, 3, 6, 19, 59]`](http://oeis.org/A024607)
received    :  `[0, 3, 0, 0, 0]`


**FAILED**  : `k_max_clique=3`
OEIS        : [`[1, 2, 11, 63, 477]`](http://oeis.org/A126745)
received    :  `[0, 2, 0, 0, 0]`


**FAILED**  : `k_max_clique=4`
OEIS        : [`[0, 1, 3, 25, 266]`](http://oeis.org/A126746)
received    :  `[0, 1, 0, 0, 0]`


**FAILED**  : `k_max_clique=5`
OEIS        : [`[0, 0, 1, 4, 45]`](http://oeis.org/A126747)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `k_max_clique=6`
OEIS        : [`[0, 0, 0, 1, 5]`](http://oeis.org/A126748)
received    :  `[0, 0, 0, 0, 0]`


**FAILED**  : `k_max_clique=7`
OEIS        : [`[0, 0, 0, 0, 1]`](http://oeis.org/A217987)
received    :  `[0, 0, 0, 0, 0]`


