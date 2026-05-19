class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]

        def conflicts(intervalA: List[int], intervalB: List[int]) -> bool:
            return (intervalA[0] <= intervalB[0] and intervalA[1] >= intervalB[0]) or (intervalB[0] <= intervalA[0] and intervalB[1] >= intervalA[0])

        newIntervals = []
        inserted = False
        
        for interval in intervals:
            if conflicts(interval, newInterval):
                newInterval[0], newInterval[1] = min(newInterval[0], interval[0]), max(newInterval[1], interval[1])
            else:
                if inserted == False and interval[0] > newInterval[0]:
                    inserted = True
                    newIntervals.append(newInterval)
                
                newIntervals.append(interval)

        if inserted == False:
            newIntervals.append(newInterval)

        return newIntervals
                