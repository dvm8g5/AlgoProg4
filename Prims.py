import MyGraph
import vertex
import math

def PRIM(G, w, r: vertex):
    for ver in G:
        ver.set_distance(math.inf)
        ver.set_predecessor(None)
    G[r.get_index()].set_distance(0)

    adj_vert = []
    adj_vert.append(G[r.get_index()])
    Q = G
    while Q is not None:
        u = function(G, w, adj_vert)
        Q.remove(u)



def function(G: [vertex], w, adj_vert):
    min_edge = math.inf
    min_ver = None
    min_ver_index = None
    predecessor_index = None
    for ver in adj_vert:
        ver_index = ver.get_index()
        for index in range(len(w[ver_index])):
            if w[ver_index][index] < min_edge and G[index].get_preecessor == None:
                min_ver = G[index]
                min_ver_index = index
                min_edge = w[ver_index][index]
                predecessor_index = ver.get_index()

    adj_vert.append(min_ver)
    G[min_ver_index].set_predecessor = predecessor_index
    G[min_ver_index].set_distance = w[predecessor_index][min_ver_index]

    return G[min_ver]

def main():



def EXTRACT_MIN(w, adjacent_ver):
    min_edge = math.inf
    min_ver = None

    for ver in adjacent_ver:
        adj_edge_weight = w[vertex_index][ver.get_index()]
        if adj_edge_weight < min_edge:
            min_edge = adj_edge_weight
            min_ver = ver

    return min_ver


def Adj(G, w, v, adjacent_ver: [vertex] = []):
    vertex_index = v.get_index()
    for index in range(len(w[vertex_index])):
        if w[vertex_index][index] != math.inf:
           adjacent_ver.append(G[index]) 
      
    return adjacent_ver