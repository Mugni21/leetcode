class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n=len(code)
        edited=[0]*n
        if k==0:
            return edited
        elif k>0:
            for j in range(n):
                suma=0
                for i in range(k):
                    suma+=code[(j+i+1)%n]
                edited[j]=suma
            return edited
        else:
            print('yes')
            for j in range(n):
                suma=0
                for i in range(-k):
                    suma+=code[(j-(i+1))%n]
                edited[j]=suma
            return edited
        

        