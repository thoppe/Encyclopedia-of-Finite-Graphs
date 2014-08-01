# -*- coding: utf-8 -*-
"""
Flow based connectivity and cutsets
"""
# http://www.informatik.uni-augsburg.de/thi/personen/kammer/Graph_Connectivity.pdf
# http://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf

import itertools
import networkx as nx
__author__ = '\n'.join(['Jordi Torrents <jtorrents@milnou.net>'])
__all__ = [ 'vertex_connectivity',
            'global_vertex_connectivity',
            'edge_connectivity',
            'global_edge_connectivity',
            'all_pairs_vertex_connectivity_matrix',
            'dominating_set',
            'minimum_st_vertex_cutset',
            'minimum_vertex_cutset',
            'minimum_st_edge_cutset',
            'minimum_edge_cutset',
            ]

def _aux_digraph_vertex_connectivity(G):
    r""" Creates a directed graph D from an undirected graph G to compute flow
    based vertex connectivity.
    For an undirected graph G having `n` nodes and `m` edges we derive a
    directed graph D with 2n nodes and 2m+n arcs by replacing each
    original node `v` with two nodes `vA`,`vB` linked by an (internal)
    arc in D. Then for each edge (u,v) in G we add two arcs (uB,vA)
    and (vB,uA) in D. Finally we set the attribute capacity = 1 for each
    arc in D [1].
    For a directed graph having `n` nodes and `m` arcs we derive a
    directed graph D with 2n nodes and m+n arcs by replacing each
    original node `v` with two nodes `vA`,`vB` linked by an (internal)
    arc `(vA,vB)` in D. Then for each arc (u,v) in G we add one arc (uB,vA)
    in D. Finally we set the attribute capacity = 1 for each arc in D.
    References
    ----------
    .. [1] Kammer, Frank and Hanjo Taubig. Graph Connectivity. in Brandes and
        Erlebach, 'Network Analysis: Methodological Foundations', Lecture
        Notes in Computer Science, Volume 3418, Springer-Verlag, 2005.
        http://www.informatik.uni-augsburg.de/thi/personen/kammer/Graph_Connectivity.pdf
 
    """
    directed = G.is_directed()
    mapping = {}
    D = nx.DiGraph()
    for i,node in enumerate(G):
        mapping[node] = i
        D.add_node('%dA'%i,id=node)
        D.add_node('%dB'%i,id=node)
        D.add_edge('%dA'%i,'%dB'%i, capacity=1)
   
    edges = []
    for (source, target) in G.edges():
        edges.append(('%sB'%mapping[source], '%sA'%mapping[target]))
        if not directed:
            edges.append(('%sB'%mapping[target], '%sA'%mapping[source]))
   
    D.add_edges_from(edges, capacity=1)
    return D, mapping
