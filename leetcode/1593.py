# 1593. Split a String Into the Max Number of Unique Substrings
# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/description/
# TC: O(2**N)
# SC: O(2**N)
# YT: https://www.youtube.com/@eka_code

class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        # i want to max the unique split of the string
        N = len(s)

        def dfs(dic, i,j):
            if j >= N:
                if i>=N:
                    return len(dic) # return the number of sub-string i got after spliting
                else:
                    tempS = s[i:j]
                    if tempS not in dic: return len(dic) + 1
                    else: return float("-inf") # return min value that i could have

            res = 0
            tempS = s[i:j+1]
            if tempS not in dic:
                # take
                temp1 = dic.copy()
                temp1[tempS] = 1
                res = max(res, dfs(temp1, j+1, j+1))

                # not take
                temp1 = dic.copy()
                res = max(res, dfs(temp1, i, j+1))

            else:
                # not take
                temp1 = dic.copy()
                res = max(res, dfs(temp1, i, j+1))

            return res
        
        return dfs({}, 0,0)
