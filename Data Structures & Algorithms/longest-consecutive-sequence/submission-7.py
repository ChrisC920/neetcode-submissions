class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        numbers = set(nums)

        res = 1
        for n in numbers:
            val = n + 1
            run = 1
            while val in numbers:
                val += 1
                run += 1
                res = max(run, res)
        return res