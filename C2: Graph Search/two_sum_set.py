### Straightforward implementation of Two Sum problem using a hash set.
### Slow!

import time

start = time.time()
def read_file(name):
    """
    Given the name of the file, return the hashset d.
    """

    d = set()
    
    file = open(name, 'r')
    data = file.readlines()
    
    for line in data:
        items = line.split()
        d.add((int)(items[0]))
    return d


def two_sum(d,t):
    """Given set d and target value t, return if target value t is the sum of two elements in d.
    """
    for key in d:
        if t-key in d and key != t/2:
            return True
       
    return False
            
    

def two_sum_all(name):
    """Given the name of the file, return the total number.
    """
    d = read_file(name)
    total = 0 
    for t in range(-10000,1000):
        if two_sum(d,t) is True:
            total+=1   
    return total



def main():
    total = two_sum_all('two_sum.txt')
    return total

if __name__ == '__main__':
    
    total = main()
    print(total)

end = time.time()
print(end - start)
