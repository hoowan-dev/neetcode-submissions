class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        mergedIntervals = [ intervals[0] ]

        for i in range(1, len(intervals)):
            currInterval = intervals[i]
            prevInterval = mergedIntervals[-1]

            if currInterval[0] <= prevInterval[1]:
                prevInterval[1] = max(prevInterval[1], currInterval[1])
            else:
                mergedIntervals.append(currInterval)

        return mergedIntervals

