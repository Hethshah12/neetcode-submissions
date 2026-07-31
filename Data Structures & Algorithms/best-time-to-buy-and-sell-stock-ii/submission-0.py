class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[0]*n
        dp[0]=0

        for i in range(1,n):
            dp[i]=max(0, dp[i-1], dp[i-1]+(prices[i]-prices[i-1]))

        return dp[n-1]