# 2070. Most Beautiful Item for Each Query
# https://leetcode.com/problems/most-beautiful-item-for-each-query/description/
# TC: O(NlogN)
# SC: O(N)
# YT: https://www.youtube.com/@eka_code

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
      
      # make the pair with price to its max beauty
        dic = {}
        for p,b in items:
            if p in dic:
                dic[p] = max(dic[p], b)
            else:
                dic[p] = b
        
      # get all the unique keys and sort them
        keys = list(dic.keys())
        keys.sort()

      # manipulate the hashmap with the maxValue from the previousKey to the currentKey [kindly like a prefix max array]
        tempMax = dic[keys[0]]
        for i in range(1, len(keys)):
            dic[keys[i]] = max(dic[keys[i]], tempMax)
            tempMax = dic[keys[i]]

      # for every query i use the binary search and find the value of the key from the hashMap
        res = []
        for i in queries:
            index = bisect.bisect_left(keys, i)
            if index==0 and keys[index] > i:
                res.append(0)
            elif index>=len(keys):
                index = len(keys)-1
                res.append(dic[keys[index]])
            elif keys[index] > i:
                index -= 1
                res.append(dic[keys[index]])
            else:
                res.append(dic[keys[index]])

      # return the result aray
        return res
