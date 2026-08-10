class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        seen=set()
        mheap=[(0, (0,0))]

        while mheap:
            diff,(x,y) = heapq.heappop(mheap)
            if (x,y) in seen:
                continue
            seen.add((x,y))
            
            if (x,y) == (rows-1, cols-1):
                return diff
            
            for nr,nc in [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]:
                if (nr<0 or nr>=rows) or (nc<0 or nc>=cols) or ((nr,nc) in seen):
                    continue 
                newdiff=max(diff, abs(heights[x][y]-heights[nr][nc]))
                heapq.heappush(mheap, [newdiff, (nr,nc)])
        
            