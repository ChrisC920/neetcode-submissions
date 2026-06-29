class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        minProd, maxProd = 0, 0
        res = nums[0]
        for num in nums:
            maxProd = max(maxProd * num, num, minProd * num)
            minProd = min(maxProd * num, num, minProd * num)
            res = max(maxProd, res)
        return res