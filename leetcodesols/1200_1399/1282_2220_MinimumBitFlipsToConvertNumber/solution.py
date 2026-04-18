class Solution:
    #My sol: Its just the hamming distance between the binary representations: 
    #So XOR, tells us where they differ then just count 1's on the XOR
    def minBitFlips(self, start: int, goal: int) -> int:
        diff=bin(start ^ goal)[2:]
        ops=0
        for bit in diff:
            if bit=='1':
                ops+=1
        return ops

#Even cleaner impoementation: .bit_count() does the "count 1"'s for us: 
    #def minBitFlips(self, start: int, goal: int) -> int:
        #return (start ^ goal).bit_count()