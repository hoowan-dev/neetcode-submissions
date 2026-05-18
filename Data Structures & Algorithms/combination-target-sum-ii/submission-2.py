class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []

        def computeCombinationsRec(i = 0, currCombination = [], currSum = 0):
            if currSum == target:
                combinations.append(currCombination.copy())
                return

            if currSum > target or i >= len(candidates):
                return

            # simulate adding this element
            currCombination.append(candidates[i])
            computeCombinationsRec(i + 1, currCombination, currSum + candidates[i])
            currCombination.pop()

            # simulate trying to add the next non-duplicate element
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1

            computeCombinationsRec(i + 1, currCombination, currSum)

        candidates.sort()
        computeCombinationsRec()

        return combinations