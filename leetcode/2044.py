# 2044. Count Number of Maximum Bitwise-OR Subsets
# TC: O(2**N)
# SC: O(2**N)
# LC Link: https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/
# YT Link: https://www.youtube.com/@eka_code

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        # i have to find the ferq of the max bitwise OR of the subset
        N = len(nums)
        dic = defaultdict(int)

        def dfs(i, res):
            if i>=N:
                dic[res] += 1
                return  

            # i can pick this
            dfs(i+1, res | nums[i]) 
            # i wont pick this
            dfs(i+1, res)

        dfs(0, 0)

        maxValue = max(list(dic.keys()))
        return dic[maxValue]
