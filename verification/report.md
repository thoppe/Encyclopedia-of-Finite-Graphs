## Unit tests for N={3, ..., 10}

*passed*  : `is_integral=1`
OEIS      : [`[1, 2, 3, 6, 7, 22, 24, 83]`](http://oeis.org/A064731)
received  :  `[1, 2, 3, 6, 7, 22, 24, 83]`


*passed*  : `n_vertex>0`
OEIS      : [`[2, 6, 21, 112, 853, 11117, 261080, 11716571]`](https://oeis.org/A001349)
received  :  `[2, 6, 21, 112, 853, 11117, 261080, 11716571]`


*passed*  : `n_edge=10`
OEIS      : [`[0, 0, 1, 14, 132, 486, 797, 657]`](https://oeis.org/A054923)
received  :  `[0, 0, 1, 14, 132, 486, 797, 657]`


*passed*  : `automorphism_group_n=1`
OEIS      : [`[0, 0, 0, 8, 144, 3552, 131452, 7840396]`](http://oeis.org/A124059)
received  :  `[0, 0, 0, 8, 144, 3552, 131452, 7840396]`


*passed*  : `edge_connectivity>0`
OEIS      : [`[2, 6, 21, 112, 853, 11117, 261080, 11716571]`](https://oeis.org/A001349)
received  :  `[2, 6, 21, 112, 853, 11117, 261080, 11716571]`


*passed*  : `edge_connectivity>1`
OEIS      : [`[1, 3, 11, 60, 502, 7403, 197442, 9804368]`](http://oeis.org/A007146)
received  :  `[1, 3, 11, 60, 502, 7403, 197442, 9804368]`


*passed*  : `vertex_connectivity>=0`
OEIS      : [`[2, 6, 21, 112, 853, 11117, 261080, 11716571]`](https://oeis.org/A001349)
received  :  `[2, 6, 21, 112, 853, 11117, 261080, 11716571]`


*passed*  : `vertex_connectivity>1`
OEIS      : [`[1, 3, 10, 56, 468, 7123, 194066, 9743542]`](http://oeis.org/A002218)
received  :  `[1, 3, 10, 56, 468, 7123, 194066, 9743542]`


*passed*  : `vertex_connectivity>2`
OEIS      : [`[0, 1, 3, 17, 136, 2388, 80890, 5114079]`](http://oeis.org/A006290)
received  :  `[0, 1, 3, 17, 136, 2388, 80890, 5114079]`


**FAILED**  : `vertex_connectivity>3`
OEIS        : [`[0, 0, 1, 4, 25, 384, 14480]`](http://oeis.org/A086216)
received    :  `[0, 0, 1, 4, 25, 384, 14480, 1211735]`


**FAILED**  : `vertex_connectivity>4`
OEIS        : [`[0, 0, 0, 1, 4, 39, 1051]`](http://oeis.org/A086217)
received    :  `[0, 0, 0, 1, 4, 39, 1051, 102630]`


*passed*  : `is_subgraph_free_C4=1`
OEIS      : [`[2, 3, 8, 19, 57, 186, 740, 3389]`](http://oeis.org/A077269)
received  :  `[2, 3, 8, 19, 57, 186, 740, 3389]`


*passed*  : `is_subgraph_free_K3=1`
OEIS      : [`[1, 3, 6, 19, 59, 267, 1380, 9832]`](http://oeis.org/A024607)
received  :  `[1, 3, 6, 19, 59, 267, 1380, 9832]`


**FAILED**  : `is_subgraph_free_K4=1`
OEIS        : [`[2, 5, 17, 82, 536, 5606, 95915]`](http://oeis.org/A079574)
received    :  `[2, 5, 17, 82, 536, 5606, 95915, 2784072]`


*passed*  : `is_bipartite=1`
OEIS      : [`[1, 3, 5, 17, 44, 182, 730, 4032]`](http://oeis.org/A005142)
received  :  `[1, 3, 5, 17, 44, 182, 730, 4032]`


*passed*  : `is_planar=1`
OEIS      : [`[2, 6, 20, 99, 646, 5974, 71885, 1052805]`](http://oeis.org/A003094)
received  :  `[2, 6, 20, 99, 646, 5974, 71885, 1052805]`


*passed*  : `n_cycle_basis=1`
OEIS      : [`[1, 2, 5, 13, 33, 89, 240, 657]`](http://oeis.org/A001429)
received  :  `[1, 2, 5, 13, 33, 89, 240, 657]`


*passed*  : `n_cycle_basis=0`
OEIS      : [`[1, 2, 3, 6, 11, 23, 47, 106]`](http://oeis.org/A000055)
received  :  `[1, 2, 3, 6, 11, 23, 47, 106]`


*passed*  : `n_articulation_points=0`
OEIS      : [`[1, 3, 10, 56, 468, 7123, 194066, 9743542]`](http://oeis.org/A002218)
received  :  `[1, 3, 10, 56, 468, 7123, 194066, 9743542]`


*passed*  : `is_planar=1`
OEIS      : [`[2, 6, 20, 99, 646, 5974, 71885, 1052805]`](https://oeis.org/A003094)
received  :  `[2, 6, 20, 99, 646, 5974, 71885, 1052805]`


*passed*  : `is_chordal=1`
OEIS      : [`[2, 5, 15, 58, 272, 1614, 11911, 109539]`](http://oeis.org/A048192)
received  :  `[2, 5, 15, 58, 272, 1614, 11911, 109539]`


*passed*  : `n_endpoints=0`
OEIS      : [`[1, 3, 11, 61, 507, 7442, 197772, 9808209]`](https://oeis.org/A004108)
received  :  `[1, 3, 11, 61, 507, 7442, 197772, 9808209]`


*passed*  : `chromatic_number=2`
OEIS      : [`[1, 3, 5, 17, 44, 182, 730, 4032]`](http://oeis.org/A005142)
received  :  `[1, 3, 5, 17, 44, 182, 730, 4032]`


*passed*  : `chromatic_number=3`
OEIS      : [`[1, 2, 12, 64, 475, 5036, 80947, 2010328]`](http://oeis.org/A126737)
received  :  `[1, 2, 12, 64, 475, 5036, 80947, 2010328]`


*passed*  : `chromatic_number=4`
OEIS      : [`[0, 1, 3, 26, 282, 5009, 149551, 7694428]`](http://oeis.org/A126738)
received  :  `[0, 1, 3, 26, 282, 5009, 149551, 7694428]`


*passed*  : `chromatic_number=5`
OEIS      : [`[0, 0, 1, 4, 46, 809, 27794, 1890221]`](http://oeis.org/A126739)
received  :  `[0, 0, 1, 4, 46, 809, 27794, 1890221]`


*passed*  : `chromatic_number=6`
OEIS      : [`[0, 0, 0, 1, 5, 74, 1940, 113272]`](http://oeis.org/A126740)
received  :  `[0, 0, 0, 1, 5, 74, 1940, 113272]`


**FAILED**  : `is_strongly_regular=1`
OEIS        : [`[1, 2, 2, 3, 1, 3, 3]`](http://oeis.org/A088741)
received    :  `[1, 2, 2, 3, 1, 3, 3, 5]`


*passed*  : `is_tree=1`
OEIS      : [`[1, 2, 3, 6, 11, 23, 47, 106]`](http://oeis.org/A000055)
received  :  `[1, 2, 3, 6, 11, 23, 47, 106]`


*passed*  : `is_eulerian=1`
OEIS      : [`[1, 1, 4, 8, 37, 184, 1782, 31026]`](http://oeis.org/A003049)
received  :  `[1, 1, 4, 8, 37, 184, 1782, 31026]`


*passed*  : `is_k_regular=3`
OEIS      : [`[0, 1, 0, 2, 0, 5, 0, 19]`](http://oeis.org/A002851)
received  :  `[0, 1, 0, 2, 0, 5, 0, 19]`


*passed*  : `is_k_regular=4`
OEIS      : [`[0, 0, 1, 1, 2, 6, 16, 59]`](http://oeis.org/A006820)
received  :  `[0, 0, 1, 1, 2, 6, 16, 59]`


*passed*  : `is_k_regular=5`
OEIS      : [`[0, 0, 0, 1, 0, 3, 0, 60]`](http://oeis.org/A006820)
received  :  `[0, 0, 0, 1, 0, 3, 0, 60]`


*passed*  : `is_k_regular=6`
OEIS      : [`[0, 0, 0, 0, 1, 1, 4, 21]`](http://oeis.org/A006822)
received  :  `[0, 0, 0, 0, 1, 1, 4, 21]`


*passed*  : `is_k_regular=7`
OEIS      : [`[0, 0, 0, 0, 0, 1, 0, 5]`](http://oeis.org/A014377)
received  :  `[0, 0, 0, 0, 0, 1, 0, 5]`


*passed*  : `is_k_regular=8`
OEIS      : [`[0, 0, 0, 0, 0, 0, 1, 1]`](http://oeis.org/A014378)
received  :  `[0, 0, 0, 0, 0, 0, 1, 1]`


*passed*  : `k_max_clique=2`
OEIS      : [`[1, 3, 6, 19, 59, 267, 1380, 9832]`](http://oeis.org/A024607)
received  :  `[1, 3, 6, 19, 59, 267, 1380, 9832]`


*passed*  : `k_max_clique=3`
OEIS      : [`[1, 2, 11, 63, 477, 5339, 94535, 2774240]`](http://oeis.org/A126745)
received  :  `[1, 2, 11, 63, 477, 5339, 94535, 2774240]`


*passed*  : `k_max_clique=4`
OEIS      : [`[0, 1, 3, 25, 266, 4646, 136935, 7121703]`](http://oeis.org/A126746)
received  :  `[0, 1, 3, 25, 266, 4646, 136935, 7121703]`


*passed*  : `k_max_clique=5`
OEIS      : [`[0, 0, 1, 4, 45, 785, 26205, 1696407]`](http://oeis.org/A126747)
received  :  `[0, 0, 1, 4, 45, 785, 26205, 1696407]`


*passed*  : `k_max_clique=6`
OEIS      : [`[0, 0, 0, 1, 5, 73, 1908, 110140]`](http://oeis.org/A126748)
received  :  `[0, 0, 0, 1, 5, 73, 1908, 110140]`


*passed*  : `k_max_clique=7`
OEIS      : [`[0, 0, 0, 0, 1, 6, 109, 4085]`](http://oeis.org/A217987)
received  :  `[0, 0, 0, 0, 1, 6, 109, 4085]`


