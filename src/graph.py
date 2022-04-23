class Vertex(object):
    """Un sommet d'un graphe"""

    def __init__(self, graph = -1, id = -1, name = "") -> None:
        self.graph = graph
        self.id = id
        self.name = name
        self.neighbors = []
        self.line = []

    def __str__(self):
        return "Graph : {} | ID : {} | Name : {} | Ligne : {}".format(self.graph, self.id, self.name, self.line)

    def get_graph(self):
        return self.graph

    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name

    #TODO modifier get_neighbors pour une liste de voisin, et déplacer la version actuelle pour un print()
    def get_neighbors(self):
        return [{vertex.id : vertex.name} for vertex in self.neighbors]

    def get_line(self):
        return self.line

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

    def set_line(self,newline):
        self.line = newline

    def add_line(self, line):
        self.line.append(line)

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

        return len([vertex for vertex, discovered in visited.items() if discovered == "discovered"])

    def dijkstra(self, start_vertex):
        if (isinstance(start_vertex, Vertex)):
            if (start_vertex not in self.vertices.values()):
                return -1
            else:
                unvisited = [vertex for vertex in self.vertices.values()]
                min_path = dict()
                previous_vertex_cost = dict()
                final_pre_vertex_cost = dict()
                min_path[start_vertex] = 0
                actual_cost = 0

                for vertex in unvisited:
                    previous_vertex_cost[vertex] = 2048, start_vertex 

                previous_vertex_cost[start_vertex] = 0, start_vertex
                final_pre_vertex_cost[start_vertex] = 0, start_vertex

                while (unvisited):
                    for vertex in min_path:
                        for neighbor in vertex.neighbors:
                            if (neighbor in unvisited and neighbor not in min_path):
                                if (neighbor not in previous_vertex_cost):
                                    previous_vertex_cost[neighbor] = actual_cost + self.find_edge_value((vertex, neighbor)), vertex
                                else:
                                    if (previous_vertex_cost[neighbor][0] > actual_cost + self.find_edge_value((vertex, neighbor))):
                                        previous_vertex_cost[neighbor] = actual_cost + self.find_edge_value((vertex, neighbor)), vertex
                                    else:
                                        continue
                            else:
                                continue
                    
                    actual_cost = list(previous_vertex_cost.values())[0][0]
                    min_vertex = list(previous_vertex_cost.keys())[0]

                    for vertex, values in previous_vertex_cost.items():
                        cost, pre_vertex = values
                        if (cost < actual_cost):
                            actual_cost = cost
                            min_vertex = vertex

                    min_path[min_vertex] = actual_cost
                    final_pre_vertex_cost[min_vertex] = previous_vertex_cost.get(min_vertex)
                    unvisited.remove(list(min_path.keys())[-1])
                    previous_vertex_cost.pop(min_vertex)

                return min_path, final_pre_vertex_cost
        else:
            return -1

    def print_vertices(self):
        for vertex in self.vertices.values():
            print(vertex)

    def print_neighbors(self):
        for vertex in self.vertices.values():
            print(vertex)
            print("-->", vertex.get_neighbors())

    

