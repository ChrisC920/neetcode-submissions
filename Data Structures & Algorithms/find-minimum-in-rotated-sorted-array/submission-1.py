class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1,2,3,4,5,6 - l < c < r - left
        # 6,1,2,3,4,5 - c < r < l - left
        # 5,6,1,2,3,4 - c < r < l - center
        # 4,5,6,1,2,3 - l < r < c - right
        # 3,4,5,6,1,2 - r < l < c - right
        # 2,3,4,5,6,1 - r < l < c - right
        res = nums[0]
        l, r = 0, len(nums) - 1
        while l < r:
            c = (l + r) // 2
            res = min(res, nums[c], nums[l], nums[r])
            if nums[r] < nums[c]:
                l = c + 1
            else:
                r = c 
        return res