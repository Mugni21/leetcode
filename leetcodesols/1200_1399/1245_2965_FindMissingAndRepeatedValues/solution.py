class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        #I find the double counted one using a set and then solve for a using an auxiliary equation!
        f=sum(grid, [])
        seen=set()
        n=len(f)
        rho=(n*(n+1))/2
        gamma=sum(i for i in f)
        for x in f:
            if x in seen:
                a=x
                break
            seen.add(x)
        b=rho-gamma+a
        return [a,int(b)]

#Even nicer solution: create two auxiliary equation, one with the sums of elements and another one with the sums of squares
#of the list f and the list [1,...,n^2] that gives a 2x2 linear system that can be solved for a,b !!