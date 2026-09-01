from collections import Counter
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=r=0
        res,total=0,0

        while r<len(nums):
            total+=nums[r]
            while (nums[r]*(r-l+1)>total+k):
                total-=nums[l]
                l+=1
            res=max(res, (r-l+1))
            r+=1
        return res
            
        # nums.sort()
        # bestfrq=1
        # n=len(nums)
        # for i in range(n-1,-1,-1):
        #     target=nums[i]
        #     budget=k
        #     currfrq=1
        #     j=i-1
        #     while j>=0:
        #         cost=target-nums[j]
        #         if cost>budget:
        #             break
        #         budget-=cost
        #         j-=1
        #         currfrq+=1
        #     bestfrq=max(bestfrq,currfrq)
        # return bestfrq