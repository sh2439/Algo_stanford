### The following code implements the traveling salesman probblem with a greedy heuristic approach.

from tqdm import tqdm
import numpy as np

def read_file(name):
    """Given the path/name of the file, return the graph (dictionary).
    """
    file = open(name,'r')
    data = file.readlines()
    
    # initialize the graph
    g = {}
    #num = int(data[0][0])
    for line in data[1:]:
        item = line.split()
        g[int(item[0])] = (float(item[1]), float(item[2]))
        
    return g
        
g = read_file('tsp_large.txt')

def euclidean_sq(a,b):
    """Return the square euclidean distance of a(x1,y1) and b(x2,y2)
    """
    dis = (a[0] - b[0])**2 + (a[1]- b[1])**2
    return dis


def tsp(g):
    """Given the graph, return the heuristic traveling salesman problem value.
    """
    # number of cities
    num = len(g)
    
    # Initialize visited and unvisited set
    visited = []
    visited.append(1)
    
    unvisited = list(range(2, len(g)+1))
    
    final_dis = 0
    # Main loop: stop when all the cities are visited.
    for i in tqdm(range(num-1)):
        
        current_city = visited[-1]
        next_city = unvisited[0]
        
        min_dis = euclidean_sq(g[current_city], g[next_city])
    
        if len(unvisited)>1:
            for j in unvisited[1:]:
                dis = euclidean_sq(g[current_city], g[j])
                if dis < min_dis:
                    min_dis = dis
                    next_city = j
                # break the tie
                elif dis == min_dis:
                    next_city = min(next_city, j)
            
        visited.append(next_city)
        unvisited.remove(next_city)
        final_dis += np.sqrt(min_dis)
        
    final_dis += np.sqrt(euclidean_sq(g[visited[-1]], g[1]))
    
    return final_dis
        

def main():
    g = read_file('tsp_large.txt')
    best_dis = tsp(g)
    
    return best_dis


if __name__ == '__main__':
    main()
