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

        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, rooms = 0, 0

        s, e = 0, 0

        while s < len(intervals) and e < len(intervals):
            if start[s] < end[e]:
                rooms += 1
                s += 1
            else:
                rooms -= 1
                e += 1
            res = max(res, rooms)

        return res