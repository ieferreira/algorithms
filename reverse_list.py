# given N integers find largest possible integer rearranging those numbers
from typing import List

def reverse_list(N: List[int]) -> List[int]:
    length = len(N)
    for i in range(1,length):
        item = N[i]
        j = i-1
        while j>=0 and N[j] < item:
            N[j+1] = N[j]
            j -= 1

        N[j+1] = item           
    return N

ls = [9, 4, 5, 12, 54, 32, 11]
print(reverse_list(ls))



    

