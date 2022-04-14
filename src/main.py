from set import *

graph = new_graph(1, "data.txt")

if (graph.is_connected()):
    print("graph : yes")
else:
    print("graph : no")

graph_test = new_graph(2, "data2.txt")

if (graph_test.is_connected()):
    print("graph_test : yes")
else:
    print("graph_test : no")