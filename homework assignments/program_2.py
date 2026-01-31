def find_min_max(arr):

    if not arr:
        return None, None
        
    min_val = arr[0]
    max_val = arr[0]
    
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
        elif arr[i] > max_val:
            max_val = arr[i]
            
    return min_val, max_val


nums = [3, 5, 1, 9, 2, 8]
mn, mx = find_min_max(nums)
print(f"Minimum: {mn}, Maximum: {mx}")