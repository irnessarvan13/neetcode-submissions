class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []    # tracks min at each level

    def push(self, val: int) -> None:
        self.stack.append(val)
        # current min is either val or whatever was min before
        minVal = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)
        
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
