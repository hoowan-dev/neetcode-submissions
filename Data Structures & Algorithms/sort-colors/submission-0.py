class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colorCounts = { 0 : 0, 1 : 0, 2 : 0 }
        for c in nums:
            colorCounts[c] += 1

        numsIndex = 0

        for i in range(colorCounts[0]):
            nums[numsIndex] = 0
            numsIndex += 1

        for i in range(colorCounts[1]):
            nums[numsIndex] = 1
            numsIndex += 1

        for i in range(colorCounts[2]):
            nums[numsIndex] = 2
            numsIndex += 1

        