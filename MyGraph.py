
import random
import vertex


class MyGraph:
    def __init__(self, adj_matrix: [int] = [], vertices: [vertex.Vertex] = []):
        self.adj_matrix = adj_matrix
        self.vertices = vertices

    def init_random(self, vertex_count: int, edge_count: int):
        if edge_count > vertex_count ** 2:
            return

        self.adj_matrix = []
        self.add_vertices(vertex_count)

        for i in range(edge_count):
            v1 = random.randint(0, vertex_count-1)
            v2 = random.randint(0, vertex_count-1)
            weight = random.randint(0, 10)
            self.add_edge(v1, v2, weight)

    def clear_vertex_data(self):
        for v in self.vertices:
            v.reinit()

    def add_edge(self, v1: int, v2: int, weight: int):
        self.adj_matrix[v2][v1] = weight

    def add_vertices(self, amount: int):
        for i in range(amount):
            self.vertices.append(vertex.Vertex(index=len(self.vertices)))

        for col in self.adj_matrix:     # Extend columns
            for i in range(amount):
                col.append(0)

        for i in range(amount):           # Extend rows
            self.adj_matrix.append([0 for i in range(amount)])
