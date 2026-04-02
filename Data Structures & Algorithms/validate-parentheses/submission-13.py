class Solution:
    def isValid(self, s: str) -> bool:
        parens = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if c not in parens:
                stack.append(c)
            else:
                if stack and parens[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False