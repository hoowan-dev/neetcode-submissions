class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []

        currSubset = []
        def addSubsetsRec(nextIndex):
            if nextIndex == len(nums):
                subsets.append(currSubset.copy())
                return

            currSubset.append(nums[nextIndex])
            addSubsetsRec(nextIndex + 1)

            currSubset.pop()
            addSubsetsRec(nextIndex + 1)

        addSubsetsRec(0)

        return subsets