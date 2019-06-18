# The following code implements the knapsack problem with bottom-up dynamic programming approach.

def read_file(name):
    """Given the path/nname of a file ,return the Values list, Weights list,
       capacity and number of jobs.
    """
    file = open(name, 'r')
    data = file.readlines()
    
    capacity = int(data[0].split()[0])
    n =int(data[0].split()[1])
    # Create two lists to store values and sizes
    V = [0]*(n+1)
    W = [0]*(n+1)
    for index, line in enumerate(data[1:]):
        V[index+1]=int(line.split()[0])
        W[index+1]=int(line.split()[1])
        
    return V, W, capacity, n

V,W, capacity, n = read_file('knapsack1.txt')

def knapsack_dynamic(V, W, capacity, numbers):
    """Return the matrix of maximum value
    """
    # initialize the 2-d array
    A = [[0]*(capacity+1) for x in range(numbers+1)]
    for i in range(1,numbers+1):
        for j in range(capacity+1):
            # make sure the size of current is not larger than the current capacity.
            if W[i]>j:
                A[i][j] = A[i-1][j]
            else:
                
                A[i][j] = max(A[i-1][j],A[i-1][j-W[i]]+V[i])
    return A


def main():
    V,W, capacity, n = read_file('knapsack1.txt')
    A = knapsack_dynamic(V,W, capacity, n)
    # return the largest value of the matrix.
    print(A[-1][-1])
    
if __name__ == '__main__':
    main()
