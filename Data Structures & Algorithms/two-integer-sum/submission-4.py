class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        compMap = { target - nums[0] : 0 } # target : index

        for i in range(1, len(nums)):
            comp = nums[i]
            if comp in compMap:
                return [compMap[comp], i]
            compMap[target - comp] = i

        # error state
        return [-1,-1]