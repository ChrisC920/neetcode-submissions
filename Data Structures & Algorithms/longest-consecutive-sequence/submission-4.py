class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)

        res = 0
        seen = set()
        for n in numbers:
            if n in seen:
                continue
            seen.add(n)
            val = n + 1
            run = 1
            while val in numbers and val not in seen:
                val += 1
                run += 1
                res = max(run, res)
        return res