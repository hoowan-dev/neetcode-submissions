class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleets = []
        for i in range(len(position)):
            fleets.append([position[i], speed[i]])
        fleets = sorted(fleets)
        
        numMerged = 0
        for i in range(len(position) - 1, 0, -1):
            currTime = ((target - fleets[i][0]) / fleets[i][1])
            prevTime = ((target - fleets[i - 1][0]) / fleets[i - 1][1])

            if prevTime <= currTime:
                fleets[i - 1][0], fleets[i - 1][1] = fleets[i][0], fleets[i][1]
                numMerged += 1

        return len(position) - numMerged