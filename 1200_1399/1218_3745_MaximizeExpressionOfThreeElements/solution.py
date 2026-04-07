class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        a=max(nums)
        c=min(nums)
        if nums.count(a)>1:
            b=a
        else:
            nums.remove(a)
            b=max(nums)
        return a+b-c

    
        