class Solution:
    def climbStairs(self, n: int) -> int:
        cache = {}
        def dp(i):
            if i < 0:
                return 0
            if i == 1:
                return 1
            if i == 2:
                return 2
            if i in cache:
                return cache[i]
            ret = dp(i - 1) + dp(i - 2)
            cache[i] = ret
            return ret
        return dp(n)
