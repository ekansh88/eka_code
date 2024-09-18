# 179. Largest Number
# https://leetcode.com/problems/largest-number/description/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        N = len(nums)
        nums = list(map(str, nums))

        def cmp(a,b):
            return int(a+b) > int(b+a)

        for _ in range(N):
            for i in range(N-1):
                a, b = nums[i], nums[i+1]        
                if cmp(a,b)==0:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
        
        res = "".join(nums)
        if int(res)==0:
            return "0"
        return res
