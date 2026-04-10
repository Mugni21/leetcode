class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums)>1:
            for j in range(len(nums)-1):
                nums[j]=(nums[j]+nums[j+1]) % 10
            nums.pop(-1)
        return nums[0]
        
        
        