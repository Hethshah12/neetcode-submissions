class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        count=0

        def check(r, c):
            if (r<0 or r>=rows) or (c<0 or c>=cols):
                return
            if grid[r][c]!="1":
                return 
            grid[r][c]=0
            check(r+1,c)
            check(r-1,c)
            check(r,c+1)
            check(r,c-1)
            
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]== "1":
                    count+=1
                    check(r,c)

        return count
