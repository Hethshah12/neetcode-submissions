class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # n=len(prices)
        # profit=0
        # curr=0
        # for i in range(n-1):
        #     for j in range(i+1,n):
        #         curr=prices[j]- prices[i]
        #         profit=max(profit, curr)
        # return profit

        #better code 

        n=len(prices)
        profit=0
        min_price=prices[0]

        for i in range(n):
            ele=prices[i]
            min_price=min(min_price, ele)
            profit=max(profit, ele-min_price)
        return profit
