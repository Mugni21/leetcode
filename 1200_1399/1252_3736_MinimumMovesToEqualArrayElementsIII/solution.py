class Solution:
    def minMoves(self, nums: List[int]) -> int:
        m=max(nums)
        tot=0
        for k in nums: 
            tot+=abs(k-m)
        return tot
        