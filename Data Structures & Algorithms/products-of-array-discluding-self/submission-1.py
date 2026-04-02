class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1] * len(nums)
        post = [1] * len(nums)
        res = [1] * len(nums)
        pre_prod = 1
        post_prod = 1
        for i in range(len(nums)):
            if i > 0:
                pre_prod *= nums[i - 1]
                pre[i] = pre_prod
            if i < len(nums) - 1:
                post_prod *= nums[len(nums) - i - 1]
                post[len(nums) - i - 2] = post_prod

        for i in range(len(nums)):
            res[i] = pre[i] * post[i]
        return res