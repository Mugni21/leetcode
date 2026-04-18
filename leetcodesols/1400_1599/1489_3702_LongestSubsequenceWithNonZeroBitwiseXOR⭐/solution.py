class Solution:

    #Very neat sol. So the idea is the following. I had to read about  bit XOR. 
    #So XOR between two integers is just, find their binary representation and do XOR
    #on every digit (so just addition mod 2). Then from that we can infer tons of nice properties
    #The thing is associative, a*b=0 if and only if a=b, a*0=a, and a super useful one is: 
    #x*y*z=0 impies that x*y=z or y*z=x by associativity and the previous properties
    #So using that last property gives the solution. 

    #If we are looking at the XOR between n numbers, then if that output is 0, we can turn it into 
    #a non-zero outpu by removing one of its components but if and only if the element we remove is
    #non-zero!
    #So that gives the solution.
    #1.Compute the xor of all elements in the array. 
    #2. If its non-zero then the answer is len(list)
    #3. Otherwise, we can turn it into a nonzero XOR by removing any non=zer0 element. So, if 
    #there is at least one non-zero element, we remove it and have a subsequence of size n-1 that is nonzero
    #4. The bad issue is if they are all 0, which then gives answer 0
    def longestSubsequence(self, nums: List[int]) -> int:
        cum=0
        if nums == [0]*len(nums):
            return 0
        for num in nums:
            cum  ^= num
        if cum==0:
            return len(nums)-1
        else:
            return len(nums)

        
        
           

    
        