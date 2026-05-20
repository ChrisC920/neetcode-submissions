class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        targetSum = total // 2
        memo = [[False] * (targetSum + 1) for _ in range(len(nums) + 1)]
        for i in range(len(nums) + 1):
            memo[i][0] = True
        
        for i in range(1, len(nums) + 1):
            for j in range(1, targetSum + 1):
                if nums[i - 1] <= j:
                    memo[i][j] = memo[i - 1][j] or memo[i - 1][j - nums[i - 1]]
                else:
                    memo[i][j] = memo[i - 1][j]
        return memo[len(nums)][targetSum]