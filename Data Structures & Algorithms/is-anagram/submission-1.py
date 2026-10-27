class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sChars = {}
        tChars = {}

        for c in s:
            if c in sChars:
                sChars[c] += 1
            else:
                sChars[c] = 1

        for c in t:
            if c in tChars:
                tChars[c] += 1
            else:
                tChars[c] = 1

        if len(sChars.keys()) != len(tChars.keys()):
            return False

        for c in sChars.keys():
            if c not in tChars or sChars[c] != tChars[c]:
                return False

        return True