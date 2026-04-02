class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            length = len(s)
            res += str(length) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        l, r = 0, 0
        while r < len(s):
            while s[r] != '#':
                r += 1
            # r should be at index of delimitter
            length = int(s[l:r])
            l = r + 1
            r += length + 1
            res.append(s[l:r])
            l = r
        return res