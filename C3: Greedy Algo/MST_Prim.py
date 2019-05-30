
import random

def read_file(name):
	"""Given path/name of the file, return the undirected graph in list.
		list[1] is a tuple, which contains (node, weights) of node 1.

	"""
    
    
    file = open(name, 'r')
    data = file.readlines()
    
    num_nodes = 500
    
    graph = [[] for i in range(num_nodes+1)]
    for line in data[1:]:
        item = line.split()
        graph[int(item[0])] += [(int(item[1]), int(item[2]))]
        graph[int(item[1])] += [(int(item[0]), int(item[2]))]

    return graph


def Prim_MST(graph):
	"""Given the graph as a list, return the minimum spanning tree using Prim's method.
	"""
    # Initialize the visited list
    X = set()

    X.add(random.choice([i for i in range(1,len(graph))]))
    T = 0
    
    
    while(len(X) < len(graph)-1):
        edge = {}
        
        for node in X:
            for v in graph[node]:
                if v[0] not in X:
                    edge[(node, v[0])] = v[1]

        # find the shortest edge
        (u,v),dist = min(edge.items(), key = lambda x : x[1])
    
        X.add(v)
        T+=dist

    return T

  def main():
    graph = read_file('edges.txt')
    t = Prim_MST(graph)
    return t

if __name__ =='__main__':
    t = main()
    print(t)

    
        