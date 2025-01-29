# 684. Redundant Connection
# https://leetcode.com/problems/redundant-connection/description/
# TC: O(N)
# SC: O(2N)
# YT: https://www.youtube.com/@eka_code 


class UnionFind:
    def __init__(self, N):
        self.rank = [0 for _ in range(N+1)]
        self.parent = [i for i in range(N+1)]
        self.size = N
    
    def findParent(self,node):
        if self.parent[node] == node: return node
        
        self.parent[node] = self.findParent(self.parent[node])
        return self.parent[node]
    
    def unionNodes(self, node1, node2):
        parent1 = self.findParent(node1)
        parent2 = self.findParent(node2)
        rank1 = self.rank[parent1]
        rank2 = self.rank[parent2]
        
        if rank1 > rank2:
            self.parent[parent2] = parent1
        elif rank1 < rank2:
            self.parent[parent1] = parent2
        else:
            self.parent[parent2] = parent1
            self.rank[parent1] += 1
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        numberOfEdges = 0
        for i,j in edges:
            numberOfEdges = max(numberOfEdges, i, j)
        
        unionFind = UnionFind(numberOfEdges)

        for i,j in edges:
            parent1 = unionFind.findParent(i)
            parent2 = unionFind.findParent(j)

            if parent1 == parent2: return [i,j]
            else:
                unionFind.unionNodes(i,j)
        
        return []
