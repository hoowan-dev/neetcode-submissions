class Solution:
    def maxScore(self, s: str) -> int:
        numOnes = 0
        for c in s:
            if c == '1':
                numOnes += 1

        currScore = numOnes
        if s[0] == '1':
            currScore -= 1
        else:
            currScore += 1

        maxScore = currScore
        for i in range(1, len(s) - 1):
            c = s[i]
            if c == '0':
                currScore += 1
            else:
                currScore -= 1

            if currScore > maxScore:
                maxScore = currScore

        return maxScore