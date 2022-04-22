class Vertex(object):
    """Un sommet d'un graphe"""

    def __init__(self, graph = -1, id = -1, name = "") -> None:
        self.graph = graph
        self.id = id
        self.name = name
        self.neighbors = []

    def __str__(self):
        return "Graph : {} | ID : {} | Name : {}".format(self.graph, self.id, self.name)

    def get_graph(self):
        return self.graph

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    #TODO modifier get_neighbors pour une liste de voisin, et déplacer la version actuelle pour un print()
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

class Graph(object):
    """Un graphe simple"""

    def __init__(self, id = -1) -> None:
        self.id = id
        self.vertices = dict()
        self.edges = dict()
        self.edges_value = dict()

    def get_id(self):
        return self.id
    
    def get_vertices(self):
        return self.vertices

    def get_edges(self):
        return self.edges

    def get_edges_value(self):
        return self.edges_value
    
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

    def len_vertices(self):
        return len(self.vertices)

    def len_edges(self):
        return len(self.edges)

    def len_edges_value(self):
        return len(self.edges_value)

    def add_vertex(self, vertex):
        if (isinstance(vertex, Vertex) and vertex not in self.vertices.values()):
            self.vertices[vertex.id] = vertex
            return True
        else:
            return False

    def find_vertex(self, id):
        for vertex in self.vertices.values():
            if (vertex.get_id() == id):
                return vertex

    def find_couple(self, vertex1, vertex2):
        if (vertex1 in self.vertices and vertex2 in self.vertices):
            new_vertex1 = self.vertices[vertex1]
            new_vertex2 = self.vertices[vertex2]
            return new_vertex1, new_vertex2
        else:
            return 0

    def find_edge(self, couple):
        temp = []
        if (isinstance(couple, tuple)):
            vertex1, vertex2 = couple
            if (isinstance(vertex1, Vertex) and isinstance(vertex2, Vertex)):

                for key, value in self.edges.items():
                    if (vertex1 not in value or vertex2 not in value):
                        continue
                    else:
                        temp.append(key)
                
                if (len(temp) == 0):    # Cas où il n'y a pas d'arete trouvé
                    return -2
                elif (len(temp) > 1):   # Cas où il y a plusieurs aretes trouvés possèdant les mêmes sommets
                    return -3
                else:
                    return temp[0]
            else:
                return -1
        else:
            return -1
            
    def add_edge(self, vertex1, vertex2):
        couple = self.find_couple(vertex1, vertex2)

        if (couple and self.find_edge(couple) == -2):
            new_vertex1, new_vertex2 = couple
            self.edges[len(self.edges)] = [new_vertex1, new_vertex2]
            new_vertex1.add_neighbor(new_vertex2)
            new_vertex2.add_neighbor(new_vertex1)
            return True
        else:
            return False

    def add_edge_value(self, couple, time):
        temp = []
        if (isinstance(couple, tuple)):
            new_vertex1, new_vertex2 = couple

            new_vertex1 = self.find_vertex(new_vertex1)
            new_vertex2 = self.find_vertex(new_vertex2)

            for key, value in self.edges.items():
                if (new_vertex1 not in value or new_vertex2 not in value):
                    continue
                else:
                    new_couple = new_vertex1, new_vertex2
                    index = self.find_edge(new_couple)

                    if (index < 0):
                        return False
                    else:
                        self.edges_value[index] = time
                        return True
        else:
            return False

    def find_edge_value(self, couple):
        id = self.find_edge(couple)

        if (id < 0):
            return -1
        else:
            return self.edges_value.get(id)

    def DFS(self, visited, vertex):
        visited[vertex] = "discovered"
        for neighbor in vertex.neighbors:
            if (visited[neighbor] is None):
                self.DFS(visited, neighbor)

        return len([vertex for vertex, discovered in visited.items() if discovered =="discovered"])

    def dijkstra(self, start_vertex):
        if (isinstance(start_vertex, Vertex)):
            if (start_vertex not in self.vertices.values()):
                return -1
            else:
                previous_min_path = dict()
                min_path = dict()
                visited = [start_vertex]
                discard = []
                list_cost = []

                for vertex in self.vertices.values():
                    previous_min_path[vertex] = start_vertex, 100**100          # infinite
                
                min_path[start_vertex] = 0
                previous_min_path[start_vertex] = start_vertex, 0

                while (len(min_path) != self.len_vertices()):
                    temp, actual_time = list(min_path[len(min_path)-1])
                    for vertex in min_path:
                        for neighbor in vertex.neighbors:
                            if (neighbor not in min_path and neighbor not in discard):
                                edge_time = self.find_edge_value((vertex, neighbor))
                                visited.append(neighbor)
                                new_cost = actual_time + edge_time
                                previous_min_path[neighbor] = vertex, new_cost
                                list_cost.append(new_cost)
                            elif (neighbor in min_path and neighbor not in discard):
                                pre_vertex, time = list(previous_min_path[neighbor])
                                if (time > actual_time + edge_time):
                                    previous_min_path[neighbor] = vertex, cost + new_cost
                        
                    cost += min(list_cost)

                    for key, value in previous_min_path.items():
                        pre_vertex, time = value
                        if (time == cost):
                            min_path[key] = cost
                            discard.append(vertex)
                            previous_min_path.pop(key)
                            break
                    print(vertex.name)
                    
                    print(previous_min_path)
            
                return min_path
        else:
            return -1

    def print_vertices(self):
        for vertex in self.vertices.values():
            print(vertex)

    def print_neighbors(self):
        for vertex in self.vertices.values():
            print(vertex)
            print("-->", vertex.get_neighbors())

    

