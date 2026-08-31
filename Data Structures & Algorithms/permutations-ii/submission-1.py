class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        seen=set()
        res,substr=[],[]
        used=[False]*len(nums)
        def backtrack():
            if len(substr)==len(nums) and substr[:] not in res:
                res.append(substr[:])
                return 
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i]==nums[i-1] and not used[i-1]:
                    continue
                used[i]=True
                substr.append(nums[i])
                backtrack()
                substr.pop()
                used[i]=False
        backtrack()
        return res