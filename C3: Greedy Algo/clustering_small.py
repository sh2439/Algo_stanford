from operator import attrgetter

class unionfind:
    """An implementation of union-find data structure by rank.
    """
    
    def __init__(self,n):
        """Initialize an union-find with n items(objects).
        """
        self.root = list(range(n))
        self.rank = [0]*n
        self.num = n # the number of clusters
    
    def find(self, x):
        """Find the root(pointer) of the item x. Using path compression.
        """
        s_list = self.root
        if s_list[x] != x:
            s_list[x] = self.find(s_list[x])
        return s_list[x]
    
    def count(self):
        return self.num
        
    def union(self, x,y):
        """Union x and y.
        """
        s = self.root
        rank_list = self.rank
        
        s1 = self.find(x)
        s2 = self.find(y)
        
        if s1 == s2:
            return
        
        self.num -= 1
        if rank_list[s1] == rank_list[s2]:
            s[s2] = s1
            rank_list[s1] +=1
        elif rank_list[s1]>rank_list[s2]:
            s[s2] = s1
        else:
            s[s1] = s2
            
    def connected(self, x, y):
        """Check if x and y are in the same cluster.
        """
        return self.find(x) == self.find(y)
            

class Edge:
    """An instance is an edge with:
        the 'from' vertex
        the 'to' vertex
        the cost of the edge
        
    """
    def __init__(self, from_node, to_node, cost):
        self.from_node = from_node
        self.to_node = to_node
        self.cost = cost

def read_file(name):
    """Given the path/name of the file, return a list of object Edge.
    """
    
    file = open(name, 'r')
    data = file.readlines()
    
    # Initialize the edges
    edges = []
    
    for line in data[1:]:
        item = line.split()
        edges.append(Edge(int(item[0]) -1 , int(item[1]) -1 , int(item[2])))
        
    return edges

def clustering(edges, num_clusters, num_vertices):
    """Return the minimum distance of the separate vertices.
    """
    # sort the edges 
    edges = sorted(edges, key = attrgetter('cost'))
    
    UF = unionfind(num_vertices)
    

    for edge in edges:
        if not UF.connected(edge.from_node,edge.to_node) and UF.count()!= num_clusters:
            UF.union(edge.from_node,edge.to_node)
        
        if not UF.connected(edge.from_node,edge.to_node) and UF.count()== num_clusters:
            return edge.cost   
        
    
    
def main():
    edges = read_file('clustering1.txt')
    
    max_dis = clustering(edges, 4, 500)
    return max_dis

if __name__ =='__main__':
    t = main()
    print(t)

