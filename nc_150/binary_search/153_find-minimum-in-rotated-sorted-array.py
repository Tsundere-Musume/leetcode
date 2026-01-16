class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1
        result = nums[0]
        while l <= r:
            m = l + (r - l) // 2
            result = min(result, nums[m])
            if nums[m] < nums[r]:
                r = m - 1
            else:
                l = m + 1
        return result
