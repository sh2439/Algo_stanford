# The following code implements the NP-complete problem 'Traveling Salesman Problem' .
# With dynamic programming approach, the algorithm is able to complete in reasonable time.
import numpy as np
import math
from itertools import combinations
from tqdm.auto import tqdm

def read_file(name):
    """Given the path/name of the text file, return the 
    """
    file = open(name,'r')
    data = file.readlines()
    
    # Initialize the vertices list
    vertices = []
    
    num = int(data[0][0])
    for line in data[1:]:
        item = line.split()
        vertices.append((float(item[0]), float(item[1])))
        
    return vertices

def euclidean(a,b):
    """Return the euclidean distance of a(x1,y1) and b(x2,y2)
    """
    dis = np.sqrt((a[0] - b[0])**2 + (a[1]- b[1])**2)
    return dis

def n_choose_k(n,k):
    """Return the number of combinations of 'n choose k'
    """
    return int(math.factorial(n)/(math.factorial(k)*math.factorial(n-k)))

def subset(arr, k):
    """Given array arr and integer k, find the combinations of subsets. With 1 prepend.
    """
    sub = []
    a = list(combinations(arr, k))
    for i in a:
        i = tuple([1]+list(i))
        sub.append(i)
    return sub


def find_min(A, vertices, subset, j):
    """Given subset and j, find the minimum value.
    
    """
    # remove the last vertice.
    subset = list(subset)
    subset.remove(j)
    
    s_removed = subset
    
    
    if len(s_removed)>1:
        
        s_removed = tuple(s_removed)
        mini = min(A[(s_removed, k)] + euclidean(vertices[k-1],vertices[j-1]) for k in s_removed)
    
    else:
        s_removed = 1
        mini = A[(1, 1)] + euclidean(vertices[0],vertices[j-1])
    
    return mini

def find_min_final(A,vertices):
    """Given the whole matrix(graph), find the minimum value of traveling salesman problem.
    """
    
    mini = min(A[(tuple(range(1,len(vertices)+1)), j)] + euclidean(vertices[j-1], vertices[0]) for j in range(2,len(vertices)+1))
    
    return mini

def salesman(name):
    """Main function of traveling salesman problem.
    Given the path/name of the file, return the minimum value.
    """
    
    vertices = read_file(name)
    num = len(vertices)
    
    # Initialize the matrix
    inf = 1e6
    A = {}
    A[(1,1)] = 0
    keys = {}
    indices = []
    for i in range(1, num):
        current_keys = []
        S = subset(range(2,num+1), i)
        for j in S:
            A[(j,1)] = inf
            indices.append(j)
            current_keys.append(j)
        keys[i+1] = current_keys 
    
    
    # Fill in the graph(matrix)
    for m in tqdm(range(2, num+1)):
        for key in tqdm(keys[m]):
            s = key
            #print(s)
            for j in s:
                if j !=1:
                    A[(s,j)] = find_min(A, vertices, s, j)
                        
    # Find the minimum value
    mini = find_min_final(A, vertices)              
    
    return mini
    
def main():
    mini = salesman('tsp.txt')
    print(mini)
    
    
if __name__ == '__main__':
    main()
