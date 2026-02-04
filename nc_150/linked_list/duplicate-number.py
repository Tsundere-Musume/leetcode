from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            n = nums[i]
            if nums[n] < 0:
                return n
            nums[n] *= -1
        return 0
        
