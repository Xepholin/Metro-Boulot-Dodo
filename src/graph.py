class Vertex(object):
    """Un sommet d'un graphe"""

    def __init__(self, graph = -1, id = -1, name = "") -> None:
        self.graph = graph
        self.id = id
        self.name = name
        self.neighbors = []

    def get_graph(self):
        return self.graph

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_neighbors(self):
        return [{vertex.id : vertex.name} for vertex in self.neighbors]

    def set_graph(self, graph):
        self.graph = graph
        return self

    def set_id(self, id):
        self.id = id
        return self
    
    def set_name(self, name):
        self.name = name
        return self

    def set_neighbors(self, list):
        self.neighbors = list
        return self

    def add_neighbor(self, vertex):
        if (vertex not in self.neighbors):
            self.neighbors.append(vertex)

    def print_vertex(self):
        print("Graph : {} | ID : {} | Name : {}".format(self.graph, self.id, self.name))

class Graph(object):
    """Un graphe simple"""

    def __init__(self, id = -1, vertrices = dict(), edges = dict(), edges_value = dict()) -> None:
        self.id = id
        self.vertrices = vertrices
        self.edges = edges
        self.edges_value = edges_value

    def get_id(self):
        return self.id
    
    def get_vertrices(self):
        return self.vertrices

    def get_edges(self):
        return self.edges

    def get_edges_value(self):
        return self.edges_value
    
    def set_id(self, id):
        self.id = id
        return self

    def set_vertrices(self, vertrices):
        self.vertrices = vertrices
        return self
    
    def set_edges(self, edges):
        self.edges = edges
        return self
    
    def set_edges_value(self, edges_value):
        self.edges_value = edges_value
        return self

    def add_vertex(self, vertex):
        if (isinstance(vertex, Vertex) and vertex not in self.vertrices.values()):
            self.vertrices[vertex.id] = vertex
            return True
        else:
            return False

    def find_couple(self, vertex1, vertex2):
        if (vertex1 in self.vertrices and vertex2 in self.vertrices):
            new_vertex1 = self.vertrices[vertex1]
            new_vertex2 = self.vertrices[vertex2]
            return new_vertex1, new_vertex2
        else:
            return 0
            
    def add_edge(self, vertex1, vertex2):
        couple = self.find_couple(vertex1, vertex2)
        new_vertex1, new_vertex2 = couple
        if (couple):
            self.edges[len(self.edges)] = couple
            new_vertex1.add_neighbor(new_vertex2)
            new_vertex2.add_neighbor(new_vertex1)
            return True
            
        else:
            return False
            

    def find_edge(self, couple):
        if (isinstance(couple, tuple)):
            vertex1, vertex2 = couple
            if (isinstance(vertex1, Vertex) and isinstance(vertex2, Vertex)):
                if (couple in self.edges.values()):
                    for key, value in self.edges.items():
                        if (value == couple):
                            return key
                else:
                    return -1
            else:
                return -1

    def add_edge_value(self, couple, time):
        new_vertex1, new_vertex2 = couple
        for vertex1, vertex2 in self.edges.values():
            if (vertex1.get_id() == new_vertex1 and vertex2.get_id() == new_vertex2):
                new_vertex1 = vertex1
                new_vertex2 = vertex2

        if (isinstance(new_vertex1, Vertex) and isinstance(new_vertex2, Vertex)):
            new_couple = new_vertex1, new_vertex2
            index = self.find_edge(new_couple)

            if (index == -1):
                return False
            else:
                self.edges_value[index] = time
                return True
        else:
            return False


    def print_graph(self):
        for key in list(self.vertrices.keys()):
            print(key + str(self.vertrices[key].neighbors))