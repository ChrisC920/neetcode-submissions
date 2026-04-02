class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 1,2,3,4,5,6 -
        # 6,1,2,3,4,5
        # 5,6,1,2,3,4
        # 

        # 4,5,6,1,2,3 -
        # 3,4,5,6,1,2 -
        # 2,3,4,5,6,1 -
        l, r = 0, len(nums) - 1

        while l <= r:
            c = (l + r) // 2
            if nums[c] == target:
                return c
            if nums[l] <= nums[c]:
                if target < nums[l] or target > nums[c]:
                    l = c + 1
                else:
                    r = c - 1
            else:
                if target > nums[r] or target < nums[c]:
                    r = c - 1
                else:
                    l = c + 1
        return -1