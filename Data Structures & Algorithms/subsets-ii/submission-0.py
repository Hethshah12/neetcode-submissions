class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,substring=[],[]
        def backtrack(start):
            res.append(substring[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                substring.append(nums[i])
                backtrack(i+1)
                substring.pop()
        backtrack(0)
        return res