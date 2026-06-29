class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def helper(i, prev, length):
            if i >= len(nums):
                return length
            if nums[i] > prev:
                return max(helper(i + 1, nums[i], length + 1), helper(i + 1, prev, length))
            return helper(i + 1, prev, length)
        return helper(0, float('-inf'), 0)
