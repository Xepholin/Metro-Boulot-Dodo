def is_connected(graph):
        visited = dict.fromkeys(graph.vertices.values())
        visited = graph.DFS(visited, list(graph.vertices.values())[0])

        if (visited == graph.vertex_nb):
            return True
        else:
            return False