class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        for r in range(1, len(nums)):
            print(str(l) + " " + str(r))
            if nums[r] == nums[l]:
                if abs(r - l) <= k:
                    return True
                r = l + 1
        return False