class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        cache = {}

        def helper(i, currSum):
            if i == len(nums):
                return 1 if currSum == target else 0
            if i in cache:
                return cache[i]
            ret = helper(i + 1, currSum + nums[i]) + helper(i + 1, currSum - nums[i])
            cache[i] = ret
            return ret
        return helper(0, 0)