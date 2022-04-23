from set import *
from look import *

graph = new_graph(1, "data.txt")
graph_test = new_graph(2, "data2.txt")
graph_test_test = new_graph(3, "data3.txt")

<<<<<<< Updated upstream
graphs = [graph, graph_test, graph_test_test]
=======
graphs = [graph, graph_test, graph_test_test]

for vertex in graph.vertices.values():
    print(vertex)

#min_path = graph_test_test.dijkstra(list(graph_test_test.vertices.values())[0])

#print(min_path)
>>>>>>> Stashed changes
