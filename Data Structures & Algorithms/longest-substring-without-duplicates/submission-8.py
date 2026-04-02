class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l, r = 0, 1
        res = 1
        seen = set()
        seen.add(s[0])
        while r < len(s):
            print(f'{s[l]} {s[r]} {seen}')
            if s[r] in seen:
                res = max(res, r - l)
                while s[r] in seen:
                    seen.remove(s[l])
                    l += 1
            else:
                seen.add(s[r])
                r += 1
        return max(res, r - l)