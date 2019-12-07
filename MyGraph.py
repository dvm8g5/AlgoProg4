
import random
import vertex


class MyGraph:
    def __init__(self, adj_matrix: [int] = [], vertices: [vertex.Vertex] = []):
        self.adj_matrix = adj_matrix
        self.vertices = vertices

    def init_random(self, vertex_count: int, edge_count: int):
        if edge_count > (vertex_count ** 2 - vertex_count) / 2:
            print("Tried to create a graph with too many edges!")
            return
        if edge_count < vertex_count-1:
            print("Tried to create a graph with too many vertices!")
            return

        self.adj_matrix = []
        self.add_vertices(vertex_count)
        connected_verts = [0]  # The vertices that this graph connects

        for i in range(edge_count):
            # Pick v1 from currently-spanned vertices
            v1 = random.choice(connected_verts)
            # Pick v2 from either non-spanned vertices, or a random vertex if all are spanned
            v2 = random.choice([i for i in range(vertex_count) if i not in connected_verts or len(connected_verts) >= vertex_count])
            while v1 == v2 or self.adj_matrix[v1][v2] != 0 or self.adj_matrix[v2][v1] != 0:
                v1 = random.randint(0, vertex_count)
                v2 = random.randint(0, vertex_count)

            weight = random.randint(1, 10)
            self.add_edge(v1, v2, weight)
            self.add_edge(v2, v1, weight)

            if v2 not in connected_verts:
                connected_verts.append(v2)

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

    def export_as_gv(self):
        print("\ndigraph D {")
        for i in range(len(self.adj_matrix)):
            for j in range(i, len(self.adj_matrix[i])):
                if self.adj_matrix[i][j] > 0:
                    print("{} -> {}[label=\"{}\"]".format(i, j, self.adj_matrix[i][j]))
        print("}\n")
