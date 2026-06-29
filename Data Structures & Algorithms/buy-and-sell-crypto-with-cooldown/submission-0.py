class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        def helper(i, profit, canBuy):
            if i >= len(prices):
                return profit
            
            if canBuy:
                return max(helper(i + 1, profit - prices[i], False), helper(i + 1, profit, True))
            else:
                return max(helper(i + 2, profit + prices[i], True), helper(i + 1, profit, False))
        return helper(0, 0, True)