def vertex_connectivity(G, s, t, aux_digraph=None, mapping=None):
    r"""Computes local vertex connectivity for nodes s and t.
    Local vetrex connectivity for two non adjacent nodes s and t is the
    minimum number of nodes that must be removed (along with their incident
    edges) to disconnect them in G (ie to destroy any path from s to t).
    This is a flow based implementation of vertex connectivity. We compute the
    maximum flow on an auxiliary digraph build from the original input
    graph (see below for details). This is equal to the local vertex
    connectivity because the value of a maximum s-t-flow is equal to the
    capacity of a minimum s-t-cut (Ford and Fulkerson theorem) [1].
    What do we do with adjacent nodes? [1] suggests K = n-1 but I prefer having
    a parameter to
   
    Parameters
    ----------
    G : NetworkX graph
        Undirected graph
    s : node
        Source node
    t : node
        Target node
    aux_digraph : NetworkX DiGraph (default=None)
        Auxiliary digraph to compute flow based vertex connectivity. If None
        the auxiliary digraph is build.
    mapping : dict (default=None)
        Dictionary with a mapping of node names in G and in the auxiliary digraph.
    Returns
    -------
    K : integer
        local vertex connectivity for nodes s and t
    Examples
    --------
    >>> # Platonic icosahedral graph has vertex connectivity 5
    ... # for each non adjacent node pair
    >>> G = nx.icosahedral_graph()
    >>> print(nx.info(G))
    >>> nx.vertex_connectivity(G,0,6)
    5
    Notes
    -----
    This is a flow based implementation of vertex connectivity. We compute the
    maximum flow using the Ford and Fulkerson algorithm on an auxiliary digraph
    build from the original input graph:
    For an undirected graph G having `n` nodes and `m` edges we derive a
    directed graph D with 2n nodes and 2m+n arcs by replacing each
    original node `v` with two nodes `vA`,`vB` linked by an (internal)
    arc in D. Then for each edge (u,v) in G we add two arcs (uB,vA)
    and (vB,uA) in D. Finally we set the attribute capacity = 1 for each
    arc in D [1].
    For a directed graph G having `n` nodes and `m` arcs we derive a
    directed graph D with 2n nodes and m+n arcs by replacing each
    original node `v` with two nodes `vA`,`vB` linked by an (internal)
    arc `(vA,vB)` in D. Then for each arc (u,v) in G we add one arc (uB,vA)
    in D. Finally we set the attribute capacity = 1 for each arc in D.
    This is equal to the local vertex connectivity because the value of
    a maximum s-t-flow is equal to the capacity of a minimum s-t-cut (Ford
    and Fulkerson theorem) [1].
    See also
    --------
    global_vertex_connectivity
    all_pairs_vertex_connectivity_matrix
    edge_connectivity
    global_edge_connectivity
    maximum_flow
    ford_fulkerson
    References
    ----------
    .. [1] Kammer, Frank and Hanjo Taubig. Graph Connectivity. in Brandes and
        Erlebach, 'Network Analysis: Methodological Foundations', Lecture
        Notes in Computer Science, Volume 3418, Springer-Verlag, 2005.
        http://www.informatik.uni-augsburg.de/thi/personen/kammer/Graph_Connectivity.pdf
   
    """ 
    if aux_digraph is None or mapping is None:
        H, mapping = _aux_digraph_vertex_connectivity(G)
    else:
        H = aux_digraph
    return nx.maximum_flow(H,'%sB'%mapping[s],'%sA'%mapping[t])
