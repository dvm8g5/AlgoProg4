import MyGraph
import math


def MST_Kruskal(G: MyGraph):
    a_forest = G.adj_matrix
    for x in a_forest.vertices:                 # Initializes the a_forest to have no connections, i.e. all are -1
        for y in a_forest.vertices:
            a_forest.adj_matrix[x][y] = 0



    edge_list = {}
    to_diagonal = 1
    for x in G.vertices:                        # Yields a dictionary that contains all edges and their weights, denoted by the key being "<start_vertex><end_vertex>
        for y in range(0, to_diagonal):
            if G.adj_matrix[x][y] != 0:
                edge_list["{}{}".format(x, y)] = G.adj_matrix[x][y]
        to_diagonal += 1

    min_edge = math.inf
    min_edge_row = 0
    min_edge_col = 0
    to_diagonal = 1
    for x in G.vertices:                        # determines the smallest edge weight of all vertices
        for y in range(0, to_diagonal):
            if edge_list["{}{}".format(x, y)] < min_edge:
                min_edge = edge_list["{}{}".format(x, y)]
                min_edge_row = x
                min_edge_col = y
        to_diagonal += 1






    return





