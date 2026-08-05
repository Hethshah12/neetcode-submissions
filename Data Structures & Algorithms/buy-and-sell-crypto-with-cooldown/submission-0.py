class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        INF=float('-inf')
        HOLD, SOLD, REST=0,1,2

        dp=[[INF]*3 for _ in range(n)]
        dp[0][HOLD]=-prices[0]
        dp[0][SOLD]= INF
        dp[0][REST]=0

        for i in range(1,n):
            dp[i][HOLD]=max(dp[i-1][HOLD], dp[i-1][REST] - prices[i])
            dp[i][SOLD]=dp[i-1][HOLD]+prices[i]

            dp[i][REST]=max(dp[i-1][REST], dp[i-1][SOLD])

        return max(dp[n-1][SOLD], dp[n-1][REST])