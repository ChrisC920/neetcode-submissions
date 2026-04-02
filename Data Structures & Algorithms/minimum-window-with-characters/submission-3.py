from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT = defaultdict(int)

        for i in range(len(t)):
            countT[t[i]] += 1
        
        l = 0
        res = ""
        resLength = float('inf')
        window = defaultdict(int)
        have, need = 0, len(countT)
        for r in range(len(s)):
            window[s[r]] += 1
            if countT[s[r]] > 0 and window[s[r]] == countT[s[r]]:
                have += 1
            
            while have == need:
                if r - l + 1 < resLength:
                    res = s[l:r + 1]
                    resLength = r - l + 1
                window[s[l]] -= 1
                if countT[s[l]] > 0 and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
        return res

            