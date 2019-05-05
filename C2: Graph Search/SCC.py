import sys
import threading

def read_file(name):
    
    num_nodes = 875715
    file = open(name,"r")
    data = file.readlines()
    
    G = [[] for i in range(num_nodes)]
    G_rev = [[] for i in range(num_nodes)]
    
    
    for line in data:
        items = line.split()
        G[int(items[0])] += [int(items[1])]
        G_rev[int(items[1])] += [int(items[0])]
        
    return G, G_rev


def DFS1(graph_rev, i):
    global t, visited
    visited[i] = True
    
    for edge in graph_rev[i]:
        if not visited[edge]:
            DFS1(graph_rev, edge)

    finish[t] = i
    t= t+1
    
    

def DFS_loop1(graph_rev, num_nodes):
    
    global t, visited, finish
    visited = [False]*num_nodes
    finish = [None]*num_nodes
    t = 0
    for node in reversed(range(num_nodes)):
        if not visited[node]:
            DFS1(graph_rev, node)
    return finish

def DFS2(graph, i):
    
    global scc_size, visited
    visited[i] = True
    for edge in graph[i]:
        if not visited[edge]:
            DFS2(graph,edge)
    
    scc_size += 1
    
      


def DFS_loop2(graph, num_nodes):
    
    global scc_size, visited, finish
    visited = [False]*num_nodes
    scc = []
    
    for node in reversed(range(num_nodes)):
        if not visited[finish[node]]:
            scc_size = 0
            DFS2(graph, finish[node])
            scc.append(scc_size)
    return scc
    
    
def combine(graph, graph_rev):
    
    num_nodes = 875715
    finish = DFS_loop1(graph_rev, num_nodes)
    scc = DFS_loop2(graph, num_nodes)
    return scc

def main():
    graph, graph_rev = read_file('SCC.txt')
    
    scc = combine(graph, graph_rev)
    
    print(','.join(map(lambda x: str(x), sorted(scc)[::-1][:5])))
    #print(sorted(scc)[:5])
    
    
if __name__ == '__main__':
    threading.stack_size(67108864) # 64MB stack
    sys.setrecursionlimit(2 ** 20)  # approx 1 million recursions
    thread = threading.Thread(target = main) # instantiate thread object
    thread.start() # run program at target
