class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        low=0
        high=n-1
        if target not in nums:
            return -1
        for i in range(n):
            mid=(low+high)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return mid