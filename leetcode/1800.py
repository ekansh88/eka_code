# 1800. Maximum Ascending Subarray Sum
# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/
# TC: O(N)
# SC: O(1)
# YT: https://www.youtube.com/@eka_code 

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        N = len(nums)
        res, temp = 0, nums[0]
        
        for i in range(1, N):
            if nums[i-1] <= nums[i]:
                temp += nums[i]

            else:
                res = (res, temp)
                temp = nums[i]

        return res
