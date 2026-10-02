"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        interval=[]
        for pair in intervals:
            interval.append([pair.start, pair.end])
        
        interval.sort()
        prev=float('-inf')

        for c_s, c_e in interval:
            if c_s<prev:
                return False
            prev=c_e
        return True
