class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        seen = {}

        while r < len(nums):
            if nums[r] in seen:
                if abs(seen[nums[r]] - r) <= k:
                    return True
                l += 1
            seen[nums[r]] = r
            r += 1
        return False