class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        best=0
        def check(r,c):
            if (r<0 or r>=row) or (c<0 or c>=col):
                return 0
            if grid[r][c]!=1:
                return 0
            
            grid[r][c]=0
            return 1+ check(r+1,c) +check(r-1,c) +check(r,c+1) +check(r,c-1)

        
        for r in range(row):
            for c in range(col):
                if grid[r][c]==1:
                    best=max(check(r,c),best)
                    
        return best

        