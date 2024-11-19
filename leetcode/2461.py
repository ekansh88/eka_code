# 2461. Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# TC: O(N)
# SC: O(N)
# YT: https://www.youtube.com/@eka_code

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        # Input: nums = [1,5,4,2,9,9,9], k = 3
        # Output: 15
        N = len(nums)
        res, sumis = 0, 0
        visit = set([])
        i, j = 0, 0

        for j in range(N):
            cur, begin = nums[j], nums[i]
            if cur not in visit:
                visit.add(cur)
                sumis += cur
                if j-i+1==k:
                    res = max(res, sumis)
                    i += 1
                    sumis -= begin
                    visit.remove(begin)
            else:
                while nums[i] != nums[j]:
                    visit.remove(nums[i])
                    sumis -= nums[i]
                    i += 1
                i += 1
                
        return res
