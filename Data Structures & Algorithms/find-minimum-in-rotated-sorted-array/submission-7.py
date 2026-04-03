class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        res = float('inf')

        while l < r:
            m = (l + r) // 2
            if nums[r] <= nums[m]:
                l = m + 1
            else:
                r = m
        return nums[l]