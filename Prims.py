import MyGraph
import vertex
import math

# This function takes an adjacency matrix generated from PRIM and generates a graphvis usable text file.
def print_adj_matrix(adj_matrix, start_ver):
    print('graph{\ntrankdir=LR;\n\n')
    for elem in adj_matrix:
        print('\tnode[shape=circle]' + str(elem.get_index()))
        print()

    for elem in adj_matrix:
        if elem != start_ver:
            print('\t' + str(elem.get_index()) + ' -- ' + str(elem.get_predecessor()) + '[label = \"' + str(elem.get_distance()) + '\"]\n')
    print('}')

# This function takes a list of vertexes object G, an adjacency matrix w, and a starting vertex r.
def PRIM(G, w, r: vertex):
    for ver in G:
        ver.set_distance(math.inf)
        ver.set_predecessor(None)
    G[r.get_index()].set_distance(0)
    G[r.get_index()].set_predecessor(math.inf)

    adj_vert = []
    adj_vert.append(G[r.get_index()])
    Q = G.copy()
    Q.remove(r)
    while Q != []:
        u = function(G, w, adj_vert)
        if u is not None:
            Q.remove(u)

    G[r.get_index()].set_predecessor(None)
    return

# This function is the loop from lines 8-11 in the pseudocode that extracts min and then updates weights and predecessors as needed.
def function(G: [vertex], w, adj_vert):
    min_edge = math.inf
    min_ver = None
    min_ver_index = None
    predecessor_index = None
    for ver in adj_vert:
        ver_index = ver.get_index()
        total_len = len(w[ver_index])
        for index in range(total_len):
            if index < total_len and ver_index != index and w[ver_index][index] < min_edge and G[index].get_predecessor() is None:
                min_ver = G[index]
                min_ver_index = index
                min_edge = w[ver_index][index]
                predecessor_index = ver.get_index()
                # w[ver_index][index] = math.inf

    if min_ver_index is not None:
        G[min_ver_index].set_predecessor(predecessor_index)
        G[min_ver_index].set_distance(min_edge)
        adj_vert.append(G[min_ver_index])

        return G[min_ver_index]
    else:
        return None

