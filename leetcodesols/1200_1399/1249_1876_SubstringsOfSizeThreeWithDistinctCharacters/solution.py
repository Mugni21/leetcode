class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        if n<3:
            return 0
        unique=0
        for i in range(n-2):
            if s[i]!=s[i+1] and s[i]!=s[i+2] and s[i+1]!=s[i+2]:
                unique+=1
        return unique


        