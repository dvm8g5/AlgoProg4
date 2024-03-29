
import random
from vertex import Vertex


class MyGraph:
    def __init__(self, adj_matrix: [int] = [], vertices: [Vertex] = []):
        self.adj_matrix = adj_matrix
        self.vertices = vertices

    # Creates a randomly-generated undirected weighted graph, with all vertices connected to every other vertex.
    def init_random(self, vertex_count: int, edge_count: int) -> None:
        if edge_count > (vertex_count ** 2 - vertex_count) / 2:
            raise Exception("Tried to create a graph with too many edges! ({} of maximum {})".format(edge_count, (vertex_count ** 2 - vertex_count) // 2))
        if edge_count < vertex_count-1:
            raise Exception("Tried to create a graph with too many vertices! ({} of maximum {})".format(vertex_count, edge_count+1))

        self.adj_matrix = []
        self.vertices = []
        self.add_vertices(vertex_count)
        connected_verts = [0]  # The vertices that this graph connects

        for i in range(edge_count):
            # Pick v1 from currently-spanned vertices
            v1 = random.choice(connected_verts)
            # Pick v2 from either non-spanned vertices, or a random vertex if all are spanned
            v2 = random.choice([i for i in range(vertex_count) if i not in connected_verts or len(connected_verts) >= vertex_count])
            while v1 == v2 or self.adj_matrix[v1][v2] != 0 or self.adj_matrix[v2][v1] != 0:
                v1 = random.randint(0, vertex_count - 1)
                v2 = random.randint(0, vertex_count - 1)

            weight = random.randint(1, 10)
            self.add_edge(v1, v2, weight)
            self.add_edge(v2, v1, weight)

            if v2 not in connected_verts:
                connected_verts.append(v2)

    # Clears all non-index vertex data
    def clear_vertex_data(self) -> None:
        for v in self.vertices:
            ind = v.index
            v.reinit()
            v.index = ind
        return

    # Rebuilds the adjacency matrix from vertex data
    def rebuild_adj_matrix(self) -> None:
        # Reset matrix
        self.adj_matrix = []
        self._expand_adj_matrix(len(self.vertices))

        # Rebuild matrix
        for v in self.vertices:
            if v.predecessor is not None:
                if v.distance is not None and self.vertices[v.predecessor].distance is not None:
                    self.adj_matrix[v.index][v.predecessor] = v.distance - self.vertices[v.predecessor].distance
                else:
                    self.adj_matrix[v.index][v.predecessor] = 1

    # Effectively removes directed edges by making the adjacency matrix symmetrical along x = y
    def make_undirected(self) -> None:
        for i in range(len(self.adj_matrix)):
            for j in range(len(self.adj_matrix)):
                if self.adj_matrix[i][j] != 0:
                    self.adj_matrix[j][i] = self.adj_matrix[i][j]

    # Adds an edge between two vertices
    def add_edge(self, v1: int, v2: int, weight: int) -> None:
        self.adj_matrix[v2][v1] = weight
        return

    # Adds the specified amount of blank vertices
    def add_vertices(self, amount: int) -> None:
        self._expand_adj_matrix(amount)
        for i in range(amount):
            self.vertices.append(Vertex(index=len(self.vertices)))
        return

    # Adds a vertex to the graph
    def add_vertex(self, vertex: Vertex):
        self._expand_adj_matrix(1)
        vertex.index = len(self.vertices)
        self.vertices.append(vertex)
        return

    # Prints the matrix to the console as GraphViz code
    def export_as_gv(self, directed: bool = False):
        print("\n{} D ".format("digraph" if directed else "graph") + "{")
        for i in range(len(self.adj_matrix)):
            for j in range(0 if directed else i, len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] > 0:
                    print("{} {} {}[label=\"{}\"]".format(i, "->" if directed else "--", j, self.adj_matrix[i][j]))
        print("}\n")
        return

    # Expands the adjacency matrix by the given amount
    def _expand_adj_matrix(self, amount: int):
        # Extend columns
        for col in self.adj_matrix:
            for i in range(amount):
                col.append(0)

        # Extend rows
        for i in range(amount):
            self.adj_matrix.append([0 for i in range(amount)])
        return
