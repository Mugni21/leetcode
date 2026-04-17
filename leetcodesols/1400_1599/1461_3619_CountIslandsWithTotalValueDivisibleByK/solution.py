from collections import deque
class Solution:
    #First solution. Works but is very slow. I first scan all potential starting points and then do BFS for each of them. Inside 
    #Each BFS I update the states I have already visited so we don't repeat, so I keep updating the set of
    #"unexplored" states at every point. 
    def countIslands(self, grid: List[List[int]], k: int) -> int:

        m=len(grid)
        n=len(grid[0])
        num_islands=0

        def son_gen(i,j,m,n):
            dirs=[(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            valid_dirs=[dir for dir in dirs if 0<=dir[0]<m and 0<=dir[1]<n]
            return valid_dirs


        unexplored=set()
        for i in range(m):
            for j in range(n):
                if grid[i][j]!=0:
                    unexplored.add((i,j))

        
        while unexplored:
            node=unexplored.pop()
            q=deque([node])
            current_sum=0
            current_island={node}
            while q:

                node=q.popleft()
                sons=son_gen(node[0],node[1],m,n)
                current_sum+=grid[node[0]][node[1]]
                current_island.add(node)
                unexplored.discard(node)
                
                for son in sons:
                    value=grid[son[0]][son[1]]
                    if value!=0 and (son[0],son[1]) not in current_island:
                        current_island.add((son[0],son[1]))
                        q.append((son[0],son[1]))

            if current_sum%k==0:
                num_islands+=1
        
        return num_islands
    

    #Second much faster solution. Now we just keep track of the visited states by updateing the matrix. So now we explore
    #the matrix and do BFS for "valid" starting point instead of finding all the starting points from the start
    #This also avoids repetating so many operations on sets ,since now I update the original matrix in place. 

    from collections import deque

class Solution:
    
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m=len(grid)
        n=len(grid[0])
        islands=0

        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    grid[i][j]=-2
                elif grid[i][j]!=-2:
                    current_sum=grid[i][j]
                    grid[i][j]=-2
                    q=deque([(i,j)])
                    while q: 
                        node=q.popleft()
                        x,y=node
                        #Up
                        if x+1<m and grid[x+1][y]>0:
                            q.append((x+1,y))
                            current_sum+=grid[x+1][y]
                            grid[x+1][y]=-2
                        #dow
                        if 0<=x-1 and grid[x-1][y]>0:
                            q.append((x-1,y))
                            current_sum+=grid[x-1][y]
                            grid[x-1][y]=-2
                        #left
                        if 0<=y-1 and grid[x][y-1]>0:
                            q.append((x,y-1))
                            current_sum+=grid[x][y-1]
                            grid[x][y-1]=-2
                        #right
                        if y+1<n and grid[x][y+1]>0:
                            q.append((x,y+1))
                            current_sum+=grid[x][y+1]
                            grid[x][y+1]=-2
                    if current_sum%k==0:
                        islands+=1
        return islands




        
            