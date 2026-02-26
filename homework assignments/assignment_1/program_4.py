def find_union(a, b):
    res_set = set(a) | set(b)
    return list(res_set)
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]
print(find_union(a, b)) 