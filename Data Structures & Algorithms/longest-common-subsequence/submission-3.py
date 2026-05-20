class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def helper(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]

            if text1[i] == text2[j]:
                cache[(i, j)] = helper(i + 1, j + 1) + 1
            else:
                cache[(i, j)] = max(helper(i, j + 1), helper(i + 1, j))
            return cache[(i, j)]
        return helper(0, 0)
