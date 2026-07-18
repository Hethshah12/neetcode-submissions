from math import sqrt
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # npts=len(points)
        # minheap=[]

        # for i in range(npts):
        #     dist=sqrt((points[i][0])**2 + (points[i][1])**2)
        #     heapq.heappush(minheap, (dist,points[i]))

        # heapq.heapify(minheap)
        # res=[]
        # while k>0:
        #     node=heapq.heappop(minheap)[1]
        #     res.append(node)
        #     k-=1
        #return res

        #Nlogn approach (good but can be better)

        #nlogk approach 
        #idea is to first create a max heap that can hold only k elements and at the end only heap elemtns are returned
        
        def dist(x,y):
            return x**2 + y**2
        
        heap=[]
        for x,y in points:
            d=dist(x,y)
            if len(heap)<k:
                heapq.heappush(heap, (-d, [x,y]))
            else:
                heapq.heappushpop(heap, (-d, [x,y]))
            
        return [(x,y) for d, [x,y] in heap]
