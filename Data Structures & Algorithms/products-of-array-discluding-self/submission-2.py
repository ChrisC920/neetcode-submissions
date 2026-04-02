class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            sIdx = len(nums) - 1 - i
            suffix[sIdx] = suffix[sIdx + 1] * nums[sIdx + 1]
        
        for i in range(len(suffix)):
            prefix[i] *= suffix[i]
        return prefix