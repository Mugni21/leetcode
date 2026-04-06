#Naive solution
#class Solution:
#    def sortedSquares(self, nums: List[int]) -> List[int]:
#        for i in range(nums):
#            nums[i]=nums[i]**2
#        nums.sort()
#        return nums

#Just square everything and then sort

#O(n) solution uses the fact that the extremes of the list are the largest in absolute value
#and traverses the list from both ends:

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        leftpoint=0
        rightpoint=len(nums)-1
        newlist=[0]*len(nums)
        pos=len(nums)-1
        while leftpoint<= rightpoint:
            if abs(nums[leftpoint])< abs(nums[rightpoint]):
                newlist[pos]=nums[rightpoint]**2
                rightpoint=rightpoint-1
            else:
                newlist[pos]=nums[leftpoint]**2
                leftpoint=leftpoint+1
            pos=pos-1
       
       
        return newlist