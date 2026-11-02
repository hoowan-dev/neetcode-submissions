class Solution:
    def trap(self, height: List[int]) -> int:
        ml, mr = len(height) * [0], len(height) * [0]

        lMax, rMax = 0, 0
        for i in range(len(height)):
            ml[i] = lMax
            if height[i] > lMax:
                lMax = height[i]

            j = len(height) - 1 - i
            mr[j] = rMax
            if height[j] > rMax:
                rMax = height[j]

        trappedWater = 0
        for i in range(len(height)):
            mp = min(ml[i], mr[i])
            localTrappedWater = min(ml[i], mr[i]) - height[i]
            if localTrappedWater > 0:
                trappedWater += localTrappedWater

        return trappedWater