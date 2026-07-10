class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=sorted(nums1+nums2)
        l=0
        n=len(nums)
        r=n-1
        m=(l+r)//2
        if n%2==0:
            return (nums[m+1]+nums[m])/2
        else:
            return nums[m]