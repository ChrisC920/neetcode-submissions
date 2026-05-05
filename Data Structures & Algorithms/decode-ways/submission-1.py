class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        dp = {len(s): 1}
        
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif i < len(s) - 1 and 10 <= int(s[i:i+2]) <= 26:
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        return dp[0]