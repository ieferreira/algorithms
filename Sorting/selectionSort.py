from typing import List
import random 

def locateSmallest(ls,s, e):
    i = s
    j = i

    while i<=e:        
        if ls[j] > ls[i]:
            j = i
        i += 1

    return j
    

def selectionSort(ls: List) -> List:
    mini = 0
    i = 0
    j = len(ls)
    while i < j -1 :
        mini = locateSmallest(ls,i, j-1)
        ls[i], ls[mini] = ls[mini], ls[i]
        i += 1
        
    return ls



ls = random.sample(range(100), 10)
print(ls)
print(locateSmallest(ls, 0, len(ls)-1))
print(selectionSort(ls))

