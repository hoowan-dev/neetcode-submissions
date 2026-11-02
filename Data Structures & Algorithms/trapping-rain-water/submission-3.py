class Solution:
    def trap(self, height: List[int]) -> int:
        ml, mr = len(height) * [0], len(height) * [0]

        localMax = 0
        for i in range(len(height)):
            ml[i] = localMax
            if height[i] > localMax:
                localMax = height[i]

        localMax = 0
        for i in range(len(height) - 1, -1, -1):
            mr[i] = localMax
            if height[i] > localMax:
                localMax = height[i]

        trappedWater = 0
        for i in range(len(height)):
            mp = min(ml[i], mr[i])
            localTrappedWater = min(ml[i], mr[i]) - height[i]
            if localTrappedWater > 0:
                trappedWater += localTrappedWater

        return trappedWater