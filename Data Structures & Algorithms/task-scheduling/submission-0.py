import heapq
from collections import deque
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter=Counter(tasks)
        maxheap=[]
        for ele, val in counter.items():
            heapq.heappush(maxheap, -val)
        heapq.heapify(maxheap)

        time= 0
        q=deque()

        while maxheap or q:
            time+=1
            if maxheap:
                cnt=1+heapq.heappop(maxheap)
                if cnt!=0:
                    q.append([cnt, time+n])

            if q and q[0][1]==time:
                heapq.heappush(maxheap, q.popleft()[0])

        return time

