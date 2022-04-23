from graph import *
from parse import *

def new_vertices_edges(graphID, file):
    temp, edges, line = parse(file)

    vertices = [Vertex() for i in range(len(temp))]

    i = 0

    for id, name in temp.items():
        vertices[i].set_graph(graphID)
        vertices[i].set_id(id)
        vertices[i].set_name(name)

        i += 1
    
    for vertex in vertices:
        for num_line, list_vertex in line.items():
            for id in list_vertex:
                if vertex.get_id() == id:
                    print("metal gear")
                    vertex.add_line(num_line)
        
  
    return vertices, edges

def new_graph(id, file):
    vertices, edges = new_vertices_edges(id, file)

    new_graph = Graph(id)

    for vertex in vertices:
        new_graph.add_vertex(vertex)
    
    for vertices_couple, time in edges.items():
        vertex1, vertex2 = vertices_couple
        new_graph.add_edge(vertex1, vertex2)
        new_graph.add_edge_value(vertices_couple, time)

    return new_graph
