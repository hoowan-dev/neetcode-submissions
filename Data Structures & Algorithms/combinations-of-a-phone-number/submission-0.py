class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        LETTER_LOOKUP = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        solution = []

        def getCombinations(currStr = "", nextIndex = 0):
            if nextIndex == len(digits):
                solution.append(currStr)
                return

            nextDigit = int(digits[nextIndex])
            nextLetters = LETTER_LOOKUP[nextDigit]

            for c in nextLetters:
                getCombinations(currStr + c, nextIndex + 1)
        
        getCombinations()

        return solution