class Solution:
    #Nasty solution. Just brute forcing and removing edge cases.....I don''t think there's much
    #Improvement room........
    #The only room for imporovement is that there are exactly 8 unique 3x3 magic squares. 
    #So we could store them all in a set and check if our subgrids are there....but it's kind of cheating
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        if m<3 or n<3:
            return 0

        def isMS(grid,k,l):

            if grid[1+k][1+l]!=5:
                return False

            counter={}
            for i in range(3):
                for j in range(3):
                    counter[grid[i+k][j+l]]=counter.get(grid[i+k][j+l],0)+1
                    if grid[i+k][j+l]>9 or grid[i+k][j+l]<1:
                        return False
            if len(counter)!=9:
                return False

            for i in range(3):
                current=0
                for j in range(3):
                    current+=grid[i+k][j+l]
                if current!=15:
                    return False
            for j in range(3):
                current=0
                for i in range(3):
                    current+=grid[i+k][j+l]
                if current!=15:
                    return False
            current=0
            current2=0
            for i in range(3):
                current+=grid[i+k][i+l]
                current2+=grid[2-i+k][i+l]
            if current!=15 or current2!=15:
                return False
            return True
        magic=0
        for i in range(m-2):
            for j in range(n-2):
                if isMS(grid,i,j)==True:
                    magic+=1
        return magic




            