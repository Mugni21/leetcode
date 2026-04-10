#class Solution:
    #def differenceOfSums(self, n: int, m: int) -> int:
        #nondiv=0
        #div=0
        #for j in range(1,n+1):
            #if j % m != 0:
                #nondiv+=j
            #else:
                #div+=j
        
        #return nondiv-div
    
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        return n*(n+1)//2 - 2*m*(k*(k+1)//2)
        