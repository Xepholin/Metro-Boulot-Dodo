from graph import *

def new_vertrices(vertrices):
    buff = [Vertex() for i in range(len(vertrices))]

    i = 0

    for id, name in vertrices.items():
        buff[i].set_id(id)
        buff[i].set_name(name)
        i += 1
    
    return buff

def new_graph(id, vertrices, edges):
    new_graph = Graph(id)

    for vertex in vertrices:
        new_graph.add_vertex(vertex)
    
    for vertrices_couple, time in edges.items():
        vertex1, vertex2 = vertrices_couple
        new_graph.add_edge(vertex1, vertex2)
        new_graph.add_edge_value(vertrices_couple, time)

    return new_graph
