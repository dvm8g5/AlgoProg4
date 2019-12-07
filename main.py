from timing_framework import Timing
import datetime

timer = Timing()
kruskal_results = timer.test_Kruskal()
prim_results = timer.test_Prim()

t = datetime.time()
csv = open("results_{}_{}_{}.csv".format(t.hour, t.minute, t.second), "w+")
kruskal_results_spread = [["" for j in range(timer.max_edges)] for i in range(timer.max_vertices)]
prim_results_spread = [["" for j in range(timer.max_edges)] for i in range(timer.max_vertices)]

for res in kruskal_results:
    kruskal_results_spread[res.vertices][res.edges] = str(res.time)
for row in kruskal_results_spread:
    csv.write(",".join(row) + "\n")

for res in prim_results:
    prim_results_spread[res.vertices][res.edges] = str(res.time)
for row in prim_results_spread:
    csv.write(",".join(row) + "\n")

csv.write("\n")

