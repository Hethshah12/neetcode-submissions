class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0], nums[1])
        def check(arr):
            m=len(arr)
            dp=[0]*m
            dp[0]=arr[0]
            dp[1]=max(arr[0], arr[1])
            for i in range(2,m):
                dp[i]=max(dp[i-1], dp[i-2]+arr[i])
            
            return dp[m-1]
            

        
        return max(check(nums[:-1]), check(nums[1:]))