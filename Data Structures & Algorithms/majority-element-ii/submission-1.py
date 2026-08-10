import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        target=math.floor(n/3)
        res=[]
        count={}
        for i in range(n):
            count[nums[i]]=1+count.get(nums[i], 0)
            
        for i in count:
            if count[i]>target:
                res.append(i)
        return res