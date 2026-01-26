from typing import List
import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k > len(nums):
            return []

        h = []
        for i in range(k):
            heapq.heappush(h, (-nums[i], i))
        result = []
        result.append(-h[0][0])
        l = 1
        for r in range(k, len(nums)):
            heapq.heappush(h, (-nums[r], r))
            while h[0][1] < l:
                heapq.heappop(h)

            elem, _ = h[0]
            result.append(-elem)
            l += 1

        return result


        
