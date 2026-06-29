class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        if len(s1) >= len(s2):
            return False

        freqs1, freqs2 = [0] * 26, [0] * 26
        for c1 in s1:
            freqs1[ord(c1) - ord('a')] += 1
        
        l = 0
        for r in range(len(s2)):
            freqs2[ord(s2[r]) - ord('a')] += 1
            if freqs1[ord(s2[r]) - ord('a')] > 0:
                if freqs2 == freqs1:
                    return True
            else:
                freqs2[ord(s2[l]) - ord('a')] -= 1
                l += 1
        print(freqs1)
        print(freqs2)
        return freqs2 == freqs1
