class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # handle empty string
        if len(s) == 0:
            return 0

        # keep track of present chars in substring and the longest running substring
        presentChars = { s[0] }
        longestSubstring = 1

        # keep track of sliding window
        l = 0
        r = 1

        while r < len(s):
            # if we find duplicate, slide left window until we have all unique chars again
            while s[r] in presentChars:
                presentChars.remove(s[l])
                l += 1

            # add current and slide right window
            presentChars.add(s[r])
            r += 1

            # update longest substring
            longestSubstring = max(longestSubstring, len(presentChars))

        return longestSubstring