def global_vertex_connectivity(G):
    r"""Returns vertex connectivity for a graph or digraph G.
    Global vertex connectivity is the minimum number of nodes that
    must be removed to disconnect G or render it trivial. This is a flow
    based implementation. The algorithm is based in solving a number of
    max-flow problems (ie local st-vertex connectivity, see
    `vertex_connectivity`) to determine the the capacity of the minimum
    cut on an auxiliary directed network that corresponds to the minimum
    vertex cut of G. It handles both directed and undirected graphs.
   
    Parameters
    ----------
    G : NetworkX graph
        Undirected graph
    Returns
    -------
    K : integer
        global vertex connectivity for G
    Examples
    --------
    >>> # Platonic icosahedral graph is 5-vertex-connected
    >>> G = nx.icosahedral_graph()
    >>> print(nx.info(G))
    >>> nx.global_vertex_connectivity(G)
    5
   
    Notes
    -----
    This is a flow based implementation of global vertex connectivity. The
    algorithm works by solving `O((n-\delta-1+\delta(\delta-1)/2)` max-flow
    problems on an auxiliary digraph. Where `\delta` is the minimum degree
    of G. For details about the auxiliary digraph and the computation of
    local vertex connectivity see `vertex_connectivity`.
    This implementation is based on algorithm 11 in [1]. We use the Ford
    and Fulkerson algorithm to compute max flow (see `ford_fulkerson`).
   
    See also
    --------
    vertex_connectivity
    all_pairs_vertex_connectivity_matrix
    edge_connectivity
    global_edge_connectivity
    maximum_flow
    ford_fulkerson
    References
    ----------
    .. [1] Abdol-Hossein Esfahanian. Connectivity Algorithms. (this is a
        chapter, look for the reference of the book).
        http://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf
    """
    if G.is_directed():
        if not nx.is_weakly_connected(G):
            return 0
        # I think that it is necessary to consider both predecessors
        # and successors for directed graphs
        def neighbors(v):
            return itertools.chain.from_iterable([G.predecessors_iter(v),
                                                  G.successors_iter(v)])
    else:
        if not nx.is_connected(G):
            return 0
        neighbors=G.neighbors_iter
    K = G.order()-1
    # Choose a node with minimum degree
    deg = G.degree()
    min_deg = min(deg.values())
    v = (n for n,d in deg.items() if d==min_deg).next()
    # Reuse the auxiliary digraph
    H, mapping = _aux_digraph_vertex_connectivity(G)
    # compute local vertex connectivity with all non-neighbors nodes
    # and store the minimum
    for w in set(G)-set(neighbors(v))-set([v]):
        K = min(K, vertex_connectivity(G, v, w, aux_digraph=H, mapping=mapping))
    # Same for non adjacent pairs of neighbors of v
    if G.is_directed():
        for x,y in itertools.permutations(neighbors(v),2):
            if y not in G[x]:
                K = min(K, vertex_connectivity(G, x, y,
                                                aux_digraph=H, 
                                                mapping=mapping))
    else:
        for x,y in itertools.combinations(neighbors(v),2):
            if y not in G[x]:
                K = min(K, vertex_connectivity(G, x, y,
                                                aux_digraph=H, 
                                                mapping=mapping))
    return K
def all_pairs_vertex_connectivity_matrix(G):
    """Return a numpy 2d ndarray with vertex connectivity between all pairs
    of nodes.
    Parameters
    ----------
    G : NetworkX graph
        Undirected graph
    Returns
    -------
    K : 2d numpy ndarray
         vertex connectivity between all pairs of nodes.
    See also
    --------
    vertex_connectivity
    global_vertex_connectivity
    edge_connectivity
    global_edge_connectivity
    maximum_flow
    ford_fulkerson
    """
    try:
        import numpy
    except ImportError:
        raise ImportError(\
            "all_pairs_vertex_connectivity_matrix() requires NumPy")
    n = G.order()
    M = numpy.zeros((n, n), dtype=int)
    # Create auxiliary Digraph
    D, mapping = _aux_digraph_vertex_connectivity(G)
    if G.is_directed():
        for u, v in itertools.permutations(G, 2):
            K = vertex_connectivity(G, u, v, aux_digraph=D, mapping=mapping)
            M[mapping[u],mapping[v]] = K
    else:
        for u, v in itertools.combinations(G, 2):
            K = vertex_connectivity(G, u, v, aux_digraph=D, mapping=mapping)
            M[mapping[u],mapping[v]] = M[mapping[v],mapping[u]] = K
    return M
def _aux_digraph_edge_connectivity(G):
    """Auxiliary digraph for computing flow based edge connectivity
   
    If the input graph is undirected, we replace each edge (u,v) with
    two reciprocal arcs (u,v) and (v,u) and then we set the attribute
    'capacity' for each arc to 1. If the input graph is directed we simply
    add the 'capacity' attribute. Part of algorithm 1 in [1].
   
    References
    ----------
    .. [1] Abdol-Hossein Esfahanian. Connectivity Algorithms. (this is a
        chapter, look for the reference of the book).
        http://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf
    """
    if G.is_directed():
        D = G.copy()
        capacity = dict((e,1) for e in D.edges())
        nx.set_edge_attributes(D, 'capacity', capacity)
        return D
    else:
        D = G.to_directed()
        capacity = dict((e,1) for e in D.edges())
        nx.set_edge_attributes(D, 'capacity', capacity)
        return D
