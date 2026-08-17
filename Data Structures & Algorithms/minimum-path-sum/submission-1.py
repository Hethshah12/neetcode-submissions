class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        INF=float('inf')
        res=[0]
        dp=[[INF]*cols for _ in range(rows)]
        dp[rows-1][cols-1]=grid[rows-1][cols-1]
        for i in range(rows-1,-1,-1):
            for j in range(cols-1, -1, -1):
                if j<cols-1 and i<rows-1:
                    dp[i][j]=grid[i][j]+min(dp[i+1][j], dp[i][j+1])
                elif (i==rows-1) and j<cols-1:
                    dp[i][j]=dp[i][j+1]+grid[i][j]
                elif (j==cols-1) and i<rows-1:
                    dp[i][j]=dp[i+1][j]+grid[i][j]
        
        return dp[0][0]