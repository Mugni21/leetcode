class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        rightpoint=start
        leftpoint=start-1
        n=len(nums)
        maxd=max(n-start,start)
        for i in range(n):
            if rightpoint<= n-1:
                if nums[rightpoint]==target:
                    return abs(rightpoint-start)
            if leftpoint>=0: 
                if nums[leftpoint]==target:
                    return abs(leftpoint-start)
            rightpoint+=1
            leftpoint-=1
        
            
