import time
from ast import literal_eval

def read_file(name,num_nodes=201):
    """Given the name of the file , return the graph in list.
    """
    graph = [None]*num_nodes
    
    file = open(name)
    data = file.readlines()
    for line in data:
        items = line.split()
        graph[int(items[0])] = [literal_eval(a) for a in items[1:]]
    
    return graph
        


    
def dijkstra(graph, num_nodes=201):
    """The Main function of Dijkatra's shortest path algorithm.
    """
    
    # Store the vertices that have been processed.
    visited = []
    visited.append(1)
    
    
    # Store the distances to all other vertices. Initialize with 10000.
    dis = [100000]*(num_nodes)
    dis[1] = 0
    
    
    while len(visited) < (num_nodes-1):
        
        # dictionary to store the edge and the distances
        short_dist = {}
        for node in visited:
            for v in graph[node]:
                if v[0] not in visited:
                    short_dist[(node, v[0])] = dis[node] + v[1]
        # find the shortest edge
        (node, edge), dist = min(short_dist.items(), key=lambda x: x[1])  
        dis[edge] = dist
        visited.append(edge)
        
    return dis
