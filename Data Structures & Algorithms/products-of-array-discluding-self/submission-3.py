class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [1] * (len(nums) + 1)
        right = [1] * (len(nums) + 1)
        # left should look like: [1, 1, 2, 8]
        # right should look like: [48, 24, 6, 1]
        for i in range(len(nums)):
            left[i + 1] = left[i] * nums[i]
            j = len(nums) - i - 1
            right[j] = right[j + 1] * nums[j]
        
        # remove last elem of left
        # remove first elem of right

        res = [0] * len(nums)
        for i in range(len(res)):
            res[i] = left[i] * right[i + 1]
        return res