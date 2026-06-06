class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = dict()
        for c in magazine:
            if c not in letters:
                letters[c] = 1
            else:
                letters[c] += 1

        for c in ransomNote:
            if c not in letters or letters[c] == 0:
                return False

            letters[c] -= 1

        return True
