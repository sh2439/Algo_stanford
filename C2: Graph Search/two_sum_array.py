
import time
from bisect import bisect_left, bisect_right


start = time.time()
def read_file(name):
    """
    Given the name of the file, return the sorted array array_a.
    """

    d = set()
    
    file = open(name, 'r')
    data = file.readlines()
    
    for line in data:
        items = line.split()
        d.add((int)(items[0]))
    array_a = sorted(d)
    return array_a


def two_sum(array_a):
    """Given sorted array_a and target value t, return the result.
    """
    sum_value = set()
    for i in array_a:
        # find the indices
        left = bisect_left(array_a, -10000 - i)
        right = bisect_right(array_a, 10000-i)
        
        for j in array_a[left:right]:
            if i != j:
                sum_value.add(i+j)
    
    return len(sum_value)

    



def main():
    file = read_file('two_sum.txt')
    total = two_sum(file)
    return total

if __name__ == '__main__':
    
    total = main()
    print(total)

end = time.time()
print(end - start)
    
