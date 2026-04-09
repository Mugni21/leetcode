class Solution:
    def returnToBoundaryCount(self, nums: List[int]) -> int:
        counter=0
        cumsum=0
        for i,v in enumerate(nums):
            cumsum+=v
            if cumsum==0:
                counter+=1
        return counter
