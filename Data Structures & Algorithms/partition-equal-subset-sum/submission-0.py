class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        targetSum = total // 2
        
        def helper(i, tot):
            if tot == targetSum:
                return True
            if i >= len(nums):
                return False
            
            return helper(i + 1, tot) or helper(i + 1, tot + nums[i])
        return helper(0, 0)