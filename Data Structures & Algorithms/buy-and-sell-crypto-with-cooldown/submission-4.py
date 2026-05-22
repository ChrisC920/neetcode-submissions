class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # dp[i][1] -> max profit starting at day i when we are allowed to buy
        # dp[i][0] -> max profit starting at day i when we are holding a stock (sell)
        N = len(prices)
        dp = [[0] * 2 for _ in range(N + 1)]
        
        for i in range(len(prices) - 1, -1, -1):
            # buy
            buy = dp[i + 1][0] - prices[i] if i < N - 1 else -prices[i]
            wait = dp[i + 1][1] if i < N - 1 else 0
            dp[i][1] = max(buy, wait)

            # sell
            sell = dp[i + 2][1] + prices[i] if i < N - 2 else prices[i]
            wait = dp[i + 1][0] if i < N - 1 else 0
            dp[i][0] = max(sell, wait)
        return dp[0][1]