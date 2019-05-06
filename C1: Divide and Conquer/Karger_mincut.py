import random, copy

def read_file(name):
    """
        Input the file name and return a dictionary to store the graph.
    """
    
    with open(name, 'r') as data:
        line = data.read().strip().split("\n")

    graph_dict = {}
    for element in line:
        line_list = list(map(int, element.strip().split("\t")))
        graph_dict[line_list[0]] = line_list[1:]
        
    return graph_dict

def random_pick(new_dict):
    """
        Given a graph dictionary, return a randomly selected pair a and b.
    """
    a = random.choice(list(new_dict.keys()))
    b = random.choice(new_dict[a])
    
    selected_pair = (a,b)
    return selected_pair


def karger(new_dict):
    """
        Return the min_cut in a single loop/trial.
    """
    num = []
    
    while len(new_dict)>2:
        
        a,b = random_pick(new_dict)
        # merge two vertices
        new_dict[a].extend(new_dict[b])

        # add a/delete b in vertices connected with b
        for c in new_dict[b]:
            new_dict[c].remove(b)
            new_dict[c].append(a)

        # delete self-loops of vertice a
        while a in new_dict[a]:
            new_dict[a].remove(a)

        # delete vertice b
        del new_dict[b]

    for key in new_dict:
        num.append(len(new_dict[key]))
    return num[0]

def combine(n, name):
    """
        Arguments
        n: the number of iterations/trials.
        name: input file name
        
        Output
        min_cut: the minimum cut
        
    """
    graph = read_file(name)
    min_cut = 1000
    for i in range(n):
        G = copy.deepcopy(graph)
        cut = karger(G)
        if cut < min_cut:
            min_cut = cut
    return min_cut
    
