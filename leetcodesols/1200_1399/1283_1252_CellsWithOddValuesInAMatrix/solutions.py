class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix=[[0]*n for j in range(m)]
        for r,c in indices:
            for i in range(m):
                matrix[i][c]+=1
            for j in range(n):
                matrix[r][j]+=1
        counter=0
        for i in range(m):
            for j in range(n):
                counter+=(matrix[i][j])%2
        return counter
    