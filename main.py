from timing_framework import Timing
import datetime

# Setup
timer = Timing()
kruskal_results = timer.test_kruskal()
prim_results = timer.test_prim()

# Open the .csv we're going to write to
t = datetime.time()
csv = open("results_{}_{}_{}.csv".format(t.hour, t.minute, t.second), "w+")
kruskal_results_spread = [["" for j in range(timer.max_edges)] for i in range(timer.max_vertices)]
prim_results_spread = [["" for j in range(timer.max_edges)] for i in range(timer.max_vertices)]

# Add kruskal results to the .csv file
for res in kruskal_results:
    kruskal_results_spread[res.vertices][res.edges] = str(res.exec_time)
for row in kruskal_results_spread:
    csv.write(",".join(row) + "\n")

csv.write(","*len(kruskal_results_spread[0]))

# Add prim results to the .csv file
for res in prim_results:
    prim_results_spread[res.vertices][res.edges] = str(res.exec_time)
for row in prim_results_spread:
    csv.write(",".join(row) + "\n")
