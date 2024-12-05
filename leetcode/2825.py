# 2825. Make String a Subsequence Using Cyclic Increments
# https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments/description/
# TC: O(N+M) *N=len(str1),M=len(str2)
# SC: O(1)
# YT: https://www.youtube.com/@eka_code 

# 2 Pointer Method
class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        # str1 = "ab", str2 = "d"
        idx1, idx2 = 0, 0
        len1, len2 = len(str1), len(str2)
        steps = 0

        while idx1<len1 and idx2<len2:
            if str1[idx1]==str2[idx2]:
                idx1 += 1
                idx2 += 1
            elif (ord(str1[idx1])+1==ord(str2[idx2])) or (str1[idx1]=="z" and str2[idx2]=="a"):
                steps += 1
                idx1 += 1
                idx2 += 1
            else:
                idx1 += 1
        
        if idx2>=len2: return True
        return False
        
