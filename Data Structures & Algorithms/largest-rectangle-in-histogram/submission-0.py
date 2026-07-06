class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st=[]
        n=len(heights)
        max_area=0
        for i, height in enumerate(heights):
            start=i
            while st and st[-1][0]>height:
                st_h, st_i=st.pop()
                width=i-st_i
                area=st_h*width
                max_area=max(area, max_area)
                start=st_i
            st.append((height,start ))
        while st:
            h,j =st.pop()
            w=n-j
            max_area=max(max_area, h*w)   
        return max_area