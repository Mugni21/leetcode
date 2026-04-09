from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumsum=0
        out=[]
        for i in range(len(nums)):
            out.append(nums[i]+cumsum)
            cumsum+=nums[i]
        return out