class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        currentacum0 = 0
        listblocks = []

        for i in range(len(nums)):
            if nums[i] == 0:
                currentacum0 += 1
            else:
                listblocks.append(currentacum0)
                currentacum0 = 0

        
        if currentacum0 > 0:
            listblocks.append(currentacum0)

        #They idea here is that you have an array of size n, it has exactly 1+2+...+n possible subarrays!
        substringys = [(n * (n + 1)) // 2 for n in listblocks]
        return sum(substringys)

#An even BETTER soluion. We compute the sum n*(n+1)/2 on the same pass! We avoid the second loop

#class Solution:
    #def zeroFilledSubarray(self, nums: List[int]) -> int:
        currentacum0 = 0
        ans=0

        for x in nums:
            if x == 0:
                currentacum0 += 1
                ans+=currentacum0
            else:
                currentacum0 = 0

    
        return ans


