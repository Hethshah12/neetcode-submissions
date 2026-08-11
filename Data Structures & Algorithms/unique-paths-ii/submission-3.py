class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        grid=obstacleGrid
        rows=len(grid)
        cols=len(grid[0])
        if grid[0][0]==1:
                    return 0
        dp=[]
        for i in range(rows):
            dp.append([0]*cols)


        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    dp[i][j]=float('inf')
                else:
                    dp[i][j]=grid[i][j]
        dp[0][0]=1
        for i in range(rows):
            for j in range(cols):
                
                if dp[i][j]==float('inf'):
                    continue
                val=0
                if i>0 and dp[i-1][j]!=float('inf'):
                    val+=dp[i-1][j]
                if j>0 and dp[i][j-1]!=float('inf'):
                    val+=dp[i][j-1]
                
                dp[i][j]+=val
                
        return 0 if dp[rows-1][cols-1]==float('inf') else dp[rows-1][cols-1]