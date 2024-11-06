# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/description/
# TC: O(N)
# SC: O(N)
# YT: https://www.youtube.com/@eka_code

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        N = len(nums)
      
        # sum from 0 to i index
        prefix = [0]*N
        prefix[0] = nums[0]
        for i in range(1, N):
            prefix[i] += prefix[i-1] + nums[i]
        
        # find the max value of range k
        res = prefix[k-1]
        for i in range(k, N):
            res = max(res, prefix[i] - prefix[i-k])
          
        # return the average value of the k length subarray
        return res/k
