class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total=sum(stones)
        target=total//2

        def dfs(i, curr):
            if curr>=total or i==len(stones):
                return abs(curr-(total-curr))
            if (i,curr) in dp:
                return dp[(i,curr)]

            dp[(i,curr)]=min(dfs(i+1,curr), dfs(i+1, curr+stones[i]))
            return dp[(i,curr)]
        
        dp={}
        return dfs(0,0)
        # stones.sort()
        # # print(stones)
        # dp=[0]*(len(stones))
        # i=0
        # while len(stones)>1 and i<len(stones):
        #     left=stones.pop()
        #     right=stones.pop()
        #     if left==right:
        #         continue
        #     else:
        #         stones.append(abs(left-right))
        #     dp[i]=dp[i-1]
        #     print(stones)
        # return dp[len(stones)-2]
