def kth_smallest_sort(arr, k):
    arr.sort()
    return arr[k-1]

b=[1,2,3,8,6,5,7,0]
kth_smallest_element=kth_smallest_sort(b, 4)
print(kth_smallest_element)