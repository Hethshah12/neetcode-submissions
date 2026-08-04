class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF= float('inf')
        g=defaultdict(list)
        for u,v,w in flights:
            g[u].append((v,w))

        best=[INF]*n
        best[src]=0
        q=deque([(src, 0)]) 

        for _ in range(k+1):
            for _ in range(len(q)):
                node,c = q.popleft()
                for v,w in g[node]:
                    if c+w<best[v]:
                        best[v]=c+w
                        q.append((v,c+w))
        return -1 if best[dst]==INF else best[dst]   