class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r + l) // 2
            if target == nums[m]:
                return m
            if nums[m] < target:
                if nums[r] < target:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[m] > target:
                if nums[l] > target:
                    l = m + 1
                else:
                    r = m - 1
        return -1