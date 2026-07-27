class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #BU DP CONSTANT SPACE
        n=len(cost)
        prev,curr=0, 0

        for i in range(2, n+1):
            prev,curr= curr, min(prev+cost[i-2], curr+cost[i-1])
        return curr
        #BOTTOM UP DP WITH SPACE
        # n=len(cost)
        # dp=[0]*(n+1)
        # dp[0]=0
        # dp[1]=0
        # for i in range(2,n+1):
        #     dp[i]=min(dp[i-2]+cost[i-2], dp[i-1]+cost[i-1])
        #     print(dp)
        # return dp[n]

        


        