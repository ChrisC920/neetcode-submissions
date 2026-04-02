class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = [0] * 26
        count_s2 = [0] * 26
        for c in s1:
            count_s1[ord(c) - ord('a')] += 1

        r = 0
        for l in range(len(s2)):
            r = l
            while r < len(s2) and s2[r] in s1 and r - l + 1 <= len(s1):
                count_s2[ord(s2[r]) - ord('a')] += 1
                if count_s1 == count_s2:
                    return True
                r += 1
            count_s2 = [0] * 26
        return False