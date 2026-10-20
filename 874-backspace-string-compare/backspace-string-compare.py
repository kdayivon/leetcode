class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def compute(string):
            stack = []
            for char in string:
                if char.isalnum():
                    stack.append(char)
                else:
                    if (stack):
                        stack.pop()
            return "".join(stack)
        return compute(s) == compute(t) 
