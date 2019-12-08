from MyGraph import MyGraph
from operator import itemgetter


def MST_Kruskal(G: MyGraph):
    # Initializes the a_forest to have no connections, i.e. all are 0
    a_forest = [[0 for y in G.vertices] for x in G.vertices]

    # The list of edges is empty to be filled.
    edge_list = []
    to_diagonal = 1
    # Yields a list that contains the edges, via tuples of form (<vert_start>, <vert_end>, <weight>)
    for x in range(0, len(G.vertices)):
        for y in range(0, to_diagonal):
            if G.adj_matrix[x][y] != 0:
                edge_tup = (x, y, G.adj_matrix[x][y])
                edge_list.append(edge_tup)
        to_diagonal += 1

    # a list of sets, containing each vertex's ID / name
    le_trees = [set([x]) for x in range(0, len(G.vertices))]

    # Gypsy magic to sort this list of tuples based on the tuple[2] value (the edge's weight).
    edge_list.sort(key=itemgetter(2))

    # For each edge in the graph, taken in nondecreasing order by weight
    start_vertex = 0
    end_vertex = 1
    vertex_weight = 2
    removed = set([-1])
    for edge in range(0, len(edge_list)):
        u_tree = -1
        v_tree = -1
        for tree in range(0, len(le_trees)):
            if (edge_list[edge][start_vertex] in le_trees[tree]) and (edge_list[edge][end_vertex] not in le_trees[tree]):
                u_tree = tree
            if (edge_list[edge][end_vertex] in le_trees[tree]) and (edge_list[edge][start_vertex] not in le_trees[tree]):
                v_tree = tree
            if u_tree != -1 and v_tree != -1:
                break
        if u_tree != v_tree and (u_tree != -1) and (v_tree != -1):
            le_trees[u_tree] = le_trees[u_tree].union(le_trees[v_tree])
            le_trees[v_tree] = removed.copy()
            a_forest[edge_list[edge][start_vertex]][edge_list[edge][end_vertex]] = edge_list[edge][vertex_weight]
            a_forest[edge_list[edge][end_vertex]][edge_list[edge][start_vertex]] = edge_list[edge][vertex_weight]

    return a_forest

adj_mat = [[0,4,0,0,0,0,0,8,0],[4,0,8,0,0,0,0,0,0],[0,8,0,7,0,4,0,0,2],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]]
test_graph = MyGraph()
potato = MST_Kruskal(test_graph)
test_graph.export_as_gv()


ctr = 0
for x in range(0, 16):
    for y in range(0, 16):
        print("\t" + str(potato[x][y]), end='')
        ctr += 1
        if ctr == 16:
            print("")
            ctr = 0

exit()

