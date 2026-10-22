class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        stack = []
        for el in asteroids: 
            if el >= 0:
                stack.append(el)
            else:
                while True:
                    if stack and stack[-1] > 0:
                        if stack[-1] < abs(el):
                            stack.pop()
                        elif stack[-1] == abs(el):
                            stack.pop()
                            break
                        else:
                            break
                    else:
                        stack.append(el)
                        break
        return stack
