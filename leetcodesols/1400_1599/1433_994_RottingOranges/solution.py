#This one took me super long. First time implementing BFS. I had the right idea conceptaully just didnt know how
#to code it. 

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        #Initial list to keep track of fresh and rotten oranges at time t=0
        rotten = []
        orange = []

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    orange.append((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))

        #Check easy cases first

        if len(rotten) == 0 and len(orange) > 0:
            return -1

        if len(orange) == 0:
            return 0
        
        #Now we are going to do BFS!! So the initial block in the queue are all the rotten oranges
        q = deque()
        #Here I will store the time it took for reached fresh oranges to be infected
        #As we are doping BFS simultaneosly for all rotten orange, this will be the smallest
        #time it took for the fresh orange to be infected (independent of from which original
        #rotten  orange it was infected from )
        time_reached = {}
        
        #First the first depth block of the BFS are the rotten oranges,
        #they are reached at time 0 (I think this is irrelevant but anyways)

        for rot in rotten:
            q.append(rot)
            time_reached[rot] = 0
        
        #This are the possible moves

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        #Now BFS, so while the queue is non empty we keep exploring level by level

        while q:
            #Take the first node on the queue and remove it
            r, c = q.popleft()
            #On the first step the time reached will be 0 for the inital rotten oranges
            t = time_reached[(r, c)]

            #Now for a fixed node, we explore all possible directions

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                #Check if they are valid points on the grid first

                if 0 <= nr < rows and 0 <= nc < cols:
                    #If it was a fresh orange we infect it! And the time reached will be t+1
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        time_reached[(nr, nc)] = t + 1
                        #Then we add it to the queue
                        q.append((nr, nc))

        #After exploring the entire thing, the number of infected fresh oranges
        #Will be the size of the dictionary of reached times minus the initial rotten ones we added
        #with time 0
        infected_fresh = len(time_reached) - len(rotten)
        #If there are less infected fresh ones that initial fresh ones then at least one fresh one was 
        #never infected and we return -1
        if infected_fresh != len(orange):
            return -1
        
        #Else if all the fresh ones were infected, we return the time of the one that toolk
        #the longest!

        return max(time_reached.values())