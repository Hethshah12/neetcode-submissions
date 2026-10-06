class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key=lambda t:t[1])
        minheap=[] #(end,curpass)
        curpass=0

        for t in trips:
            numpass,start,end=t
            while minheap and minheap[0][0]<=start:
                curpass-=minheap[0][1]
                heapq.heappop(minheap)
            
            curpass+=numpass
            if curpass>capacity:
                return False
            heapq.heappush(minheap, [end, numpass])
        return True
        # #sort by pickup location using lambda fn 
        # trips.sort(key=lambda t:t[1]) #t is short for trips and t[1] is starting pos 
        # minheap=[] #end pos and pass
        # curpass=0

        # for t in trips:
        #     numpass, start, end=t
        #     while minheap and minheap[0][0]<=start:
        #         curpass-=minheap[0][1]
        #         heapq.heappop(minheap)

        #     curpass+=numpass
        #     if curpass>capacity:
        #         return False
        #     heapq.heappush(minheap, [end, numpass])
        # return True



