import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # res=[0]
        # n=len(nums)
        # #maxheap
        # for i in range(n):
        #     nums[i]=-nums[i]
        
        # heapq.heapify(nums)
        # while nums:
        #     k-=1
        #     if k!=0:
        #         heapq.heappop(nums)
        #     else:
        #         res[0]=heapq.heappop(nums)
            
            

        # return -res[0]
#above code returns complexity of nlogn 

        heap=[-x for x in nums]
        heapq.heapify(heap)

        for _ in range(k-1):
            heapq.heappop(heap)

        return -heapq.heappop(heap)

        #O(nlogk)
