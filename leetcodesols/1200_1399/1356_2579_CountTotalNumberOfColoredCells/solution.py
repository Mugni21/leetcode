class Solution:
    def coloredCells(self, n: int) -> int:
        if n==1:
            return 1
        base=5
        new=0
        for j in range(3,n+1):
            new+=4+4*(j-2)
        return new+base

#Even cleaner, just cleaning the fomula: 

#class Solution:
    #def coloredCells(self, n: int) -> int:
        ans = 1
        for k in range(1, n):
            ans += 4 * k
        return ans

#Even cleaner, thats just sum up to n: 
#class Solution:
    #def coloredCells(self, n: int) -> int:
        return 1 + 2 * n * (n - 1)

            