from graph import *
from parse import *

def new_vertices_edges_lines(graphID, file):
    """Create a list of new vertices, edges, lines
    
    Keyword arguments:
    graphID -- type int which is add for vertices data
    file    -- the path of a file with data

    Return value:
    --> - list of object of class Vertex()
        - edges with dictionary format 
    """
    temp, edges, temp2, temp3 = parse(file) 

    vertices = [Vertex() for i in range (len(temp))]
    lines = [Line() for i in range (len(temp2))]

    i = 0

    for id, name in temp.items():
        vertices[i].set_graph(graphID)
        vertices[i].set_id(id)
        vertices[i].set_name(name)

        i += 1
    
    j = 0

    for name, list in temp2.items():
        lines[j].set_name(name)
        lines[j].set_stations(list)

        j += 1

    for vertex in vertices:
        for line in lines:
            for id in line.stations:
                if (id == vertex.get_id()):
                    vertex.set_line(line)

    for list_vertex_id in temp3.values():
        for vertex in vertices:
            for vertex_id in list_vertex_id:
                if (vertex.get_id() == vertex_id):
                    list_vertex_id[list_vertex_id.index(vertex_id)] = vertex

    for name, list_station in temp3.items():
        for i in range (len(lines)):
            if (lines[i].name == name):
                for vertex in list_station:
                    lines[i].set_terminus(list_station)

    return vertices, edges

def new_graph(id, file):
    """Create a graph
    
    Keyword arguments:
    id   -- type int for the id of the new graph
    file -- the path of a file with data

    Return value:
    --> object of class Graph()
    """

    vertices, edges = new_vertices_edges_lines(id, file)

    new_graph = Graph(id)

    for vertex in vertices:
        new_graph.add_vertex(vertex)
    
    for vertices_couple, time in edges.items():
        vertex1, vertex2 = vertices_couple
        new_graph.add_edge(vertex1, vertex2)
        new_graph.add_edge_value(vertices_couple, time)

    return new_graph