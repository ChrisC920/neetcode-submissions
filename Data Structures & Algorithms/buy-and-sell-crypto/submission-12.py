class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        res = 0
        for r in range(1, len(prices)):
            if prices[r] - prices[l] >= 0:
                res = max(res, prices[r] - prices[l])
            else:
                l += 1
        return res
            
