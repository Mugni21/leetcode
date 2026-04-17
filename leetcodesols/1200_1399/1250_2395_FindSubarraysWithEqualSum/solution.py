class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        sums={}
        n=len(nums)
        for i in range(n-1):
            value=nums[i]+nums[i+1]
            if value in sums:
                return True
            else:
                sums[value]='whatever'
        return False

        