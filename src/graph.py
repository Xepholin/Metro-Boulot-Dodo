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

    def __init__(self, id = -1) -> None:
        self.id = id
        self.vertices = dict()
        self.edges = dict()
        self.edges_value = dict()
        self.vertex_nb = 0

    def get_id(self):
        return self.id
    
    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def get_edges_value(self):
        return self.edges_value

    def get_vertex_nb(self):
        return self.vertex_nb
    
    def set_id(self, id):
        self.id = id
        return self

    def set_vertices(self, vertices):
        self.vertices = vertices
        return self
    
    def set_edges(self, edges):
        self.edges = edges
        return self
    
    def set_edges_value(self, edges_value):
        self.edges_value = edges_value
        return self

    def set_vertex_nb(self, nb):
        self.vertex_nb = nb
        return self

    def add_vertex(self, vertex):
        if (isinstance(vertex, Vertex) and vertex not in self.vertices.values()):
            self.vertices[vertex.id] = vertex
            self.vertex_nb += 1
            return True
        else:
            return False

    def find_couple(self, vertex1, vertex2):
        if (vertex1 in self.vertices and vertex2 in self.vertices):
            new_vertex1 = self.vertices[vertex1]
            new_vertex2 = self.vertices[vertex2]
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

    def DFS(self, visited, vertex):
        visited[vertex] = "discovered"
        for neighbor in vertex.neighbors:
            if (visited[neighbor] is None):
                self.DFS(visited, neighbor)

        return len([vertex for vertex, discovered in visited.items() if discovered =="discovered"])

    def is_connected(self):
        visited = dict.fromkeys(self.vertices.values())
        visited = self.DFS(visited, list(self.vertices.values())[0])

        if (visited == self.vertex_nb):
            return True
        else:
            return False

    def print_vertices(self):
        for id, vertex in self.vertices.items():
            print(id, vertex.name)

    def print_neighbors(self):
        for vertex in self.vertices.values():
            vertex.print_vertex()
            print("-->", vertex.get_neighbors())

    def print_graph(self):
        for key in list(self.vertices.keys()):
            print(key + str(self.vertices[key].neighbors))