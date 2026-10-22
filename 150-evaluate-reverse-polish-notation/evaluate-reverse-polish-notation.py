class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        val, val2 = 0, 0
        for el in tokens:
            temp = 0
            if el.isdigit() or (el.lstrip("-").isdigit() and el not in ("", "-")):
                stack.append(int(el))
            elif el == "+":
                val = stack.pop()
                val2 = stack.pop()
                temp = val2 + val
                stack.append(temp)
            elif el == "-":
                val = stack.pop()
                val2 = stack.pop()
                temp = val2 - val
                stack.append(temp)
            elif el == "*":
                val = stack.pop()
                val2 = stack.pop()
                temp = val2 * val
                stack.append(temp)
            elif el == "/":
                val = stack.pop()
                val2 = stack.pop()
                temp = int(val2 / val)
                stack.append(temp)
                
        return stack[0] 
