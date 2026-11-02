class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()]).lower()
        print(s)

        if len(s) == 1:
            return True
        
        if len(s) == 2:
            return s[0] == s[1]

        i = 0
        j = len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True