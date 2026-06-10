class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1d={}
        words2d={}
        for word in words1:
            words1d[word]=words1d.get(word,0)+1
        for word in words2:
            words2d[word]=words2d.get(word,0)+1

        count=0
        for word in words1d:
            if words1d[word]==1 and words2d.get(word,0)==1:
                count+=1
        return count

            
        