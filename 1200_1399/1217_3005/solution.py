class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        counts=dict()
        for i in nums:
            counts[i]=counts.get(i,0)+1
        freqlist=list(counts.values())
        freqmax=max(freqlist)

        return freqmax*(freqlist.count(freqmax))
