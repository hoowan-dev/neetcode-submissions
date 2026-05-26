class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxOverall = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            maxSoFar = max(num, nums[i - 1] + num)
            nums[i] = maxSoFar

            if maxSoFar > maxOverall:
                maxOverall = maxSoFar

        return maxOverall