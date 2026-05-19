"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0

        intervals = sorted(intervals, key = lambda x : x.start)
        meetingRooms = [intervals[0]]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            inserted = False
            for j in range(len(meetingRooms)):
                if interval.start >= meetingRooms[j].end:
                    meetingRooms[j] = interval
                    inserted = True
                    break
            if inserted == False:
                meetingRooms.append(interval)

        return len(meetingRooms)        