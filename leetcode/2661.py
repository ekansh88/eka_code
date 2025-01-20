# 2661. First Completely Painted Row or Column
# https://leetcode.com/problems/first-completely-painted-row-or-column/description/
# TC: O(N*M)
# SC: O(N+M)
# YT: https://www.youtube.com/@eka_code 

class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        N, M = len(mat), len(mat[0])
        row, column = [0]*N, [0]*M

        dic = {}
        for i in range(N):
            for j in range(M):
                dic[mat[i][j]] = [i, j]
        
        for i in range(len(arr)):
            val = arr[i]
            r,c = dic[val]

            row[r] += 1
            column[c] += 1

            if row[r]==M or column[c]==N:
                return i
        
        return -1
