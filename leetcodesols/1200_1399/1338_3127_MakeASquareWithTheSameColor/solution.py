class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        word1=grid[0][0]+grid[0][1]+grid[1][0]+grid[1][1]
        countW1=word1.count('W')
        if countW1!=2:
            return True
        word2=grid[0][1]+grid[0][2]+grid[1][1]+grid[1][2]
        countW2=word2.count('W')
        if countW2!=2:
            return True
        word3=grid[1][0]+grid[1][1]+grid[2][0]+grid[2][1]
        countW3=word3.count('W')
        if countW3!=2:
            return True
        word4=grid[1][1]+grid[1][2]+grid[2][1]+grid[2][2]
        countW4=word4.count('W')
        if countW4!=2:
            return True
        return False

#Previous solution is kinda shitty. This is much cleaner (same idea)

#class Solution:
    #def canMakeSquare(self, grid: List[List[str]]) -> bool:
        for i in range(2):
            for j in range(2):
                Wcount = (
                    (grid[i][j] == 'W') +
                    (grid[i][j+1] == 'W') +
                    (grid[i+1][j] == 'W') +
                    (grid[i+1][j+1] == 'W')
                )
                if Wcount != 2:
                    return True
        return False

