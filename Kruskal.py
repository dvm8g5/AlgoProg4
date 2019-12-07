from MyGraph import MyGraph
from operator import itemgetter


def MST_Kruskal(G: MyGraph):
    # Initializes the a_forest to have no connections, i.e. all are 0
    a_forest = [[0 for y in G.vertices] for x in G.vertices]

    # This will be a list of "sets", or "trees" that will be used to make sure we make no cycles of nodes
    le_trees = []

    edge_list = []
    to_diagonal = 1
    # Yields a list that contains the edges, via tuples of form (<vert_start>, <vert_end>, <weight>)
    for x in range(0, len(G.vertices)):
        for y in range(0, to_diagonal):
            if G.adj_matrix[x][y] != 0:
                edge_tup = (x, y, G.adj_matrix[x][y])
                edge_list.append(edge_tup)
        to_diagonal += 1

    # Gypsy magic to sort this list of tuples based on the tuple[2] value (the edge's weight).
    edge_list.sort(key=itemgetter(2))

    # For each edge in the graph, taken in nondecreasing order by weight
    u_tree = -1
    v_tree = -2
    for edge in edge_list:
        for each_set in le_trees:
            if edge_list[edge][0] in le_trees[each_set]:
                u_tree = each_set
            if edge_list[edge][1] in le_trees[each_set]:
                v_tree = each_set
            if u_tree != v_tree:
                a_forest[edge_list[edge][0]][edge_list[edge][1]] = edge_list[edge][2]
                le_trees.append("{}{}".format(edge_list[edge][0], edge_list[edge][1]))
    return a_forest


test_graph = MyGraph()
test_graph.init_random(6, 5)
potato = MST_Kruskal(test_graph)


ctr = 0
for x in range(0, 6):
    for y in range(0, 6):
        print("\t" + str(potato[x][y]), end='')
        ctr += 1
        if ctr == 6:
            print("")
            ctr = 0

exit()

