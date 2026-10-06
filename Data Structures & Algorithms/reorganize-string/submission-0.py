class Solution:
    def reorganizeString(self, s: str) -> str:
        count=Counter(s)
        maxheap=[(-cnt, char) for char, cnt in count.items()]
        heapq.heapify(maxheap)

        prev=None
        res=""
        while maxheap or prev:
            if prev and not maxheap:
                return "" 
            cnt,char=heapq.heappop(maxheap)
            cnt+=1
            res+=char
            if prev:
                heapq.heappush(maxheap, prev)
                prev=None
            if cnt!=0:
                prev=(cnt, char)
        return res
        # count=Counter(s)
        # maxheap=[[-cnt, char] for char, cnt in count.items()]
        # heapq.heapify(maxheap)

        # prev=None
        # res=""
        # while maxheap or prev:
        #     if prev and not maxheap:
        #         return ""
        #     cnt,char=heapq.heappop(maxheap)

        #     cnt+=1 #that is bcoz we have negative count
        #     res+=char
        #     if prev:
        #         heapq.heappush(maxheap, prev)
        #         prev=None
        #     if cnt!=0:
        #         prev=[cnt, char]
        # return res
            
