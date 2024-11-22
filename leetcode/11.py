# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/description/
# TC: O(N)
# SC: O(1)

class Solution:
    def maxArea(self, height: List[int]) -> int:
        N = len(height)
        i, j = 0, N-1
        res = 0

        while  i<j:
            res = max(res, abs(j-i)*min(height[i], height[j]))

            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        
        return res
