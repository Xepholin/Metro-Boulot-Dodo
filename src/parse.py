def parse(file):
    vertices = dict()
    edges = dict()
    ligne = dict()
    terminus = dict()

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
            elif (line.startswith('T')):
                number = parse_terminus(line)
                terminus[number[0]] = number[1:]
            else:
                continue
            
    return vertices, edges, ligne, terminus

def parse_vertex(string):
    buff = string.split(" ")
    number = int(buff[1])
    name = ""

    for i in range(2, len(buff)):
        name = name + " " + buff[i]
    
    name = name[:-1].rstrip().lstrip()
    name = rename(name).lower()
    
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
    if (tmp[-1] == '\n'):
        del buff[-1]
        buff.append(tmp[:-1])

    for i in range (1, len(buff)):
        buff[i] = int(buff[i])

    return buff

def parse_terminus(string):
    buff = string.split(" ")
    del buff[0]
    tmp = buff[-1]
    if (tmp[-1] == '\n'):
        del buff[-1]
        buff.append(tmp[:-1])

    for i in range (1, len(buff)):
        buff[i] = int(buff[i])
    
    return buff
    
def rename(name):
    name = name.replace('Ã©', 'e').replace('Ã‰', 'E').replace('Ã¨', 'e').replace('Ã§', 'c').replace('Ã¢', 'a').replace('Ã´', 'o').replace('Ãª', 'e').replace('Ã®', 'i').replace('é', 'e').replace('è', 'e').replace('à', 'a').replace('â', 'a').replace('ê', 'e').replace('û', 'u').replace('î', 'i').replace('ô', 'o').replace('ç', 'c').replace('ù', 'u').replace('À', 'A').replace('É', 'E').replace('È', 'E').replace('Ç', 'C')
    return name