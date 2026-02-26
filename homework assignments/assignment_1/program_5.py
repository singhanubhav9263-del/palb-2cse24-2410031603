def largest_of_arr(arr):
    largest=0
    for x in range(len(arr)):
        if (arr[x]>largest):
            largest=arr[x]
    return largest
b=[1,2,5,4,6,7,8,48,188,0]
largest_element=largest_of_arr(b)
print(largest_element)
