from graph import *
from parse import *
from set import *

sommets, aretes = parse("data.txt")

vertrices = new_vertrices(sommets)

print(vertrices[0].get_id(), vertrices[0].get_name())

graph = new_graph(vertrices, aretes) 

print(graph.edges.items())