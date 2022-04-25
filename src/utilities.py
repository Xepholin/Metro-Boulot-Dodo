def print_usage():
    print("\n  # USAGE\n"
         " Itinéraire :\n"
         " python main.py <Nom du fichier de donnée> <Nom du station de départ> <Nom du station d'arrivé>\n")

def is_connected(graph):
        visited = dict.fromkeys(graph.vertices.values())
        visited = graph.DFS(visited, list(graph.vertices.values())[0])

        if (visited == graph.len_vertices()):
            return True
        else:
            return False