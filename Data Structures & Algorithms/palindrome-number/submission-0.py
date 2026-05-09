class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True
        elif x < 0:
            return False
        
        normalStr = str(x)
        reverseStr = normalStr[::-1]
        
        return normalStr == reverseStr