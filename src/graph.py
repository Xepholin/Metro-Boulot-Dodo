class Vertex(object):
    """Un sommet d'un graphe"""

    def __init__(self, id = 0, name = "") -> None:
        self.id = id
        self.name = name
        self.neighbors = []

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    def get_neighbors(self):
        return dict([[(name, id) for id, name in vertex] for vertex in self.neighbors])

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

class Graph(object):
    """Un graphe simple"""

    vertrices = dict()
    edges = dict()

    def __init__(self) -> None:
        pass

    def add_vertex(self, vertex):
        if (isinstance(vertex, Vertex) and vertex not in self.vertrices):
            self.vertrices.update([(vertex.name, vertex)])
            return True
        else:
            return False
        
    def add_edge(self, vertex1, vertex2, time):
        for vertex in self.vertrices.values():
            if (vertex1 == vertex.get_id()):
                new_vertex1 = vertex
            elif (vertex2 == vertex.get_id()):
                new_vertex2 = vertex

        #TODO Debug this section
        """
        if (new_vertex1 in self.vertrices and new_vertex2 in self.vertrices):
            self.edges.update([((new_vertex1, new_vertex2), time)])
            for name, vertex in self.vertrices:
                if (name == new_vertex1.get_name()):
                    vertex.add_neighbor(new_vertex2)
                if (name == new_vertex2.get_name()):
                    vertex.add_neighbor(new_vertex1)
            return True
        else:
            return False
        """
    
    def print_graph(self):
        for key in list(self.vertrices.keys()):
            print(key + str(self.vertrices[key].neighbors))