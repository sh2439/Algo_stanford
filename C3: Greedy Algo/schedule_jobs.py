### The code below implements the a scheduling problem which minimizes the weighted sum of completion time of jobs.
def read_file(name):
    """Given the path/name of the file, return nthe jobs list with jobs[][0]: weight and jobs[][1]: length.
    """
    
    file = open(name,'r')
    data = file.readlines()
    
    jobs = []
    
    for line in data[1:]:
        items = line.split()
        jobs.append([int(items[0]),int(items[1])])
        
    return jobs

### according to weight - length(difference) or weight/length(ratio)
def find_order(jobs, key = 'difference' or 'ratio'):
    """Find the order of jobs according to different key(priority).
    """
    
    # find the key of the priority
    if key == 'difference':
        
        priority = [item[0] - item[1] for item in jobs]
    else:
        priority = [item[0]/item[1] for item in jobs]
    
    order = sorted(range(len(priority)), key = priority.__getitem__)
    
    order.reverse()
    
    return order
 
def compute_sum(jobs, order):
    """Given the jobs list and order, find the weighted sum of the jobs.
    """
    finish_time = 0
    weighted_sum = 0
    for i in order:
        
        finish_time += jobs[i][1]
        weighted_sum += finish_time*jobs[i][0]
        
    return weighted_sum

def main():
    
    jobs = read_file('jobs.txt')
    order = find_order(jobs, 'ratio')
    
    weighted_sum = compute_sum(jobs, order)
    
    return weighted_sum

if __name__ == '__main__':
    
    answer = main()
    print(answer)

