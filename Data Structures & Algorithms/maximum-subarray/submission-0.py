class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        currSum = nums[0]

        for num in nums[1:]:
            currSum = max(currSum + num, num)
            res = max(res, currSum)
        return res