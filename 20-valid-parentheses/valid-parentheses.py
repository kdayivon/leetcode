class Solution:
    def isValid(self, s: str) -> bool:
        brackets:dict = {"}":"{", "]":"[", ")":"("}
        stack:list = []
        for char in s:
            if (char in "{(["):
                stack.append(char)
            else:
                if (not stack): 
                    return False
                if (stack.pop() != brackets[char]):
                    return False
                
        return not stack  
