class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res = res + '&' + str(len(s)) + '&' + s
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            i += 1
            strL = s[i]
            i += 1
            while s[i] != '&':
                strL += s[i]
                i += 1
            intL = int(strL)
            i += 1
            word = ''
            while intL > 0:
                word += s[i]
                i += 1
                intL -= 1
            res.append(word)
            print(res)
        return res