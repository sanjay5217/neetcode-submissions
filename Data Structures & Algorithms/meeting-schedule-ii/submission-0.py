"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start, end = sorted([s.start for s in intervals]), sorted([e.end for e in intervals])
        s = e = 0
        meetings = 0
        res = 0

        while s < len(intervals):
            if start[s] < end[e]:
                meetings += 1
                s += 1
            else:
                meetings -= 1
                e += 1
            res = max(res, meetings)
        return res