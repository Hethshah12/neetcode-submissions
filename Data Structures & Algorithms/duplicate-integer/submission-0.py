class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        n=len(nums)
        nums.sort()
        res=False
        present=set()
        for val in range(n):
            if nums[val] not in present:
                present.add(nums[val])
            else:
                return True
        return False
