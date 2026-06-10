class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        m=n-1
        inte=time//m
        rem=time%m
        if inte%2==0:
            return rem+1
        else:
            return n-rem


