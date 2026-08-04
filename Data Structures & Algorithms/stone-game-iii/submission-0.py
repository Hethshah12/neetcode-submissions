class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n=len(stoneValue)
        dp=[0]*(n+1)
        for i in range(n-1,-1,-1):
            grabbed=0
            best=float('-inf')

            for k in range(3):
                if i+k<n:
                    grabbed+=stoneValue[i+k]
                    lead=grabbed-dp[i+k+1]
                    best=max(best, lead)
                
            dp[i]=best

        return "Alice" if dp[0]>0 else "Bob" if dp[0]<0 else "Tie"