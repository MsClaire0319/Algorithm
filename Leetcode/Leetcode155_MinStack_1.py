class MinStack():

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if self.min_stack and self.min_stack[-1] <= x:
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(x)

    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.min_stack = self.min_stack[:-1]

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

