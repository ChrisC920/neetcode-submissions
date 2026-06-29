class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = [0] * len(nums)
        res = 0
        def dp(idx):
            nonlocal res
            if idx >= len(nums):
                return 0
            memo[idx] = max(nums[idx] + dp(idx + 2), dp(idx + 1))
            res = max(memo[idx], res)
            return memo[idx]
        dp(0)
        return res