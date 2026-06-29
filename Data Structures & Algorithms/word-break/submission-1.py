class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dictionary = set(wordDict)

        def helper(start):
            if start >= N:
                return True
            substr = ""
            valid = False
            for i in range(start, N):
                substr += s[i]
                if substr in dictionary:
                    valid = helper(i + 1)
            return valid
        return helper(0)
                