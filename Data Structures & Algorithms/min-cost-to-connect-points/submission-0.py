class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n=len(points)
        cost=0
        mheap=[(0,0)]
        seen=set()

        while len(seen)<n:
            dist, i=heapq.heappop(mheap)
            if i in seen:
                continue 
            
            seen.add(i)
            cost+=dist

            xi,yi=points[i]

            for j in range(n):
                xj,yj=points[j]
                nei_d=abs(xj-xi)+abs(yj-yi)
                heapq.heappush(mheap, (nei_d, j))
        return cost

            