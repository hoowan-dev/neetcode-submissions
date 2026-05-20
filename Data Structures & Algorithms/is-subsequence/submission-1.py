class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True

        currIndex = 0
        for c in t:
            if c == s[currIndex]:
                currIndex += 1 
                if currIndex == len(s):
                    return True
        return False
