from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()
        l = 0
        for r, num in enumerate(nums):
            while window and nums[window[-1]] <= nums[r]:
                window.pop()
            window.append(r)

            if l > window[0]:
                window.popleft()

            if (r + 1) >= k:
                result.append(nums[window[0]])
                l += 1
        return result

