class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # left=0
        # maxx=0
        # right=len(heights)-1
        # while left<right:
        #     width=right-left
        #     curr=min(heights[left], heights[right])*width
        #     maxx=max(maxx,curr)

        #     if heights[left]>heights[right]:
        #         right-=1
        #     else:
        #         left+=1

        # return maxx
        
        left=0
        n=len(heights)
        right=n-1
        largest=0
        while left<=right:
            w=right-left
            curr=min(heights[left], heights[right])*w

            largest=max(largest, curr)

            if heights[left]>heights[right]:
                right-=1
            else:
                left+=1
        return largest