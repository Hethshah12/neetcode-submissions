class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix sum method
        n=len(nums)
        prefix={0:1}
        summ=0
        cnt=0
        for x in nums:
            summ+=x #keep on adding elements
            #check whether the current sum-k has some elements that can be removed in order to get k (basically get i-1th index cnt)
            cnt+=prefix.get(summ-k,0)
            prefix[summ]=prefix.get(summ,0)+1
        return cnt

        # #brute force

        # n=len(nums)
        # cnt=0
        # for i in range(n):
        #     summ=0
        #     for j in range(i,n):
        #         summ+=nums[j]
        #         if k==summ:
        #             cnt+=1
        # return cnt


