class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+", "-", "*", "/"}
        for token in tokens:
            if token in operations:
                val2 = stack.pop()
                val1 = stack.pop()
                if token == "+":
                    val = val1 + val2
                elif token == "-":
                    val = val1 - val2
                elif token == "*":
                    val = val1 * val2
                elif token == "/":
                    val = val1 / val2
                    if val >= 0:
                        val = floor(val)
                    else:
                        val = ceil(val)
                print(val)
                stack.append(val)
            else:
                stack.append(int(token))
            
        return stack[0]