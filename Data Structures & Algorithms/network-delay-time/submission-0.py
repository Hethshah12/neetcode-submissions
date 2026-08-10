from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        INF=float('inf')
        g=defaultdict(list)
        for u,v,w in times:
            g[u].append((v,w))
        # print(g)

#lets create a distance vector to write the shortest distance it takes so that we can use dijkstra's algo
        dist=[INF]*(n+1)
        dist[k]=0 #time to reach src will always be 0 

    
        pq=[(0,k)] #always use heap for such problems as it will help you sort wrt distance 
        while pq:
            d, node= heapq.heappop(pq)

            if d>dist[node]:
                continue 
            for nei, w in g[node]:
                neid=d+w
                if neid<dist[nei]:
                    dist[nei]=neid
                    heapq.heappush(pq, (neid, nei))

        ans=max(dist[1:])
        return ans if ans<INF else -1
                


