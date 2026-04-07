class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        current=''
        for k in range(len(words)):
            current+=words[k]
            if s==current:
                return True
            if len(current) > len(s):
                return False
            
        return False
            
        
