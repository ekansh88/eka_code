3264. Final Array State After K Multiplication Operations I
https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-i
TC: O(K*logN + NlogN)
SC: O(N)
YT: https://www.youtube.com/@eka_code

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        N = len(nums)
        heap = [[nums[i], i] for i in range(N)]
        heapq.heapify(heap)

        while k:
            val, idx = heapq.heappop(heap)
            val *= multiplier
            heapq.heappush(heap, [val,idx])

            k -= 1
        
        while heap:
            val, idx = heapq.heappop(heap)
            nums[idx] = val

        return nums
