# Helper function: merge and count split
def merge_countsplit(b,c):
    """
    Given two sorted arrays b and c, output a merged sorted array and the number of inversions.
    
    Output:
    d, num_split: Merged array d and number of inversions.
    """
    i=0
    j=0
    k=0
    
    n1 = len(b)
    n2 = len(c)
    d = [None]*(n1+n2)
    num_split = 0
    
    # traverse over b and c
    while i<n1 and j<n2:
        if(b[i] <= c[j]):
            d[k] = b[i]
            i+=1
            k+=1
        else:
            d[k] = c[j]
            num_split += n1 - i
            j+=1
            k+=1
    
    while i<n1:
        d[k] = b[i]
        i+=1
        k+=1
        
    while j<n2:
        d[k] = c[j]
        j+=1
        k+=1
    return d, num_split

def sort_and_count(a):
    """
    Given array a, output a sorted array and the total number of inversions.
    
    Output:
    d, num_inv: Sorted array d and number of inversions.
    """
    n = len(a)
    
    if n <=1:
        return a,0
    mid = n//2
    
    b,x = sort_and_count(a[:mid])
    c,y = sort_and_count(a[mid:])
    d,z = merge_countsplit(b,c)
    
    num_inv = x+y+z
    return d, num_inv
    
    
    num_inv = x+y+z
    return d, num_inv
