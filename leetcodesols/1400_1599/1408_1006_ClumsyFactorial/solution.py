class Solution:
    def clumsy(self, n: int) -> int:
        stack=[n]
        op=0
        n-=1

        while n>0:
            if op==0:
                stack[-1]=stack[-1]*n
            elif op==1:
                stack[-1]=int(stack[-1]/n)
            elif op==2:
                stack.append(n)
            elif op==3:
                stack.append(-n)

            op= (op+1) % 4
            n-=1
        
        return sum(stack)


        