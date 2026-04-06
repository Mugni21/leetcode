class Solution:
    def sumAndMultiply(self, n: int) -> int:
        if n==0:
            return 0
        else:
            z=list(str(n))
            for _ in range(z.count('0')):
                z.remove('0')
            x=''
            xsum=0
            for v in z:
                x+=v
                xsum+=int(v)
            return int(x)*xsum
            
#Cleaner solution we create the list of dignits without the 0 in one step

#class Solution:
#    def sumAndMultiply(self,n:int)->int:
        digits=[ch for ch in str(n) if ch != '0']
        if not digits:
            return 0
        #.join glues together a list of strings with whatever we put on front, in this case '' empty string just glues the entries
        #digits
        x=''.join(digits)
        xsum=sum(int(digit) for digit in digits)
        return int(x)*xsum

        
                
            
