import MyGraph
import vertex
import math

def print_adj_matrix(adj_matrix, start_ver):
    print('graph{\ntrankdir=LR;\n\n')
    for elem in adj_matrix:
        print('\tnode[shape=circle]' + str(elem.get_index()))
        print()

    for elem in adj_matrix:
        if elem != start_ver:
            print('\t' + str(elem.get_index()) + ' -- ' + str(elem.get_predecessor()) + '[label = \"' + str(elem.get_distance()) + '\"]\n')
    print('}')

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
    print_adj_matrix(adj_vert, r)
    return


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
        for ver in adj_vert:
            print(ver.get_index(),' Predecessor: ', ver.get_predecessor(), 'Distance: ', ver.get_distance())
        print(end='\n\n')

        return G[min_ver_index]
    else:
        return None

def main():
    vertacies = []
    for index in range(0,9):
        vertacies.append(vertex.Vertex(index=index))
    for ver in vertacies:
        print(ver)

    weights = [[0,4,math.inf,math.inf,math.inf,math.inf,math.inf,8,math.inf,],
               [4,0,8,math.inf,math.inf,math.inf,math.inf,11,math.inf,],
               [math.inf,8,0,7,math.inf,4,math.inf,math.inf,2],
               [math.inf,math.inf,7,0,9,14,math.inf,math.inf,math.inf,],
               [math.inf,math.inf,math.inf,9,0,10,math.inf,math.inf,math.inf,],
               [math.inf,math.inf,4,14,10,0,2,math.inf,math.inf,],
               [math.inf,math.inf,math.inf,math.inf,math.inf,2,0,1,6],
               [8,11,math.inf,math.inf,math.inf,math.inf,1,7],
               [math.inf,math.inf,2,math.inf,math.inf,math.inf,math.inf,7,0],
               ]

    start_vertex = vertacies[0]



    graph = MyGraph.MyGraph(weights, vertacies)

    PRIM(graph.vertices, graph.adj_matrix, start_vertex)

main()

