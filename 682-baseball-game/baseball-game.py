class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []
        for el in operations:
            temp = 0
            if (el.isdigit() or (el.lstrip("-").isdigit() and el not in ("","-"))):
                stack.append(int(el))
            elif (el == "+"):
                temp += stack[-1] + stack[-2]
                stack.append(temp)
            elif (el == "D"):
                temp += 2 * stack[-1]
                stack.append(temp)
            elif (el == "C"):
                stack.pop()
        return sum(stack) 

