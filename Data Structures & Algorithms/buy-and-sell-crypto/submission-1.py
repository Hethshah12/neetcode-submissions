class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        curr=0
        for i in range(n-1):
            for j in range(i+1,n):
                curr=prices[j]- prices[i]
                profit=max(profit, curr)
        return profit
