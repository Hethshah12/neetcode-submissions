class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        cnt=0
        res=[]
        for c_s, c_e in intervals:
            if res and c_s<res[-1][1]:
                cnt+=1
                res[-1][1]=min(res[-1][1], c_e)
            else:
                res.append([c_s, c_e])
        return cnt
