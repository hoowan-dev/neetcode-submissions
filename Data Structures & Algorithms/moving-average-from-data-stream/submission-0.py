class MovingAverage:

    def __init__(self, size: int):
        self.window = [0] * size
        self.index = 0
        self.windowSum = 0
        self.slotsUsed = 0

    def next(self, val: int) -> float:
        self.windowSum -= self.window[self.index]
        self.window[self.index] = val
        self.windowSum += val

        self.index += 1
        if self.index >= len(self.window):
            self.index = 0

        if self.slotsUsed < len(self.window):
            self.slotsUsed += 1

        return self.windowSum / self.slotsUsed
            
# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
