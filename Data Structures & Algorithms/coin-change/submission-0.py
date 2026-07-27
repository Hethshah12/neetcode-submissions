class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort()
        dp= [0]*(amount+1)

        for i in range(1, amount+1):
            minn=float('inf')
            for coin in coins:
                diff=i-coin
                if diff<0:
                    break
                minn=min(minn, dp[diff]+1)

            dp[i]=minn
        if dp[amount]<float('inf'):
            return dp[amount]
        else:
            return -1
                    

        # #memoizaation 
        # coins.sort()
        # memo={0:0}

        # def min_coins(amt):
        #     if amt in memo:
        #         return memo[amt]
            
        #     minn=float('inf')
        #     for coin in coins:
        #         diff=amt-coin
        #         if diff<0:
        #             break
        #         minn=min(minn, 1+ min_coins(diff))
        #     memo[amt]=minn
        #     return minn

        # result=min_coins(amount)
        # if result<float('inf'):
        #     return result
        # else:
        #     return -1


        # cnt=0
        # if amount==0:
        #     return 0

        # n=len(coins)
        # if n==1:
        #     if amount%coins[0]==0:
        #         cnt+=1
                
        #     else:
        #         return -1
        #     return cnt

        # ind=len(coins)-1
        # dp=[0]*amount
        # dp[0]=amount
        
        # for i in range(1,amount):
        #     while dp[i]!=0:
        #         if not dp[i-1]<coins[ind]:
        #             dp[i]=amount-coins[ind]
        #             cnt+=1
        #             print(cnt)
        #         else:
        #             ind-=1
        # return cnt

