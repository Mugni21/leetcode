class Solution:
    #Elegant solution!! 
    #So I did like a greedy approach I just said. Well all that matters are the max an min value in a subarray
    #If max-min \leq k, then I can just add as much stuff in the middle as I can. So I sorted the array
    #and the first subarray from the left (smalles value in the list) then added as much stuff as possible
    #going forward until the tright boundary of the subarray-the initial one exceeded k. 
    #I keep doing this until we hace explored the entire array!
    #There's no need to look at all possible subarrays, sorting first simplidies this greatly.
    #Loved the problem and solution :) 
    
    def partitionArray(self, nums: List[int], k: int) -> int:
        n=len(nums)
        nums.sort()
        cuts=0
        j=0
        init=0
        while j<n: 
            while j<n and (nums[j]-nums[init] <=k):
                j+=1
            init=j
            cuts+=1
        return cuts
        


        