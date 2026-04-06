class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        cumsum=0
        for i in range(len(nums)):
            if i % 2==0:
                cumsum+=nums[i]
            else:
                cumsum-=nums[i]
        return cumsum
