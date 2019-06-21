# The following code implements the Floyd-Warshall algorithm to solve all-pairs shortest paths problem. The algorithm can either
find the shortest path of all paris or detect a negative cycle.

from tqdm import tqdm
class Edge:
    def __init__(self, from_node, to_node, weight):
        self.from_node = from_node
        self.to_node = to_node
        self.weight = weight

def read_file(name):
    """Given the path/name of the file, return the empty 3-d array(n, n, n+1).
    """
    file = open(name,'r')
    data = file.readlines()
    
    n = int(data[0].split()[0])
    m = int(data[0].split()[1])
    
    A = np.zeros((n,n,n+1))
    inf = 9999
    
    for i in range(n):
        for j in range(n):
            if i==j:
                A[i,j,0] = 0
            else:
                A[i,j,0] = inf
    for index, line in enumerate(data[1:]):
        item = line.split()
        A[int(item[0]) -1 ,int(item[1])-1,0] = int(item[2])
        
    return A

def floyd_warshall(A):
    """Given the empth 3-d array, return the minimum path(a numbber or 'Negative cycle').
    """
    n = A.shape[0]
    
    for k in tqdm(range(1, n+1)):
        for i in range(n):
            for j in range(n):
                A[i,j,k] = min(A[i,j,k-1], A[i,k-1,k-1]+A[k-1,j,k-1])
                
    
    for i in range(n):
        if A[i,i,n] <0:
            min_path = 'Negative cycle'
            return min_path
    min_path = np.min(A[:,:,n])
    
    return min_path
    
    
def main():
    A = read_file('g3.txt')
    min_path = floyd_warshall(A)
    print(min_path)

if __name__ == '__main__':
    main()
    
