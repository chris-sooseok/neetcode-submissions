class MinStack:

    def __init__(self):
        self.min = float('inf')
        self.stack = []
        
    def push(self, val: int) -> None:
        if val < self.min:
            self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.min = min(self.stack)
        else:
            self.min = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min
