class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxprofit=[]
        mincapital=list(zip(capital,profits))
        heapq.heapify(mincapital)

        for _ in range(k):
            while mincapital and  w >=mincapital[0][0]:
                c,p=heapq.heappop(mincapital)
                heapq.heappush(maxprofit, [-p, c])
            if not maxprofit:
                break
            w+= -1*heapq.heappop(maxprofit)[0]
        return w
            
