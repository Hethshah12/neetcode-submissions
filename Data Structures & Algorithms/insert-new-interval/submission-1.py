class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res=[]
        n=len(intervals)
        st,end=newInterval
        

        for (i,(c_st, c_end)) in enumerate(intervals):
            if end<c_st:
                res.append([st,end])
                res.extend(intervals[i:])
                return res
            elif c_end<st:
                res.append([c_st, c_end])
            else:
                st=min(st,c_st)
                end=max(end,c_end)
        res.append([st,end])
        return res

        
            
        
