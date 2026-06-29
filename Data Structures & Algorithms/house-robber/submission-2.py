class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        def dp(idx):
            if idx >= len(nums):
                return 0
            memo[idx] = max(nums[idx] + dp(idx + 2), dp(idx + 1))
            return memo[idx]
        return dp(0)