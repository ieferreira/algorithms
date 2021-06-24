import random

def bubbleSort(ls):

    ln = len(ls) -1 
    unfinished = True
    while unfinished:
        unfinished = False
        for i in range(0, ln):
            if ls[i] > ls[i+1]:
                unfinished = True
                ls[i], ls[i+1] = ls[i+1], ls[i]
    return ls

ls = random.sample(range(100), 10)
print(ls)
print(bubbleSort(ls))

    
    