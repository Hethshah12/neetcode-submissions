import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        st_len=len(stones)
        #to create a max heap 
        for i in range(st_len):
            stones[i]=-stones[i]

        heapq.heapify(stones) #O(n)

        while len(stones)>1:
            largest=heapq.heappop(stones)
            next_largest=heapq.heappop(stones)

            if largest!=next_largest:
                diff=largest-next_largest
            
                heapq.heappush(stones, diff)
            else:
                continue
            
        if len(stones)==1:
            return -heapq.heappop(stones)
        else:
            return 0


        
            


