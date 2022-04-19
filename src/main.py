from set import *
from look import *

graph = new_graph(1, "data.txt")
graph_test = new_graph(2, "data2.txt")
graph_test_test = new_graph(3, "data3.txt")

graphs = [graph, graph_test, graph_test_test]

for graph in graphs:
    if (is_connected(graph)):
        print("id :", graph.id)