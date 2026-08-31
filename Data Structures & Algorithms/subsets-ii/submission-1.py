class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res,sub=[],[]
        n=len(nums)

        def backtrack(i):
            if i==n:
                res.append(sub[:])
                return
            
            sub.append(nums[i])
            backtrack(i+1)
            sub.pop()

            j=i
            while j+1<n and nums[j+1]==nums[j]:
                j+=1
            backtrack(j+1)
        backtrack(0)
        return res



        # nums.sort()
        # res,substring=[],[]
        # def backtrack(start):
        #     res.append(substring[:])
        #     for i in range(start,len(nums)):
        #         if i>start and nums[i]==nums[i-1]:
        #             continue
        #         substring.append(nums[i])
        #         backtrack(i+1)
        #         substring.pop()
        # backtrack(0)
        # return res