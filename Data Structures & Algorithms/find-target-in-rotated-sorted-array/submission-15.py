class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # [6,1,2,3,4,5] target=6
        if len(nums) == 1:
            return 0 if target == nums[0] else -1
        while l < r:
            m = (r + l) // 2

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