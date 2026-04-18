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

#First I gave the standard brute force solution: just check every 3x3 window independently.
#It’s already O(mn) since the window is fixed size, so nothing wrong with it.

#Then I tried something more structural. Idea was to exploit symmetry/overlap:
#If a 3x3 square is magic and we slide one step to the right, the new square shares
#two columns. That forces the third column to match the first one of the previous square,
#so we can "propagate" magic squares horizontally by just checking column equality.
#Same idea vertically with rows.

#This almost works: rows and columns sums are preserved under this cyclic shift.
#BUT diagonals are not invariant under this symmetry, so the propagation breaks.
#You can satisfy all row/column constraints and still fail the diagonals (counterexample exists).

#So in the end, the propagation idea is mathematically nice but not sufficient,
#and we fall back to the clean brute force check. STILL NICE EXCERCISE!!!



#class Solution:
    #def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if m < 3 or n < 3:
            return 0

        def is_magic(r, c):
            vals = [grid[r + i][c + j] for i in range(3) for j in range(3)]
            if set(vals) != set(range(1, 10)):
                return False

            for i in range(3):
                if sum(grid[r + i][c + j] for j in range(3)) != 15:
                    return False

            for j in range(3):
                if sum(grid[r + i][c + j] for i in range(3)) != 15:
                    return False

            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15:
                return False

            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15:
                return False

            return True

        def right_propagates(r, c):
            # from window (r,c-1) to window (r,c)
            for i in range(3):
                if grid[r + i][c + 2] != grid[r + i][c - 1]:
                    return False

            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15:
                return False

            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15:
                return False

            return True

        def down_propagates(r, c):
            # from window (r-1,c) to window (r,c)
            for j in range(3):
                if grid[r + 2][c + j] != grid[r - 1][c + j]:
                    return False

            if grid[r][c] + grid[r + 1][c + 1] + grid[r + 2][c + 2] != 15:
                return False

            if grid[r][c + 2] + grid[r + 1][c + 1] + grid[r + 2][c] != 15:
                return False

            return True

        magic = [[False] * (n - 2) for _ in range(m - 2)]

        magic[0][0] = is_magic(0, 0)

        for c in range(1, n - 2):
            if magic[0][c - 1] and right_propagates(0, c):
                magic[0][c] = True
            else:
                magic[0][c] = is_magic(0, c)

        for r in range(1, m - 2):
            if magic[r - 1][0] and down_propagates(r, 0):
                magic[r][0] = True
            else:
                magic[r][0] = is_magic(r, 0)

            for c in range(1, n - 2):
                if magic[r][c - 1] and right_propagates(r, c):
                    magic[r][c] = True
                else:
                    magic[r][c] = is_magic(r, c)

        return sum(sum(row) for row in magic)


            