class MedianFinder:

    def __init__(self):
        self.small, self.large=[], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1* num) #to make it a max heap 
        #now if the largest value in small heap is larger than the smallest value in large heap then we gotta pop
        if (self.small and self.large) and (-1*self.small[0] > self.large[0]):
            ele=heapq.heappop(self.small)
            heapq.heappush(self.large, -ele)

        #now what if the size is eneven then we gotta shift elements from one heap to other as well 
        if len(self.small)>len(self.large)+1:
            val= -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.large)>len(self.small)+1:
            val=heapq.heappop(self.large)
            heapq.heappush(self.small, -val)

    def findMedian(self) -> float:
        if len(self.small)>len(self.large):
            return -self.small[0]
        if len(self.large)>len(self.small):
            return self.large[0]
        return (-self.small[0]+self.large[0])/2
        
        