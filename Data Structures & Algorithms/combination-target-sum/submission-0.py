class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = []

        def computeCombinationsRec(i = 0, currCombination = [], currSum = 0):
            if currSum == target:
                combinations.append(currCombination.copy())
                return

            # simulate adding the remaining numbers in ascending order
            for j in range(i, len(nums)):
                # stop at this point - no remaining numbers will hit target
                if currSum + nums[j] > target:
                    return

                currCombination.append(nums[j])
                computeCombinationsRec(j, currCombination, currSum + nums[j])
                currCombination.pop()

        nums.sort()
        computeCombinationsRec()

        return combinations