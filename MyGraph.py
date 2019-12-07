
import random


class MyGraph:
    def __init__(self, adj_matrix, vertices):
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

    def add_edge(self, v1, v2, weight):
        self.adj_matrix[v2][v1] = weight

    def add_vertices(self, amnt):
        for col in self.adj_matrix:     # Extend columns
            for i in range(amnt):
                col.append(0)

        for i in range(amnt):           # Extend rows
            self.adj_matrix.append([0 for i in range(amnt)])
