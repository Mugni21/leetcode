class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        nrocks=len(rocks)
        realcap=[capacity[i]-rocks[i] for i in range(nrocks)]
        realcap.sort()
        j=0
        count=0
        while additionalRocks>0 and j<=nrocks-1:
            if additionalRocks>=realcap[j]:
                count+=1
            additionalRocks-=realcap[j]
            j+=1
          
        return(count)


        