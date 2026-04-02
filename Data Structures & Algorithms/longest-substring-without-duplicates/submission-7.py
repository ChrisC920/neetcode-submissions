class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        l, r, longest = 0, 0, 0

        while r < len(s):
            while s[r] in unique:
                unique.remove(s[l])
                l += 1
            unique.add(s[r])
            longest = max(longest, r - l + 1)
            r += 1
        return longest