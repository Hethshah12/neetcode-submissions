from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        origin=[[0,0]]

        npts=len(points)

        minheap=[]

        for i in range(npts):
            dist=sqrt((points[i][0])**2 + (points[i][1])**2)
            heapq.heappush(minheap, (dist,points[i]))

        heapq.heapify(minheap)
        res=[]
        while k>0:
            node=heapq.heappop(minheap)[1]
            res.append(node)
            k-=1

    

        return res