# 2707. Extra Characters in a String
# https://leetcode.com/problems/extra-characters-in-a-string/description/
# TC : (2**N)
# SC : (N**2)

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # s = "leetscode"
        # dictionary = ["leet","code","leetcode"]
        dp = {}
        dic = set([i for i in dictionary])
        N = len(s)
        def dfs(i,j):
            # need a break case
            if (i,j) in dic: return dp[(i,j)]
            if j==N:
                if s[i:j] in dic:
                    return 0
                else:
                    return j-i
                
            curSubStr = s[i:j+1]
            tempRes = float("inf")
            # either we inc the j so that we could find the s[i:j]
            tempRes = min(tempRes, dfs(i, j+1))
            # or make the free str from j-i and i==j = j+1
            if curSubStr in dic:
                tempRes = min(tempRes, dfs(j+1, j+1))
            else:
                tempRes = min(tempRes, dfs(j+1, j+1) + j-i+1)
            
            dp[(i,j)] = tempRes
            return tempRes

        return dfs(0,0)
