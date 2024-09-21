# 386. Lexicographical Numbers
# https://leetcode.com/problems/lexicographical-numbers/description/
# TC: O(N)
# SC: O(1)

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        val = 1
        for _ in range(1,n+1):
            res.append(val)
            
            if val*10<=n:
                val *= 10
            else:
                # if val == 19 then 19%10==9 so val=1 then val+=1 it will be 2
                while val%10==9 or val>=n:
                    val //= 10
                val += 1
        
        return res