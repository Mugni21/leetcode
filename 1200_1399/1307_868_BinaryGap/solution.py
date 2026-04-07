class Solution:
    def binaryGap(self, n: int) -> int:
        bina=bin(n)[2:]
        L=len(bina)
        for dist in range(L-1,0,-1):
            subs='1'+'0'*(dist-1)+'1'
            if subs in bina:
                return dist
        return 0

#I basically start with the largest possible string of the form '100...001' where we have dist-1 zeros inside (also considering the case)
#of 0 0's and then check if that substring is in our string. 

#An even cleaner solution is just save the indices where the 1's appear like p_1<p_2<...<p_k. Then, the maximum gap is simply
#max_j |p_i-p_{i+1}|