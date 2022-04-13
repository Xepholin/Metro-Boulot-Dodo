from graph import *
from parse import *

def new_vertrices_edges(file):
    temp, edges = parse(file)

    vertrices = [Vertex() for i in range(len(temp))]

    i = 0

    for id, name in temp.items():
        vertrices[i].set_id(id)
        vertrices[i].set_name(name)
        i += 1
    
    return vertrices, edges

def new_graph(id, file):
    vertrices, edges = new_vertrices_edges(file)

    new_graph = Graph(id)

    for vertex in vertrices:
        new_graph.add_vertex(vertex)
    
    for vertrices_couple, time in edges.items():
        vertex1, vertex2 = vertrices_couple
        new_graph.add_edge(vertex1, vertex2)
        new_graph.add_edge_value(vertrices_couple, time)

    return new_graph
