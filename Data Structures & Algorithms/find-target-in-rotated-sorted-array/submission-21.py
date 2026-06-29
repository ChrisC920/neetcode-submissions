class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        if len(nums) == 2:
            if target == nums[0]:
                return 0
            if target == nums[1]:
                return 1
            return -1
        while l < r:
            m = (r + l) // 2
            print(nums[m])
            if nums[m] < target:
                if nums[r] < target:
                    r = m
                else:
                    l = m + 1
            elif nums[m] > target:
                if nums[l] > target:
                    l = m + 1
                else:
                    r = m
            else:
                return m
        return -1