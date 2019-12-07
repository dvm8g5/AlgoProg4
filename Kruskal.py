import MyGraph


def MST_Kruskal(Graph: MyGraph, w):
    a_forest = Graph.adj_matrix
    for x in a_forest.vertices:                 # Initializes the a_forest to have no connections, i.e. all are -1
        for y in a_forest.vertices:
            a_forest.adj_matrix[x][y] = -1

    vertex_list = Graph.vertices

