class Solution:
    def minimumSum(self, num: int) -> int:
        numlist=[int(numi) for numi in str(num)]
        numlist.sort()
        new1=numlist[-1]*1+numlist[-3]*10
        new2=numlist[-2]*1+numlist[-4]*10
        return new1+new2