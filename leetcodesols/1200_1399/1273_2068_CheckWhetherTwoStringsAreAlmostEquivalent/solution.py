class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        freqs={}
        n=len(word1)
        for i in range(n):
           
            freqs[word1[i]]=freqs.get(word1[i],0)+1
            freqs[word2[i]]=freqs.get(word2[i],0)-1
        
        for freq in freqs.values():
            if abs(freq)>3:
                return False
        return True
        