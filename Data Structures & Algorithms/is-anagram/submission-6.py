class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_dict = {}
        t_dict = {}
        for sc in s:
            s_dict[sc] = s_dict.get(sc, 0) + 1
        for tc in t:
            t_dict[tc] = t_dict.get(tc, 0) + 1

        return t_dict == s_dict
            