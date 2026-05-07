def getMaxWaterAtIndexBruteForce(height: List[int], i):
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

def getMaxWaterAtIndex(height: List[int], i, preMax, postMax):
    if i <= 0 or i >= len(height) - 1:
        return 0

    return max(min(preMax, postMax) - height[i], 0)

def computePrefixaAndSuffixMaxes(height: List[int]):
        prefixMaxes = [0] * len(height)
        suffixMaxes = [0] * len(height)

        currentPrefixMax = height[0]
        for i in range(1, len(height)):
            prefixMaxes[i] = currentPrefixMax
            if (height[i] > currentPrefixMax):
                currentPrefixMax = height[i]

        currentSuffixMax = height[len(height) - 1]
        for i in range(len(height) - 2, -1, -1):
            suffixMaxes[i] = currentSuffixMax
            if (height[i] > currentSuffixMax):
                currentSuffixMax = height[i]

        return prefixMaxes, suffixMaxes

class Solution:
    def trap(self, height: List[int]) -> int:
        # pre-compute prefix and suffic maxes at each index 
        prefixMaxes, suffixMaxes = computePrefixaAndSuffixMaxes(height)

        totalVolume = 0
        for i in range(len(height)):
            # totalVolume += getMaxWaterAtIndexBruteForce(height, i)
            totalVolume += getMaxWaterAtIndex(height, i, prefixMaxes[i], suffixMaxes[i])

        return totalVolume