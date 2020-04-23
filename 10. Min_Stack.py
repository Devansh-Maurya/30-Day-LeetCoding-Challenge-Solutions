class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        self.mins = []
        

    def push(self, x: int) -> None:
        if not self.mins or x <= self.mins[-1]:
            self.mins.append(x)
        self.s.append(x)
        

    def pop(self) -> None:
        if self.mins and self.mins[-1] == self.s[-1]:
            self.mins.pop()
        self.s.pop()
        

    def top(self) -> int:
        if self.s:
            return self.s[-1]
        

    def getMin(self) -> int:
        if self.mins:
            return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
