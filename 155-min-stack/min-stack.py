class MinStack:

    def __init__(self):
        self.w = []
        self.w_min = []
        self.min = float("inf")

    def push(self, value: int) -> None:
        self.w.append(value)
        if not self.w_min:
            self.w_min.append(value)
        else:
            self.w_min.append(min(self.w_min[-1], value))

    def pop(self) -> None:
        if not self.w:
            return
        self.w.pop()
        self.w_min.pop()

    def top(self) -> int:
        return self.w[-1]

    def getMin(self) -> int:
        return self.w_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()