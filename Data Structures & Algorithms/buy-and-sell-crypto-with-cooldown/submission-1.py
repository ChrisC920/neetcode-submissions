class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        def helper(i, canBuy):
            if i >= len(prices):
                return 0

            skip = helper(i + 1, canBuy)
            if canBuy:
                buy = helper(i + 1, False) - prices[i]
                return max(buy, skip)
            else:
                sell = helper(i + 2, True) + prices[i]
                return max(sell, skip)
        return helper(0, True)