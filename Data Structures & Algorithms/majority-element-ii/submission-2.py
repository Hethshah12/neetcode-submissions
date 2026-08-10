import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n=len(nums)
        target=math.floor(n/3)
        res=[]
        count={}
        for i in range(n):
            count[nums[i]]=1+count.get(nums[i], 0)
            if count[nums[i]]>target:
                res.append(nums[i])

        return list(set(res))