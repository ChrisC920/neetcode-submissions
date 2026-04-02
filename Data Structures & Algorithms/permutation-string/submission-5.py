class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        count1 = [0] * 26
        count2 = [0] * 26


        for c1 in s1:
            count1[ord(c1) - ord('a')] += 1
        for c, v in enumerate(s2):
            i = c
            while i < len(s2) and s2[i] in s1:
                count2[ord(s2[i]) - ord('a')] += 1
                if count1 == count2:
                    return True
                i += 1
            
            count2 = [0] * 26
        return False 
