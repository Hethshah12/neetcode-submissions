class Solution:
    def climbStairs(self, n: int) -> int:
        #there are two things here , you either pick 2 or you pick 1 for each iteration
        #the maximum steps you can take is n so if n=3 you need max of n steps to reach 
        if n==1:return 1
        if n==2:return 2
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=2
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
            print(dp[i])
        return dp[n-1]

