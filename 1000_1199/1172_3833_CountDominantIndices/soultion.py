class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        doms=0
        n=len(nums)
        for i in range(n-1):
            avg=sum(nums[i:])/(n-i)
            if nums[i]>avg:
                doms+=1
        return doms
        