class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def helper(i, canBuy):
            if i >= len(prices):
                return 0
            if (i, canBuy) in memo:
                return memo[(i, canBuy)]

            skip = helper(i + 1, canBuy)
            if canBuy:
                buy = helper(i + 1, False) - prices[i]
                memo[(i, canBuy)] = max(buy, skip)
            else:
                sell = helper(i + 2, True) + prices[i]
                memo[(i, canBuy)] = max(sell, skip)
            return memo[(i, canBuy)]
        return helper(0, True)