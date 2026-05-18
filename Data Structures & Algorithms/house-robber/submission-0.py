class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        maxNonNeighbor = nums[0]
        maxNeighbor = nums[1]
        
        for i in range(2, len(nums)):
            currentMax = nums[i] + maxNonNeighbor
            maxNonNeighbor = max(maxNonNeighbor, maxNeighbor)
            maxNeighbor = max(maxNeighbor, currentMax)

        return max(maxNeighbor, maxNonNeighbor)