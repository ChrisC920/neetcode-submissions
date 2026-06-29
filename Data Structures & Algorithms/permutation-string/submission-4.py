class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = [0] * 26
        count2 = [0] * 26


        for c1 in s1:
            count1[ord(c1) - ord('a')] += 1
        for c in s2:
            if c in s1:
                count2[ord(c) - ord('a')] += 1
                if count1 == count2:
                    return True
            else:
                count2 = [0] * 26
        return False 
