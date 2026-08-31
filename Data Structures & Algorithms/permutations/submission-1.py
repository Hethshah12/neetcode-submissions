class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        substr, res=[], []
        def backtrack():
            if len(substr)==n:
                res.append(substr[:]) #append the copy of substr 
                return 
        
            for x in nums:
                if x not in substr:
                    substr.append(x)
                    backtrack()
                    substr.pop()
        
        backtrack()
        return res