def edge_connectivity(G, u, v, aux_digraph=None):
    r"""Returns local edge connectivity for nodes s and t in G.
    Local edge connectivity for two nodes s and t is the minimum number
    of edges that must be removed to disconnect them in G (ie to destroy
    any path from s to t).
   
    This is a flow based implementation of edge connectivity. We compute the
    maximum flow on an auxiliary digraph build from the original
    network (see below for details). This is equal to the local edge
    connectivity because the value of a maximum s-t-flow is equal to the
    capacity of a minimum s-t-cut (Ford and Fulkerson theorem) [1].
    Parameters
    ----------
    G : NetworkX graph
        Undirected or directed graph
    s : node
        Source node
    t : node
        Target node
    aux_digraph : NetworkX DiGraph (default=None)
        Auxiliary digraph to compute flow based edge connectivity. If None
        the auxiliary digraph is build.
    Returns
    -------
    K : integer
        local edge connectivity for nodes s and t
    Examples
    --------
    >>> # Platonic icosahedral graph has edge connectivity 5
    ... # for each non adjacent node pair
    >>> G = nx.icosahedral_graph()
    >>> print(nx.info(G))
    >>> nx.edge_connectivity(G,0,6)
    5
    Notes
    -----
    This is a flow based implementation of edge connectivity. We compute the
    maximum flow using the Ford and Fulkerson algorithm on an auxiliary digraph
    build from the original graph:
    If the input graph is undirected, we replace each edge (u,v) with
    two reciprocal arcs (u,v) and (v,u) and then we set the attribute
    'capacity' for each arc to 1. If the input graph is directed we simply
    add the 'capacity' attribute. This is an implementation of algorithm 1
    in [1].
   
    The maximum flow in the auxiliary network is equal to the local edge
    connectivity because the value of a maximum s-t-flow is equal to the
    capacity of a minimum s-t-cut (Ford and Fulkerson theorem) [1].
    See also
    --------
    vertex_connectivity
    global_vertex_connectivity
    global_edge_connectivity
    maximum_flow
    ford_fulkerson
    References
    ----------
    .. [1] Abdol-Hossein Esfahanian. Connectivity Algorithms. (this is a
        chapter, look for the reference of the book).
        http://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf
 
    """
    if aux_digraph is None: 
        H = _aux_digraph_edge_connectivity(G)
    else:
        H = aux_digraph
    return nx.maximum_flow(H, u, v)
