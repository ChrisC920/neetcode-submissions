class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res_set = set()
        visited_set = set()
        l, r = 0, len(nums) - 1
        while l < r:
            target_val = -1*(nums[l]+nums[r])
            if target_val in visited_set:
                res_set.add((nums[l], nums[r], target_val))
            if l < target_val:
                visited_set.add(nums[l])
                l += 1
            else:
                visited_set.add(nums[r])
                r -= 1
        return list(map(list, res_set))
            
