#incoding:utf-8
# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return intervals
        res = []
        intervals.sort(key=lambda x: x.start)
        length = len(intervals)
        for i in range(1, length):
            if intervals[i - 1].end < intervals[i].start:
                res.append(intervals[i - 1])
            else:
                intervals[i].start = intervals[i - 1].start
                intervals[i].end = max(intervals[i].end, intervals[i - 1].end)
        res.append(intervals[length - 1])
        return res
