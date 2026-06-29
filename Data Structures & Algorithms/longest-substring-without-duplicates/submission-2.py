class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return 0
        unique = set()
        longest = 1
        l, r = 0, 1
        length = 1
        unique.add(s[l])
        while r < len(s):
            if s[l] == s[r] or s[r] in unique:
                unique.clear()
                l = r
                unique.add(s[l])
                longest = max(longest, length)
                length = 1
            else:
                length += 1
            unique.add(s[r])
            r += 1
        return max(longest, length)