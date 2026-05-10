class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sCharCounts = [0] * 26
        tCharCounts = [0] * 26

        for i in range(len(s)):
            sCharCounts[ord(s[i]) - ord('a')] += 1
            tCharCounts[ord(t[i]) - ord('a')] += 1

        for i in range(26):
            if sCharCounts[i] != tCharCounts[i]:
                return False
        
        return True