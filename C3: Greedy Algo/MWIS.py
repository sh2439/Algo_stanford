def read_file(name):
    """Given the path/nname of the file, return the list of the weights of the nodes.
    """
    file = open(name,'r')
    data = file.readlines()
    
    weights = [0]*(int(data[0])+1)
    for index,line in enumerate(data[1:]):
        item = line.split()
        weights[index+1] = int(item[0])
    
    return weights


def WIS(weights):
    """Given the weights, return the A: optimal value, S: optimal path.
    """
    A = [0]*(len(weights))
    A[0] = 0
    A[1] = weights[1]
    
    # Find the optimal value
    for i in range(2, len(weights)):
        A[i] = max(A[i-1], A[i-2]+weights[i])
    
    # Trace back to find the optimal solution.
    S= []
    i = len(weights)-1 
    while i >= 1:
        if A[i-1] >= A[i-2]+weights[i]:
            i = i-1
        else:
            S.append(i)
            i = i-2
    
    return A, S

def main():
    w = read_file('mwis.txt')
    A,S = WIS(w)
    lista = [1,2,3,4,17,117,517,997] 
    binary = []
    for i in lista:
        if i in S:
            binary.append(1)
        else:
            binary.append(0)
    print(binary)

if __name__ == '__main__':
    main()

def read_file(name):
    """Given the path/nname of the file, return the list of the weights of the nodes.
    """
    file = open(name,'r')
    data = file.readlines()
    
    weights = [0]*(int(data[0])+1)
    for index,line in enumerate(data[1:]):
        item = line.split()
        weights[index+1] = int(item[0])
    
    return weights


def WIS(weights):
    """Given the weights, return the A: optimal value, S: optimal path.
    """
    A = [0]*(len(weights))
    A[0] = 0
    A[1] = weights[1]
    
    # Find the optimal value
    for i in range(2, len(weights)):
        A[i] = max(A[i-1], A[i-2]+weights[i])
    
    # Trace back to find the optimal solution.
    S= []
    i = len(weights)-1 
    while i >= 1:
        if A[i-1] >= A[i-2]+weights[i]:
            i = i-1
        else:
            S.append(i)
            i = i-2
    
    return A, S

def main():
    w = read_file('mwis.txt')
    A,S = WIS(w)
    lista = [1,2,3,4,17,117,517,997] 
    binary = []
    for i in lista:
        if i in S:
            binary.append(1)
        else:
            binary.append(0)
    print(binary)

if __name__ == '__main__':
    main()

