# Helper function: merge
def merge(b, c):
    """
    Arguments: 
    Array1, Array2: Two sorted arrays b and c.
    
    Return:
    array_d: The merged version of b and c
    """
    i = 0
    j = 0
    k = 0
     
    
    n1 = len(b)
    n2 = len(c)
    array_d = [None]*(n1+n2)
    
    # traverse both arrays
    while i<n1 and j<n2:
        if b[i] <= c[j]:
            array_d[k] = b[i]
            i+=1
            k+=1
        else:
            array_d[k] = c[j]
            j+=1
            k+=1

    while i < n1:
        array_d[k] = b[i]
        i+=1
        k+=1
    while j < n2:
        array_d[k] = c[j]
        j+=1
        k+=1
        
    return array_d
    
# Two implementations of merge sort
def merge_sort(array_a, h,k):
    """
    Sort the array array_a[h..k]
    """
    if k-h+1<=1:
        return array_a[h:k+1]
    mid = (h+k)//2
    left = merge_sort(array_a, h,mid)
    right = merge_sort(array_a, mid+1, k)
    
    sorted_a = merge(left, right)
    
    return sorted_a
    
def merge_sort_all(array_a):
    """
    sort the array a
    """
    
    n = len(array_a)
    if n <=1:
        return array_a
    mid = n//2
    
    left = merge_sort_all(array_a[:mid])
    right = merge_sort_all(array_a[mid:])
    
    sorted_a = merge(left, right)
    
    return sorted_a
