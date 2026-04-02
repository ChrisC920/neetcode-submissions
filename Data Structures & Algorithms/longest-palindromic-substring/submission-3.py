class Solution:
    def longestPalindrome(self, s: str) -> str:
        resStart = 0
        resEnd = 0
        resLength = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLength:
                    resStart = l
                    resEnd = r
                    resLength = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > resLength:
                    resStart = l
                    resEnd = r
                    resLength = r - l + 1
                l -= 1
                r += 1
        return s[resStart:resEnd + 1]