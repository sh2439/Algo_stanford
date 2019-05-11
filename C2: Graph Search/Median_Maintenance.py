import heapq

def read_file(name):
    """Given the path of a file, return a list of numbers to be processed.
    """
    
    d = []
    file = open(name,'r')
    data = file.readlines()
    
    for line in data:
        items = line.split()
        d.append(int(items[0]))
        
    return d
  
def insert(h_low, h_high, m ):
    """Insert the item m to the heap.
    """
    # Push the m in the heap
    if m < h_low[0]:
        h_low.append(m)
        heapq._siftdown_max(h_low,0,len(h_low)-1)
    else:
        heapq.heappush(h_high, m)
    
    # Balance the two heaps
    size_diff = len(h_low) - len(h_high)
    
    if size_diff > 1:
        item = heapq._heappop_max(h_low)
        heapq.heappush(h_high,item)
    elif size_diff < -1:
        item = heapq.heappop(h_high)
        h_low.append(item)
        heapq._siftdown_max(h_low,0,len(h_low)-1)

def median_heap(d):
    """Output a list with all the medians in nsequennce.
    """
    median = []
    
    # initialize empty heaps
    h_low = []
    h_high = []
    heapq._heapify_max(h_low)
    heapq.heapify(h_high)
    
    # Push the first item into the h_low
    h_low.append(d[0])
    median.append(d[0])
    
    # Loop over all other items in d
    for m in d[1:]:
        insert(h_low, h_high, m)
        
        # Find the median
        if len(h_low)<len(h_high):
            median.append(h_high[0])
        else:
            median.append(h_low[0])
    
    return median

def main():
    
    d = read_file('Median.txt')
    median = median_heap(d)
    result = sum(median)%10000
    return result
    
    

if __name__ == '__main__':
    
    result = main()
    print(result)
