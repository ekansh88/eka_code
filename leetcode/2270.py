# 2270. Number of Ways to Split Array
# https://leetcode.com/problems/problem-name
# TC: O(N)
# SC: O(1)
# YT: https://www.youtube.com/@eka_code 

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        left = nums[0]
        right = sum(nums) - left
        res = 0

        for i in range(N-1):
            if left >= right:
                res += 1
            
            left += nums[i+1]
            right -= nums[i+1]
        
        return res
