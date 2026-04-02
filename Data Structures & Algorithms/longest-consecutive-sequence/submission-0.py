class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        max_count = 0

        for n in numSet:
            if n - 1 not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                max_count = max(length, max_count)
        return max_count