class Solution:
    def climbStairs(self, n: int) -> int:
        prev, prev2 = 1, 1

        for i in range(n - 1):
            tmp = prev
            prev += prev2
            prev2 = tmp
        return prev