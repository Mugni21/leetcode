class Solution:
    #This took me WAYY too long..........
    def maximumPossibleSize(self, nums: List[int]) -> int:
        count = 0
        prev = float('-inf')
    
        for x in nums:
            if x >= prev:
                prev = x
                count += 1
                
        return count

        