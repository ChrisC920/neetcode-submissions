class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dictionary = set(wordDict)

        def helper(start):
            if start >= N:
                return True
            for i in range(start, N):
                if s[start:i + 1] in dictionary:
                    if helper(i + 1):
                        return True
            return False
        return helper(0)
                