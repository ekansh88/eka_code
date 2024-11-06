# 3011. Find if Array Can Be Sorted
# https://leetcode.com/problems/find-if-array-can-be-sorted/description/
# TC: O(N)
# SC: O(N)
# YT: https://www.youtube.com/@eka_code

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        # what is the last max value of the sorted section of a nums with a particular ones in bit
        lastMaxSortedNumb = -1

        # how many ones a number hold for all the nums values
        numToBit = {}
        for i in nums:
            ones = 0
            temp = i
            while temp:
                ones += temp&1
                temp >>= 1
            numToBit[i] = ones
        
        # iteration
        index = 0
        while index < N:
            # starting a new section of a nums that is not sorted, and before that all are sorted
            val = nums[index]
            # this val bit ones
            valBitOnes = numToBit[val]
            # max and min value of this particular range
            minVal, maxVal = val, val
            # iteration till we have same ones in the iteration
            while index < N and valBitOnes == numToBit[nums[index]]:
                minVal, maxVal = min(minVal, nums[index]), max(maxVal, nums[index])
                index += 1

            if lastMaxSortedNumb < minVal:
                lastMaxSortedNumb = maxVal
            else:
                return False
        
        return True
