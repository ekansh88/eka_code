# 179. Largest Number
# https://leetcode.com/problems/largest-number/description/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        N = len(nums)
        nums = list(map(str, nums))

        def cmp(a,b):
            return int(a+b) < int(b+a)

        nums = sorted(nums, key=cmp_to_key(cmp))
        
        res = "".join(nums)
        if int(res)==0:
            return "0"
        return res
    

    def anotherApproach(self, nums):
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x * 10, reverse=True)
        
        res = "".join(nums)
        if int(res)==0:
            return "0"
        return res

