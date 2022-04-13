from parse import *
from set import *

sommets, aretes = parse("data.txt")

vertrices = new_vertrices(sommets)

graph = new_graph(1, vertrices, aretes)

a, b = graph.edges[0]
print("de", a.name, "à", b.name, "=", graph.edges_value[graph.find_couple(a, b)])