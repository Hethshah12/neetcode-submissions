class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n=len(intervals)
        intervals.sort()
        res=[]

        for c_s, c_e in intervals:
            if res and c_s<= res[-1][1]:
                res[-1][1]=max(res[-1][1], c_e)
            else:
                res.append([c_s, c_e])
        return res