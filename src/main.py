from set import *

graph = new_graph(1, "data.txt")

a, b = graph.edges[0]

if (graph.is_connected()):
    print("yes")
else:
    print("no")

"""
graph_test = new_graph(2, "data2.txt")

graph_test.print_neighbors()

if (graph_test.is_connected()):
    print("yes")
else:
    print("no")
"""