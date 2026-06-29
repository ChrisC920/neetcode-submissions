class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1,2,3,4,5,6 - target = l < c < r - left //
        # 6,1,2,3,4,5 - target < c < r < l - left
        # 5,6,1,2,3,4 - target = c < r < l - center //
        # 4,5,6,1,2,3 - target < r < l < c - right
        # 3,4,5,6,1,2 - target < r < l < c - right
        # 2,3,4,5,6,1 - target = r < l < c - right // 
        res = -1
        l, r = 0, len(nums) - 1
        if target == nums[0]:
            return 0
        while l <= r:
            c = (l + r) // 2
            print(c)
            if target == nums[l]:
                return l
            if target == nums[c]:
                return c
            if target == nums[r]:
                return r
            
            if nums[c] > nums[r]:
                l = c + 1
            else:
                r = c - 1
        return -1