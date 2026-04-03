from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        freqs = defaultdict(int)
        res = 0
        maxf = 0
        for r in range(len(s)):
            freqs[s[r]] += 1
            maxf = max(maxf, freqs[s[r]])

            while (r - l + 1) - maxf > k: # number of elements that arent maxf > k
                freqs[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
