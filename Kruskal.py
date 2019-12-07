import MyGraph
from operator import itemgetter


def MST_Kruskal(G: MyGraph):
    # Initializes the a_forest to have no connections, i.e. all are 0
    a_forest = [[0 for y in G.vertices] for x in G.vertices]

    # # Creates a list of lists, representing the disjoint sets that are initially each and every vertex
    # sets = []
    # for x in G.vertices:
    #     sets.append([x])
    le_tree = []

    edge_list = []
    to_diagonal = 1
    # Yields a list that contains the edges, via tuples of form (<vert_start>, <vert_end>, <weight>)
    for x in G.vertices:
        for y in range(0, to_diagonal):
            if G.adj_matrix[x][y] != 0:
                edge_tup = (x, y, G.adj_matrix[x][y])
                edge_list.append(edge_tup)
        to_diagonal += 1

    # Gypsy magic to sort this list of tuples based on the tuple[2] value (the edge's weight).
    edge_list.sort(key=itemgetter(2))

    # For each edge in the graph, taken in nondecreasing order by weight
    u_tree = -1
    v_tree = -1
    for each_edge in edge_list:
        for each_set in le_tree:
            if edge_list[each_edge][0] in le_tree[each_set]:
                u_tree = each_set
            if edge_list[each_edge][1] in le_tree[each_set]:
                v_tree = each_set
            if u_tree != v_tree:
                a_forest[edge_list[each_edge][0]][edge_list[each_edge][1]] = edge_list[each_edge][2]
                le_tree.append("{}{}".format(edge_list[each_edge][0], edge_list[each_edge][1]))
    return a_forest





