class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bina=bin(n)[2:]
        binop=''
        for i in bina:
            if i=='1':
                binop+='0'
            else:
                binop+='1'
        out=0
        k=0
        for j in reversed(binop):
            j=int(j)
            out+=j*2**(k)
            k+=1
        return out


#Cleaner Solution: int() already has a function to turn a binary string into an integer

#class Solution:
#    def bitwiseComplement(self, n: int) -> int:
        bina = bin(n)[2:]
        flipped = ''
        for ch in bina:
            if ch == '1':
                flipped += '0'
            else:
                flipped += '1'
        return int(flipped, 2)
    
#Even cleaner solution: do an xor with only 1's. That switches every bit to the opposite

#class Solution:
#    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        return n ^ ((1 << n.bit_length()) - 1)