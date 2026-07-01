class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        maxx=0
        right=len(heights)-1
        while left<right:
            width=right-left
            curr=min(heights[left], heights[right])*width
            maxx=max(maxx,curr)

            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1

        return maxx
        
