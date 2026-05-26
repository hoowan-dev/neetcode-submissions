class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        memo = [0] * len(nums)
        memo[0] = nums[0]

        maxOverall = memo[0]
        for i in range(1, len(nums)):
            num = nums[i]
            maxSoFar = max(num, memo[i - 1] + num)
            memo[i] = maxSoFar

            if maxSoFar > maxOverall:
                maxOverall = maxSoFar

        return maxOverall