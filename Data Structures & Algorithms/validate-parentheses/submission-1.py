class Solution:
    def isValid(self, s: str) -> bool:
        paren = []
        for c in s:
            if c != ')' and c != '}' and c != ']':
                paren.append(c)
            else:
                last_char = paren.pop()
                if c == ')' and last_char != '(':
                    return False
                if c == '}' and last_char != '{':
                    return False
                if c == ']' and last_char != '[':
                    return False
        return True