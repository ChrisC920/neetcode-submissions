class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in numSet:
            count = 1
            if (num - 1) in numSet:
                while (num - 1 + count) in numSet:
                    count += 1
                longest = max(longest, count)
        return longest