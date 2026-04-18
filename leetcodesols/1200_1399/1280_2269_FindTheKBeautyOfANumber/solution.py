class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        s=str(num)
        n=len(s)
        
        counter=0
        for j in range(0,n-k+1):
            val=s[j:j+k]
            print(val)
            if int(val)!=0 and num%int(val)==0:
                counter+=1
        
        return counter



        