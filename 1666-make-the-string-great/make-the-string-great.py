class Solution:
    def makeGood(self, s: str) -> str:
        if (len(s) < 2):
            return s
        stack = []
        for char in s:
            if char.isupper() and stack:
                if (stack[-1].isupper()):
                    stack.append(char)
                else:
                    if stack[-1].upper() == char:   
                        stack.pop()
                    else:
                        stack.append(char)
            elif char.islower() and stack:
                if (stack[-1].islower()):
                    stack.append(char)
                else:
                    if stack[-1].lower() == char:   
                        stack.pop()
                    else:
                        stack.append(char)
            else: 
                stack.append(char)
                
        return "".join(stack)
