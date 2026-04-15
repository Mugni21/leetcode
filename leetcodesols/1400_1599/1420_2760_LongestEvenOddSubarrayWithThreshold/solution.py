class Solution:
#Sort of same idea as 1416_2994_PartitionArraySuchThatMaximumDifferenceIsk.
#Just scan greedily from left to right the largest possible subarray we can construct that satisfies all 
#the requirements. I could've optimized it further by taking the new starting point as the previous endpont/
#As n was small, I didn't care. 
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        max_len=0
        for i in range(n):
            if nums[i]%2==0 and nums[i]<=threshold:
                current_len=1
                j=i+1
                while j<n and (nums[j-1]%2 != nums[j]%2) and (nums[j]<=threshold):
                    current_len+=1
                    j+=1
                if current_len>=max_len:
                    max_len=current_len
        return max_len
    
#With the small imporvement mentioned eariler: 
#class Solution:
    #def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        n=len(nums)
        max_len=0
        i=0
        while i<n:
            if nums[i]%2==0 and nums[i]<=threshold:
                current_len=1
                j=i+1
                while j<n and (nums[j-1]%2 != nums[j]%2) and (nums[j]<=threshold):
                    current_len+=1
                    j+=1
                i=j
                if current_len>=max_len:
                    max_len=current_len
            else:
                i+=1
            
        return max_len
                
    


        
                
    


        