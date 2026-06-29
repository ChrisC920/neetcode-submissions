class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(lst):
            if not lst:
                return 0
            if len(lst) == 1:
                return lst[0]
            memo = [0] * len(lst)
            
            memo[0] = lst[0]
            memo[1] = max(lst[0], lst[1])
            for i in range(2, len(lst)):
                memo[i] = max(lst[i] + memo[i - 2], memo[i - 1])
            return memo[-1]
        return max(helper(nums[:len(nums) - 1]), helper(nums[1:]))