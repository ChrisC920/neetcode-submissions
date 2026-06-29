class Solution:
    def isValid(self, s: str) -> bool:
        paren = {')': '(', '}': '{', ']': '['}
        stack = []
        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif stack:
                p = stack.pop()
                if paren[c] != p:
                    return False
        return True if stack == [] else False
