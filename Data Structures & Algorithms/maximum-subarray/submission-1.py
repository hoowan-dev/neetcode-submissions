class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxOverall = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            maxSoFar = max(num, nums[i - 1] + num)
            nums[i] = maxSoFar

            if maxSoFar > maxOverall:
                maxOverall = maxSoFar

        return maxOverall