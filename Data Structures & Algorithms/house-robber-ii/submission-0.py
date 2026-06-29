class Solution:
    def rob(self, nums: List[int]) -> int:
        start = nums.index(max(nums))
        memo = [0] * len(nums)
        memo[0] = nums[start]
        i = start + 1 if start + 1 < len(nums) else 0
        memo[1] = max(nums[start], nums[i])
        i = i + 1 if i + 1 < len(nums) else 0
        for j in range(2, len(nums)):
            memo[j] = max(nums[i] + memo[j - 2], memo[j - 1])
            i += 1
            if i >= len(nums):
                i = 0
        return memo[-1]