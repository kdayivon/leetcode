class MyQueue:

    def __init__(self):
        self.w = []
        self.r = []
        self.len = 0

    def push(self, x: int) -> None: # enqueue
        self.w.append(x)
        self.len += 1

    def pop(self) -> int:   # dequeue
        if not self.r:
            while self.w:
                self.r.append(self.w.pop())
        self.len -= 1
        return self.r.pop()

    def peek(self) -> int:
        if not self.r:
            while self.w:
                self.r.append(self.w.pop())
        return self.r[-1]

    def empty(self) -> bool:
        return self.len == 0



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()