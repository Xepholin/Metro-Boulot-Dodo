import sys

from set import *
from look import *

if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("error : missing command line arguments (expected 3)")
        exit(1)
    else:
        file = sys.argv[1]
        departure_name = sys.argv[2]
        arrived_name = sys.argv[3]

        departure_name = rename(departure_name).lower()
        arrived_name = rename(arrived_name).lower()

        graph = new_graph(1, file)

        for vertex in graph.vertices.values():
            if (departure_name == vertex.get_name()):
                departure = vertex
            elif (arrived_name == vertex.get_name()):
                arrived = vertex

        if (is_connected(graph)):
            graph.travel(departure, arrived)
        else:
            print("Graph is not connected")
            exit(1)

        exit(0)