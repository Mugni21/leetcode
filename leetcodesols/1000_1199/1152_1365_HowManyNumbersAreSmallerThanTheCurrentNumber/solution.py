class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n=len(nums)
        minis=[0]*len(nums)
        for i in range(n):
            tot=0
            for j in range(n):
                if i!=j and nums[j]<nums[i]:
                    tot+=1
            
            minis[i]=tot
        return minis
            



#Better solution...the last one is just brute force. We can sort the array and then the first index of 
#appearance of the number k gives the exact number of elements strictly smaller!


#class Solution:
 #   def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        numsorted=sorted(nums)
        rank={}

        for j,num in enumerate(numsorted):
            if num not in rank:
                rank[num]=j
        return [rank[j] for j in nums]      

            
