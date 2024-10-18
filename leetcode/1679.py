# 1679. Max Number of K-Sum Pairs
# https://leetcode.com/problems/max-number-of-k-sum-pairs/description/
# TC: O(N)
# SC: O(N)
# YT: https://www.youtube.com/@eka_code

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = Counter(nums)

        res = 0

        for i in dic:
            val = i
            needVal = k-val
            if needVal not in dic: continue

            if val==needVal:
                minCnt = min(dic[val], dic[needVal])//2
            else:
                minCnt = min(dic[val], dic[needVal])
                
            res += minCnt
            dic[val] -= minCnt
            dic[needVal] -= minCnt
        
        return res
