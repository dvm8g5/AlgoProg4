
import timeit
import time


class TimingResult:
    def __init__(self, vertices: int, edges: int, exec_time: float):
        self.vertices = vertices
        self.edges = edges
        self.exec_time = exec_time


class Timing:
    def __init__(self, min_vertices: int = 2, max_vertices: int = 20, min_edges: int = 2, max_edges: int = 20):
        self.min_vertices = min_vertices
        self.max_vertices = max_vertices
        self.min_edges = min_edges
        self.max_edges = max_edges

    def test_kruskal(self) -> [TimingResult]:
        results = []
        for v in range(self.min_vertices, self.max_vertices):
            for e in range(self.min_edges, min((v ** 2 - v) // 2, self.max_edges)):
                snippet = "MST_Kruskal(graph, graph.vertices)"
                init = "from Kruskal import MST_Kruskal\nfrom MyGraph import MyGraph\ngraph = MyGraph().init_random({},{})".format(v, e)
                # func_time = min(timeit.repeat(snippet, init, time.clock, 10, 25) / 25 * 10 ** 9)
                func_time = 0  # TODO
                results.append(TimingResult(v, e, func_time))

        return results

    def test_prim(self) -> [TimingResult]:
        results = []
        for v in range(self.min_vertices, self.max_vertices):
            for e in range(self.min_edges, min((v ** 2 - v) // 2, self.max_edges)):
                snippet = "MST_Prim(graph.vertices, graph.adj_matrix, 0"
                init = "from Prims import PRIM\nfrom MyGraph import MyGraph\ngraph = MyGraph().init_random({},{})".format(v, e)
                # func_time = min(timeit.repeat(snippet, init, time.clock, 10, 25) / 25 * 10 ** 9)
                func_time = 0  # TODO
                results.append(TimingResult(v, e, func_time))

        return results
