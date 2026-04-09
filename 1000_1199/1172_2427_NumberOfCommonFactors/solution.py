class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        comdiv=0
        for x in range(min(a,b)):
            if a % x==0 and b % x==0:
                comdiv+=1
        return comdiv

#It can be further optimized by onlu taking the range up to sqrt(g.c.d(a,b))+1...but either remember euclid to 
#calculate it or use import math and use math.gcd(a,b)