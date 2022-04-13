from set import *

graph = new_graph(1, "data.txt")

a, b = graph.edges[0]
print("de", a.name, "à", b.name, "=", graph.edges_value[graph.find_couple(a, b)])
print(a.get_neighbors())
print(b.get_neighbors())