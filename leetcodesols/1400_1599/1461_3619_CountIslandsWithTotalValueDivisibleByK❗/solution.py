class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        islands=[]
        m=len(grid)
        n=len(grid[0])
        def dirs(i,j,m,n):
            dirs=[(i+1,j),(i-1,j),(i,j-1),(i,j+1)]
            valid_dirs=[dir for dir in dirs if  ((0<=dir[0]<m) and (0<=dir[1]<n))]
            return valid_dirs

    

        for i in range(m):
            for j in range(n):
                center=grid[i][j]
                if center!=0:
                    island_counter=len(islands)
                    for q,island in enumerate(islands):
                        if (i,j) in island:
                            island_counter-=1
                            sons=dirs(i,j,m,n)
                            for son in sons:
                                if grid[son[0]][son[1]]!=0:
                                    islands[q].add((son[0],son[1]))
                       
                                
            

                    if island_counter==len(islands):
                        new_set=set()
                        new_set.add((i,j))
                        sons=dirs(i,j,m,n)
                        for son in sons:
                            if grid[son[0]][son[1]]!=0:
                                new_set.add((son[0],son[1]))
                        islands.append(new_set)
        good_islands=0
        
        for island in islands:
            island_sum=0
            for element in island:
                value=grid[element[0]][element[1]]
                island_sum+=value
            if island_sum%k==0:
                good_islands+=1
        
        return good_islands
                   
                   
                       
                            




                    




        