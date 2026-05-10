class Solution:
    def hasOverflow(self, x: int) -> bool:
        MIN_INT32 = -2**31
        MAX_INT32 = 2**31 - 1
        return x < MIN_INT32 or x > MAX_INT32

    def reverse(self, x: int) -> int:
        if self.hasOverflow(x):
            return 0

        intStr = str(x)

        isNegative = False
        if intStr[0] == '-':
            isNegative = True
            intStr = intStr[1::]

        intStr = intStr[::-1]
        
        if isNegative:
            intStr = '-' + intStr

        reversed = int(intStr)
        if self.hasOverflow(reversed):
            return 0

        return reversed