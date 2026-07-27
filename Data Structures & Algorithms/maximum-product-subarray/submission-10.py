class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        dp_max=[0]*n
        dp_min=[0]*n

        dp_max[0]=nums[0]
        dp_min[0]=nums[0]
        prod=nums[0]

        for i in range(1,n):
            dp_max[i]=max(dp_max[i-1]*nums[i],nums[i], dp_min[i-1]*nums[i])
            dp_min[i]=min(dp_max[i-1]*nums[i],nums[i], dp_min[i-1]*nums[i])
            prod=max(dp_max[i], prod)
        return prod



        # prod=0

        # n=len(nums)
        # dp=[0]*(n+1)
        # dp[0]=nums[0]
        # if n==1:
        #     return nums[0]
        # if n==2:
        #     return max(nums[0], nums[1], nums[0]*nums[1])
        # dp[1]=max(nums[0], nums[0]*nums[1], nums[1])
        # prod=max(nums[0], nums[0]*nums[1], nums[1])
        # for i in range(2,n):
        #     if dp[i-1]>0 and nums[i]<0:
        #         prod=dp[i-1]
        #         return prod
        #     else:

        #         dp[i]=max(dp[i-1], dp[i-1]*nums[i], nums[i])

        #         if not dp[i]>dp[i-1]:
        #             prod=max(prod, dp[i-1])
        #             return prod
        # return prod


