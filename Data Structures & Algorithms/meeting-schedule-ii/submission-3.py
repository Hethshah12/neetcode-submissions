"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        interval=[]
        for pair in intervals:
            interval.append([pair.start, pair.end])
        
        interval.sort()
        
        rooms=[]

        for c_s,c_e in interval:
            if rooms and rooms[0]<=c_s:
                heapq.heappop(rooms)
            heapq.heappush(rooms, c_e)
        return len(rooms)
        # for c_s, c_e in interval:
        #     if rooms and min(rooms)<=c_s:
        #         rooms.remove(min(rooms))
        #     rooms.append(c_e)
        # return len(rooms)