def global_edge_connectivity(G):
    r"""Returns the edge connectivity of the graph or digraph G.
    Global edge connectivity is the minimum number of edges that
    must be removed to disconnect G or render it trivial. This is a flow
    based implementation. The algorithm is based in solving a number
    of max-flow problems (ie local st-edge connectivity, see
    `edge_connectivity`) to determine the the capacity of the minimum
    cut on an auxiliary directed network that corresponds to the minimum
    edge cut of G. It handles both directed and undirected graphs.
 
    Parameters
    ----------
    G : NetworkX graph
        Undirected or directed graph
    Returns
    -------
    K : integer
        global edge connectivity for G
    Examples
    --------
    >>> # Platonic icosahedral graph is 5-edge-connected
    >>> G = nx.icosahedral_graph()
    >>> print(nx.info(G))
    >>> nx.global_edge_connectivity(G)
    5
    Notes
    -----
    This is a flow based implementation of global edge connectivity. For
    undirected graphs the algorithm works by finding a 'small' dominating
    set of nodes of G (see algorithm 7 in [1]) and computing local max flow
    (see `edge_connectivity`) between an arbitrary node in the dominating
    set and the rest of nodes in it. This is an implementation of
    algorithm 6 in [1].
    For directed graphs, the algorithm does n calls to the max flow function.
    This is an implementation of algorithm 8 in [1]. We use the Ford and
    Fulkerson algorithm to compute max flow (see `ford_fulkerson`).
   
    See also
    --------
    vertex_connectivity
    global_vertex_connectivity
    edge_connectivity
    maximum_flow
    ford_fulkerson
    References
    ----------
    .. [1] Abdol-Hossein Esfahanian. Connectivity Algorithms. (this is a
        chapter, look for the reference of the book).
        http://www.cse.msu.edu/~cse835/Papers/Graph_connectivity_revised.pdf
    """
    if G.is_directed():
        # Algorithm 8 in [1]
        if not nx.is_weakly_connected(G):
            return 0
        # initial value for lambda is min degree (\delta(G))
        L = min(G.degree().values())
        # reuse auxiliary digraph
        H = _aux_digraph_edge_connectivity(G)
        nodes = G.nodes()
        n = len(nodes)
        for i in range(n):
            if i == n-1:
                L = min(L, edge_connectivity(G, nodes[i], 
                                                nodes[0], 
                                                aux_digraph=H))
            else:
                L = min(L, edge_connectivity(G, nodes[i], 
                                                nodes[i+1], 
                                                aux_digraph=H)) 
        return L
    else: # undirected
        # Algorithm 6 in [1]
        if not nx.is_connected(G):
            return 0
        # initial value for lambda is min degree (\delta(G))
        L = min(G.degree().values())
       
        # reuse auxiliary digraph
        H = _aux_digraph_edge_connectivity(G)
        # A dominating set is \lambda-covering
        # We need a dominating set with at least two nodes
        for node in G:
            D = dominating_set(G, start_with=node)
            v = D.pop()
            if D:
                break
        else: 
            #raise nx.NetworkXError('No suitable dominating set found')
            # in complete graphs the dominating sets will always be of one node
            # thus we return min degree
            return L
        for w in D:
            L = min(L, edge_connectivity(G, v, w, aux_digraph=H))
        return L
def dominating_set(G, start_with=None):
    # Algorithm 7 in [1]
    all_nodes = set(G)
    if start_with is None:
        v = set(G).pop() # pick a node
    else:
        if start_with not in G:
            raise nx.NetworkXError('node %s not in G'%start_with)
        v = start_with
    D = set([v])
    ND = set([nbr for nbr in G[v]])
    other = all_nodes - ND - D
    while other:
        w = other.pop()
        D.add(w)
        ND.update([nbr for nbr in G[w] if nbr not in D])
        other = all_nodes - ND - D
    return D
def is_dominating_set(G, nbunch):
    # Proposed by Dan on the mailing list
    allnodes=set(G)
    testset=set(n for n in nbunch if n in G)
    nbrs=set()
    for n in testset:
        nbrs.update(G[n])
    if nbrs - allnodes:  # some nodes left--not dominating
        return False
    else:
        return True
## Cutset algorithms: it is necessary to patch maxflow.py
def minimum_st_vertex_cutset(G, s, t, aux_digraph=None, mapping=None):
    if aux_digraph is None or mapping is None:
        H, mapping = _aux_digraph_vertex_connectivity(G)
    else:
        H = aux_digraph
    rmap = dict((v,k) for k,v in mapping.items())
    edge_cut = nx.cut_set(H, '%sB'%mapping[s], '%sA'%mapping[t])
    nodes = set()
    for edge in edge_cut:
        nodes.update(edge)
    nodes = set((int(n[:-1]) for n in nodes))
    vertex_cut = set((rmap[node] for node in nodes)) - set([s,t])
    return vertex_cut
