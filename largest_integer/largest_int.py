class LargerNumKey(str):
    def __lt__(x, y):
        print(x+y > y+x)
        return x+y > y+x
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num

ls = [9, 4, 5, 12, 54, 32, 11]

lsObj = Solution()

sol = lsObj.largestNumber(ls)

print(sol)
