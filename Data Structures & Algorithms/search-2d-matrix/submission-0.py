class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m=len(matrix)
        n=len(matrix[0])
        #number of elements
        t=m*n
        l=0
        r=t-1

        #until criss cross
        while l<=r:
            m=(l+r)//2
            i=m//n
            j=m%n

            mid_ele=matrix[i][j]

            if mid_ele==target:
                return True

            elif mid_ele>target:
                r=m-1
            else:
                l=m+1
        return False