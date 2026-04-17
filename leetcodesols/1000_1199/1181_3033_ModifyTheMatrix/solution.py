class Solution:
    def modifiedMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m=len(matrix)
        n=len(matrix[0])
        targets=[]
        maxis=[]
        for j in range(n):
            maxi=-2
            for i in range(m):
                if matrix[i][j]>=maxi:
                    maxi=matrix[i][j]
                if matrix[i][j]==-1:
                    targets.append([i,j])
            maxis.append(maxi)
        for i,j in targets:
            matrix[i][j]=maxis[j]
        
        return matrix
            
