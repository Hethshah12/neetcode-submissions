class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel=set(days)
        last=days[-1]

        dp=[0]*(last+31)
        for day in range(last,0,-1):
            if day not in travel:
                dp[day]=dp[day+1]
            else:
                dp[day]=min((costs[0]+dp[day+1]), (costs[1]+dp[day+7]), (costs[2]+dp[day+30]))
        
        return dp[1]