class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins) + 1)]
        coins.sort()
        # dp[i][j] represents # of ways to form amount j using coins from index i onward
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]
        # [0, 0, 0, 0, 0]
        
        for i in range(len(dp)):
            dp[i][0] = 1

        for i in range(len(coins) - 1, -1, -1):
            for a in range(amount + 1):
                if a >= coins[i]:
                    dp[i][a] = dp[i + 1][a] + dp[i][a - coins[i]]
        return dp[0][amount]