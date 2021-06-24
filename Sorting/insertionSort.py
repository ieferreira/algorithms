from typing import List
import random


def insertionSort(ls: List) -> List:
    idx_range = range(1, len(ls))

    for i in idx_range:
        value = ls[i]
        while ls[i-1] > value and i > 0:
            ls[i], ls[i-1] = ls[i-1], ls[i]
            i = i-1

    return ls

#Codigo de quickSort

ls = random.sample(range(100), 10)
print(ls)
print(insertionSort(ls))
