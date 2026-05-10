class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = [-1] * 2
        compToIndex = { target - nums[0] : 0 }

        for i in range(1, len(nums)):
            if nums[i] in compToIndex:
                result[0] = compToIndex[nums[i]]
                result[1] = i
                break
            compToIndex[target - nums[i]] = i

        return result