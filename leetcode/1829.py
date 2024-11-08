# 1829. Maximum XOR for Each Query
# https://leetcode.com/problems/maximum-xor-for-each-query/description/
# TC: O(N)
# SC: O(N)
# YT: https://www.youtube.com/@eka_code

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        N = len(nums)
        prefixEor = [0]*N
        res = []

        for i in range(N):
            prefixEor[i] = nums[i] ^ (0 if i==0 else prefixEor[i-1])

        for i in range(N):
            temp = prefixEor[N-1-i]
            tempRes = 0
            i = 0
            while i<maximumBit:
                if (temp>>i)&1==0:
                    tempRes |= 1<<i
                i += 1
            res.append(tempRes)
        
        return res



            
