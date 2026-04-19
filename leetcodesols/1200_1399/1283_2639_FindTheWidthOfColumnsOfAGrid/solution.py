class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:

        m=len(grid)
        n=len(grid[0])
        maxis=[]

        for j in range(n):
            max_col=0
            for i in range(m):
                if len(str(grid[i][j]))>max_col:
                    max_col=len(str(grid[i][j]))
            maxis.append(max_col)
        
        return maxis
            


        