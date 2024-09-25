# 2416. Sum of Prefix Scores of Strings
# https://leetcode.com/problems/sum-of-prefix-scores-of-strings/description/
# TC : O(N*M) *N = number of words *M = length of a word
# SC : O(N*M) 

class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.isWord = False
        self.dic = {}
        self.numberOfPrefix = 0

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def getHead(self):
        temp = self.head
        return temp
    
    def addWord(self, str):
        temp = self.head

        for i in str:
            if i not in temp.dic:
                temp.dic[i] = TrieNode(i)
            temp = temp.dic[i]
        
        temp.isWord += 1
    
    def findWord(self, str):
        temp = self.head

        for i in str:
            if i not in temp.dic: return False
            temp = temp.dic[i]
        
        return temp.isWord if temp.isWord else False
    
    def findPrefix(self, str):
        temp = self.head
        
        res = 0
        for i in str:
            temp = temp.dic[i]
            res += temp.numberOfPrefix
        
        return res
    
    def _calcPrefix(self):
        temp = self.head

        def dfs(node):
            if not node: return 0
            res = node.isWord

            for i in node.dic:
                res += dfs(node.dic[i])

            node.numberOfPrefix = res
            return res
        
        dfs(temp)



class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        # create a trie according to the concept
        # then simple iterate over the trie
        # add sum the value of green node at every node

        trie = Trie()
        for i in words:
            trie.addWord(i)
        
        print(trie.findWord("eoorlyfche"))
        trie._calcPrefix()
        
        res = []

        for i in words:
            res.append(trie.findPrefix(i))
        

        return res
