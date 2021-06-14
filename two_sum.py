from typing import List

def twoSum(ls: List[int], target: int) -> List[int]:
    for i in range(len(ls)):
        for j in range(len(ls)-i):
            if ls[i] + ls[j] == target:
                return i, j

nums = [2,7,11,15]
target = 18

print(twoSum(nums, target))
