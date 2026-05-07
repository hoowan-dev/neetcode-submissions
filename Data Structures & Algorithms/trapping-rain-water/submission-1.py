def getMaxWaterAtIndex(height: List[int], i):
    if i <= 0 or i >= len(height) - 1:
        return 0

    l = i - 1
    r = i + 1

    tallestLeftIndex = i
    tallestRightIndex = i

    while l >= 0:
        if height[l] > height[tallestLeftIndex]:
            tallestLeftIndex = l
        l -= 1
        
    while r < len(height):
        if height[r] > height[tallestRightIndex]:
            tallestRightIndex = r
        r += 1 

    return min(height[tallestLeftIndex], height[tallestRightIndex]) - height[i]

class Solution:
    def trap(self, height: List[int]) -> int:
        totalVolume = 0

        for i in range(len(height)):
            totalVolume += getMaxWaterAtIndex(height, i)

        return totalVolume