class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanedStr = ""

        for c in s:
            if c.isalpha() == False and c.isnumeric() == False:
                continue
            cleanedStr += c.lower()

        p = int(len(cleanedStr) / 2)
        for l in range(0, p):
            r = len(cleanedStr) - 1 - l

            lValue = cleanedStr[l]
            rValue = cleanedStr[r]

            if lValue != rValue:
                return False
        
        return True
            