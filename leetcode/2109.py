# 2109. Adding Spaces to a String
# https://leetcode.com/problems/adding-spaces-to-a-string/
# TC: O(N)
# SC: O(N)
# YT: https://www.youtube.com/@eka_code

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        # s = "spacing", spaces = [0,1,2,3,4,5,6]
        # in this we are using 2 pointer, one over spaces array and other over the s string
        
        idxSpace = 0
        idxS = 0
        N = len(s)
        res = ""
        while idxS<N:
            if idxS==spaces[idxSpace]:
                res += " "
                idxSpace += 1
            res += s[idxS]
            idxS += 1            

        return res
