class Solution:
    def search(self, nums: List[int], target: int) -> int:
        res = -1
        l, r = 0, len(nums) - 1
        if target == nums[0]:
            return 0
        while l < r:
            c = (l + r) // 2
            if target == nums[l]:
                return l
            if target == nums[c]:
                return c
            
            if target < nums[l]:
                l = c + 1
            else:
                r = c
        return -1