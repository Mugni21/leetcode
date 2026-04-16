class Solution:
    def minOperations(self, nums: List[int]) -> int:
        m=len(nums)
        ops=0
        for i in range(m-1):
            if nums[i]>=nums[i+1]:
                diff=nums[i]-nums[i+1]+1
                ops+=diff
                nums[i+1]=nums[i+1]+diff
        return ops



        