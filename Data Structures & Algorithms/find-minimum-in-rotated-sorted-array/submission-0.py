class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = nums[0]

        for i in range(1, len(nums)):
            val = nums[i]
            if val < min:
                min = val

        return min