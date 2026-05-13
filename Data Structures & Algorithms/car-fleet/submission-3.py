class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # [[0, 2], [2, 3], [4, 1]]
        #  [5],    [2.666]  [6]

        fleets = []
        for i in range(len(position)):
            fleets.append([position[i], speed[i]])
        fleets = sorted(fleets)
        print(fleets)
        
        numMerged = 0
        for i in range(len(position) - 1, 0, -1):
            currTime = ((target - fleets[i][0]) / fleets[i][1])
            prevTime = ((target - fleets[i - 1][0]) / fleets[i - 1][1])

            if prevTime <= currTime:
                fleets[i - 1][0], fleets[i - 1][1] = fleets[i][0], fleets[i][1]
                numMerged += 1

        '''
        prevTimeToComplete = ((target - fleets[0][0]) / fleets[0][1])
        for i in range(1, len(position)):
            currTimeToComplete = ((target - fleets[i][0]) / fleets[i][1])
            print(prevTimeToComplete)
            if prevTimeToComplete <= currTimeToComplete:
                numMerged += 1
            prevTimeToComplete = currTimeToComplete

        print(prevTimeToComplete)
        '''

        return len(position) - numMerged

        '''
        numMerged = 0
        numCompleted = 0
        while numCompleted < len(fleets):
            for i in range(len(fleets)):
                if fleets[i][0] > target:
                    break

                fleets[i][0] += fleets[i][1]
                if fleets[i][0] > target:
                    numCompleted += 1

                if i != 0 and fleets[i][0] == fleets[i - 1][0] and fleets[i][1] != fleets[i - 1][1]:
                    fleets[i - 1][1] = fleets[i][1]
                    numMerged += 1

        return len(position) - numMerged
        '''