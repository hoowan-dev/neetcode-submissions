class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        string_len = len(s)
        if string_len == 0:
            return 0

        longestSubstring = 1
        presentChars = { s[0] }

        l = 0
        r = 1

        # {} = zxy
        #  l r
        # zxyzxyz
        while r < string_len:
            while s[r] in presentChars:
                presentChars.remove(s[l])
                l += 1

            presentChars.add(s[r])
            r += 1
            
            longestSubstring = max(longestSubstring, len(presentChars))

        return longestSubstring