class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)

        res = 0
        for n in numbers:
            val = n + 1
            run = 1
            while val in numbers:
                val += 1
                run += 1
                res = max(run, res)
        return res