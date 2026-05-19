class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solution = []

        def rec(currStr, openingsLeft, closingsLeft):
            if openingsLeft == 0 and closingsLeft == 0:
                solution.append(currStr)
                return

            if openingsLeft > 0:
                currStr += '('
                rec(currStr, openingsLeft - 1, closingsLeft)
                currStr = currStr[:-1]

            if closingsLeft > 0 and closingsLeft > openingsLeft:
                currStr += ')'
                rec(currStr, openingsLeft, closingsLeft - 1)
                currStr = currStr[:-1]

        rec("(", n - 1, n)

        return solution