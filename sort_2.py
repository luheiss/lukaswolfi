def sort_2(arr):
    """Quicksort"""
    "Hello World"
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return sort_2(left) + middle + sort_2(right)


