def parse(file):
    vertices = dict()
    edges = dict()
    ligne = dict()

    with open(file, 'r') as data:
        for line in data:
            if (line.startswith('#')):
                continue
            elif (line.startswith('V')):
                name, number = parse_vertex(line)
                vertices[number] = name
            elif (line.startswith('E')):
                vertex1, vertex2, time = parse_edge(line)
                edges[(vertex1, vertex2)] = time
            elif (line.startswith('L')):
                number = parse_line(line)
                ligne[number[0]] = number[1:]
            else:
                continue
    return vertices, edges, ligne

def parse_vertex(string):
    buff = string.split(" ")
    number = int(buff[1])
    name = ""

    for i in range(2, len(buff)):
        name = name + " " + buff[i]
    
    name = name[:-1].rstrip().lstrip()
    name = rename(name)
    
    return name, number

def parse_edge(string):
    buff = string.split(" ")
    vertex1 = int(buff[1])
    vertex2 = int(buff[2])
    time = int(buff[3])

    return vertex1, vertex2, time

def parse_line(string):
    buff = string.split(" ")
    del buff[0]  
    tmp = buff[-1]
    del buff[-1]
    buff.append(tmp[:-1])
    return buff
    
def rename(name):
    name = name.replace('Ã©', 'e').replace('Ã‰', 'E').replace('Ã¨', 'e').replace('Ã§', 'c').replace('Ã¢', 'a').replace('Ã´', 'o').replace('Ãª', 'e').replace('Ã®', 'i')
    return name