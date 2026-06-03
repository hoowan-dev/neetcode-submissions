class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumpTruthTable = [False] * len(nums)
        jumpTruthTable[len(nums) - 1] = True

        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if jumpTruthTable[i + j] == True:
                    jumpTruthTable[i] = True
                    break

        return jumpTruthTable[0]