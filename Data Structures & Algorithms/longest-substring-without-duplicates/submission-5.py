class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 1
        longest = 0
        seen = set()
        seen.add(s[l])

        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            r += 1
            longest = max(longest, r - l)
        return longest
