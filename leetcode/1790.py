# 1790. Check if One String Swap Can Make Strings Equal
# TC: O(N)
# SC: O(N)
# YT: https://www.youtube.com/@eka_code 


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        # if the length of the string is diff then we cant make them same by swapping
        if len1!=len2: return False

        # this flag is use to check if the char in each string are same or not
        flag = True
        # number of diff char location over the strings
        diff = 0
        # count of each char form both string
        dic = {}

        for i in range(len1):
            # inc the count if we find a diff
            if s1[i] != s2[i]:
                diff += 1
            # +1 the count for the s1 char
            dic[s1[i]] = dic[s1[i]] + 1 if s1[i] in dic else 1
            # -1 the count for the s2 char
            dic[s2[i]] = dic[s2[i]] - 1 if s2[i] in dic else -1
        
        # checking if all the char are zero or not, 
        # if not it means that few char are diff in both string
        for i in dic:
            if dic[i]: flag = False

        # either no diff or diff is 2 so that we could swap them
        if (diff==0 or diff==2) and flag: return True
        return False
