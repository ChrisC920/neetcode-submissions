class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd, maxProd = 0, 0
        res = nums[0]
        for num in nums:
            maxProd = max(maxProd * num, num, minProd * num)
            minProd = min(maxProd * num, num, minProd * num)
            res = max(maxProd, res)
        return res