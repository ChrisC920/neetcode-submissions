class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        dictionary = set(wordDict)
        memo = {len(s): True}

        def helper(start):
            if start in memo:
                return memo[start]

            for i in range(start, N):
                if s[start:i + 1] in dictionary:
                    if helper(i + 1):
                        memo[i] = True
                        return True
            memo[start] = False
            return False
        return helper(0)
                