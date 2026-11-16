class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        
        l, r = 0, 1
        chars = { s[l] }
        sol = 1

        while r < len(s):
            charToAdd = s[r]
            while charToAdd in chars:
                chars.remove(s[l])
                l += 1
            chars.add(charToAdd)
            
            sol = max(sol, len(chars))
            r += 1 

        return sol