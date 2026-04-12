#Took me much longer thann it should, stupid indexing

class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        winsize=2*k+1
        if winsize>n:
            return [-1]*n
        if k==0:
            return nums

        suma=0
        avgs=[-1]*n
        for i in range(n-winsize+1):
            if i==0:
                suma=sum(nums[:winsize])
                avgs[k]=(int(suma/winsize))
            else:
                suma=suma-nums[i-1]+nums[winsize+i-1]
                avgs[k+i]=(int(suma/winsize))
    
        return avgs
            
            
                

        