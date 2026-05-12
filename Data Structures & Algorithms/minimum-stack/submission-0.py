class MinStack:

    def __init__(self):
        self.topIndex = -1
        self.storage = [0] * 10

    def push(self, val: int) -> None:
        if self.topIndex == len(self.storage) - 1:
            self.storage *= 2

        self.topIndex += 1
        self.storage[self.topIndex] = val

    def pop(self) -> None:
        if self.topIndex >= 0:
            self.topIndex -= 1

    def top(self) -> int:
        if self.topIndex >= 0:
            return self.storage[self.topIndex]
        return -1

    def getMin(self) -> int:
        min = 2**31 - 1
        for i in range(self.topIndex + 1):
            val = self.storage[i]
            if val < min:
                min = val
        return min

