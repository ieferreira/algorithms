def quickSort(ls):

    if len(ls) <= 1:
        return ls

    pivot = ls.pop()

    less = []
    greater = []

    for i in ls:
        if i > pivot:
            greater.append(i)
        elif i < pivot:
            less.append(i)

    return quickSort(less) + [pivot] + quickSort(greater)


import random

ls = random.sample(range(100), 20)
print(ls)
print(quickSort(ls))