def minimum_vertex_cutset(G):
    # Analog to the algoritm for global vertex connectivity
    if G.is_directed():
        if not nx.is_weakly_connected(G):
            raise nx.NetworkXError('Input graph is not connected')
        def neighbors(v):
            return itertools.chain.from_iterable([G.predecessors_iter(v),
                                                  G.successors_iter(v)])
    else:
        if not nx.is_connected(G):
            raise nx.NetworkXError('Input graph is not connected')
        neighbors=G.neighbors_iter
    # Choose a node with minimum degree
    deg = G.degree()
    min_deg = min(deg.values())
    v = (n for n,d in deg.items() if d==min_deg).next()
    # Initial vertex cutset is all neighbors of the node with minimum degree
    min_cut = set(G[v])
    # Reuse the auxiliary digraph
    H, mapping = _aux_digraph_vertex_connectivity(G)
    # compute st vertex cuts between v and all its non-neighbors nodes in G
    # and store the minimum
    for w in set(G)-set(neighbors(v))-set([v]):
        this_cut = minimum_st_vertex_cutset(G,v,w,aux_digraph=H,mapping=mapping)
        if len(min_cut) > len(this_cut):
            min_cut = this_cut
    # Same for non adjacent pairs of neighbors of v
    if G.is_directed():
        for x,y in itertools.permutations(neighbors(v),2):
            if y not in G[x]:
                this_cut = minimum_st_vertex_cutset(G, x, y, 
                                                    aux_digraph=H, 
                                                    mapping=mapping)
                if len(min_cut) > len(this_cut):
                    min_cut = this_cut
    else:
        for x,y in itertools.combinations(neighbors(v),2):
            if y not in G[x]:
                this_cut = minimum_st_vertex_cutset(G, x, y, 
                                                    aux_digraph=H, 
                                                    mapping=mapping)
                if len(min_cut) > len(this_cut):
                    min_cut = this_cut
    return min_cut
def minimum_st_edge_cutset(G, s, t, aux_digraph=None):
    if aux_digraph is None:
        H = _aux_digraph_edge_connectivity(G)
    else:
        H = aux_digraph
    return nx.cut_set(H, s, t)
def minimum_edge_cutset(G):
    # Analog to the algoritm for global edge connectivity
    if G.is_directed():
        # Based on algorithm 8 in [1]
        if not nx.is_weakly_connected(G):
            raise nx.NetworkXError('Input graph is not connected')
        # Initial cutset is all edges of a node with minimum degree
        deg = G.degree()
        min_deg = min(deg.values())
        node = (n for n,d in deg.items() if d==min_deg).next()
        min_cut = G.edges(node)
        # reuse auxiliary digraph
        H = _aux_digraph_edge_connectivity(G)
        nodes = G.nodes()
        n = len(nodes)
        for i in range(n):
            if i == n-1:
                this_cut = minimum_st_edge_cutset(G, nodes[i],
                                                     nodes[0],
                                                     aux_digraph=H)
                if len(this_cut) < len(min_cut):
                    min_cut = this_cut
            else:
                this_cut = minimum_st_edge_cutset(G, nodes[i],
                                                     nodes[i+1],
                                                     aux_digraph=H)
                if len(this_cut) < len(min_cut):
                    min_cut = this_cut
        return min_cut
    else: # undirected
        # Based on algorithm 6 in [1]
        if not nx.is_connected(G):
            raise nx.NetworkXError('Input graph is not connected')
        # Initial cutset is all edges of a node with minimum degree
        deg = G.degree()
        min_deg = min(deg.values())
        node = (n for n,d in deg.items() if d==min_deg).next()
        min_cut = G.edges(node)
        # reuse auxiliary digraph
        H = _aux_digraph_edge_connectivity(G)
        # A dominating set is \lambda-covering
        # We need a dominating set with at least two nodes
        for node in G:
            D = dominating_set(G, start_with=node)
            v = D.pop()
            if D:
                break
        else:
            #raise nx.networkXError('No suitable dominating set found')
            return min_cut
        for w in D:
            this_cut = minimum_st_edge_cutset(G, v, w, aux_digraph=H)
            if len(this_cut) < len(min_cut):
                min_cut = this_cut
        return min_cut
