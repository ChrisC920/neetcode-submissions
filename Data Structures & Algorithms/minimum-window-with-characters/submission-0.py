class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        charsT = defaultdict(int)
        charsS = defaultdict(int)

        for i in range(len(t)):
            charsT[t[i]] += 1
        print(charsT)

        l, r = 0, 0
        res = ""
        while r < len(s):
            if s[r] in charsT:
                print(s[r])
                charsS[s[r]] += 1
                while charsS[s[r]] > charsT[s[r]]:
                    if s[l] == s[r]:
                        charsS[s[l]] -= 1
                        l += 1
                        break
                    l += 1
            if charsS == charsT:
                print(s[l:r+1])
                while s[l] not in charsT:
                    l += 1
                res = s[l:r+1] if len(s[l:r+1]) < len(res) or res == "" else res
                charsS[s[l]] -= 1
                print(charsS)
                l += 1
            r += 1
        return res



            