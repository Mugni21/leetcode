class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1]-1)*(nums[-2]-1)
    




    #Clearner solution in linear time:
    
    #def maxProduct(self, nums: List[int]) -> int: 
        n1=0
        n2=0
        for j,num in enumerate(nums):
            if num>=n1:
                n2=n1
                n1=num
            elif num>=n2:
                n2=num
        return (n1-1)*(n2-1)
       
       
            

