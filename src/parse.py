def parse(file):
    edge = dict()
    vertice = dict()

    with open(file, 'r') as data:
        for line in data:
            if (line.startswith('#')):
                continue
            elif (line.startswith('V')):
                number, name = parse_edge(line)
                edge.update([(number, name)])
            elif (line.startswith('E')):
                edge1, edge2, time = parse_vertice(line)
                vertice.update([((edge1, edge2), time)])
            else:
                continue
    
    return edge, vertice

def parse_edge(string):
    buff = string.split(" ")
    number = int(buff[1])
    name = ""

    for i in range(2, len(buff)):
        name = name + " " + buff[i]
    
    name = name[:-1].rstrip().lstrip()
    name = rename(name)
    
    return number, name

def parse_vertice(string):
    buff = string.split(" ")
    edge1 = int(buff[1])
    edge2 = int(buff[2])
    time = int(buff[3])

    return edge1, edge2, time

def rename(name):
    name = name.replace('Ã©', 'e').replace('Ã‰', 'E').replace('Ã¨', 'e').replace('Ã§', 'c').replace('Ã¢', 'a').replace('Ã´', 'o').replace('Ãª', 'e')
    return name