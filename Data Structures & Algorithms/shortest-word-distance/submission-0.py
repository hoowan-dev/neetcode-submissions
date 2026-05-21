class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        lastWord1Index, lastWord2Index = -1, -1
        bestDist = 30001

        for i, word in enumerate(wordsDict):
            if word == word1:
                lastWord1Index = i
            elif word == word2:
                lastWord2Index = i

            if lastWord1Index != -1 and lastWord2Index != -1:
                dist = abs(lastWord1Index - lastWord2Index)
                if dist < bestDist:
                    bestDist = dist

        return bestDist