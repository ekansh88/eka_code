# 773. Sliding Puzzle
# https://leetcode.com/problems/sliding-puzzle/description/
# TC: O(720)
# SC: O(720)

class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        # Input: board = [[4,1,2],[5,0,3]]
        # Output: 5

        queue = []
        dirs = [1,0,-1,0,1]
        visit = set([])
        res = "123450"
        
        i,j = 0, 0
        for i in range(2):
            for j in range(3):
                if board[i][j]==0:
                    queue.append([board[:],[i,j]])
                    break
        steps = 0

        while queue:
            lens = len(queue)
            while lens:
                lens -= 1

                nums, [r, c] = queue[0]
                queue.pop(0)

                strIs = ""
                for i in nums:
                    for j in i:
                        strIs += f"{j}"

                if strIs in visit: continue
                elif strIs==res:
                    return steps
                visit.add(strIs)

                for i in range(4):
                    dr,dc = r+dirs[i], c+dirs[i+1]
                    if min(dr,dc)<0 or dr>=2 or dc>=3: continue

                    nums[r][c], nums[dr][dc] = nums[dr][dc], nums[r][c]
                    temp = []
                    for i in nums:
                        temp.append([j for j in i])

                    queue.append([temp, [dr,dc]])

                    nums[r][c], nums[dr][dc] = nums[dr][dc], nums[r][c]

            
            steps += 1
            
        return -1
