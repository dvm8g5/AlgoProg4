from MyGraph import MyGraph
from operator import itemgetter

# Pre: G must be a MyGraph object with an adjacency list of V x V.
# Post: Returns an adjacency list a_forest that represents the MST found within G.
def MST_Kruskal(G: MyGraph):
    # Initializes the a_forest to have no connections, i.e. all are 0
    a_forest = [[0 for y in G.vertices] for x in G.vertices]

    # The list of edges is empty, ready to be filled.
    edge_list = []
    to_diagonal = 1     # Prevents the nested for loop from iterating unnecessarily through repeated values
    # Yields a list that contains the edges in tuples of form (<start_vert>, <end_vert>, <weight>)
    # tuples will later allow for the list of the vertices to be sorted based on edge weight, whereas a custom vertex
    # class would have proved troublesome to sort as compared to the build in python method.
    for x in range(0, len(G.vertices)):
        for y in range(0, to_diagonal):
            if G.adj_matrix[x][y] != 0:
                edge_tup = (x, y, G.adj_matrix[x][y])
                edge_list.append(edge_tup)
        to_diagonal += 1

    # Take the list of tuples and sort them in non-descending order of weights
    edge_list.sort(key=itemgetter(2))

    # a list of sets, containing each vertex's ID / name for use in ensuring no cycles are in the forest
    le_trees = [set([x]) for x in range(0, len(G.vertices))]

    # vars made for readability within code. The start, end, and weight are the [0][1][2] elements of the tuples within
    # le_trees
    start_vertex = 0
    end_vertex = 1
    vertex_weight = 2

    # Used for removing already union-ed vertices from the forest
    removed = set([-1])

    # Considers each edge in non-descending order
    for edge in range(0, len(edge_list)):
        # u_tree is the index within le_trees of the tree containing the source vertex, v_tree the destination's index
        u_tree = -1
        v_tree = -1
        # Considers each tree in the list of trees in order to avoid cycles
        for tree in range(0, len(le_trees)):
            # If the source is present but not the destination
            if (edge_list[edge][start_vertex] in le_trees[tree]) and (
                    edge_list[edge][end_vertex] not in le_trees[tree]):
                u_tree = tree
            # If the destination is present but not the source
            if (edge_list[edge][end_vertex] in le_trees[tree]) and (
                    edge_list[edge][start_vertex] not in le_trees[tree]):
                v_tree = tree
            # If the edge's start_vertex and end_vertex are found and are distinct, stop searching
            if u_tree != -1 and v_tree != -1:
                break
        # Unions the two distinct sets, removes the destination's set, and sets a_forests[i][j] amd a_forest[j][i] value
        # to the edge's weight
        if u_tree != v_tree and (u_tree != -1) and (v_tree != -1):
            le_trees[u_tree] = le_trees[u_tree].union(le_trees[v_tree])
            le_trees[v_tree] = removed.copy()
            a_forest[edge_list[edge][start_vertex]][edge_list[edge][end_vertex]] = edge_list[edge][vertex_weight]
            a_forest[edge_list[edge][end_vertex]][edge_list[edge][start_vertex]] = edge_list[edge][vertex_weight]
        print('After: ', le_trees)

    return a_forest
