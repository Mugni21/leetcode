class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        subm=[]
        for i in range(k):
            row=[]
            for j in range(k):
                row.append(grid[i+x][j+y])
            subm.append(row)
        
        subm.reverse()

        for i in range(k):
            for j in range(k):
                grid[i+x][j+y]=subm[i][j]
        
        return grid
                
#Better solution: replace the entries in place instead of creating a new submatrix+swapping+reinserting submatrix: 

#class Solution:
#    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
#        for i in range(k // 2):
#            top = x + i
#            bottom = x + k - 1 - i#
#
#            for j in range(y, y + k):
#                grid[top][j], grid[bottom][j] = grid[bottom][j], grid[top][j]

#        return grid