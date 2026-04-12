 #First sort by "its reachable or not, then sort by increasing tower quality
        #, then sort by lexicographic order of coordinates!"
        #Then if the first one is reachable return its coordinates, otherwise return [-1,-1]!

class Solution:
    #def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
       
        #towers.sort(key=lambda x : ((abs(x[0]-center[0])+abs(x[1]-center[1])>radius),
        #-x[2],
        #x[0],
        #x[1]))
        #first_tower=towers[0]
        #if abs(first_tower[0]-center[0])+abs(first_tower[1]-center[1])>radius:
            #return [-1,-1]
        #else:
            #return first_tower[:2]
        
    #Previous solution is O(n logn) because of sorting, we can just traverse the thing once
    #and just save the best up to that point. Less clean in my opinion, but more efficient!

    def bestTower(self, towers: List[List[int]], center: List[int], radius: int) -> List[int]:
        best_tower=[-1,-1]
        best_qual=-1
        cx,cy=center[0],center[1]
        for tower in towers: 
            manhattan=abs(tower[0]-cx)+abs(tower[1]-cy)
            quality=tower[2]
            coord=(tower[0],tower[1])
            if manhattan<=radius:
                if quality>best_qual:
                    best_tower=tower
                    best_qual=quality
                    best_coord=coord
                elif quality==best_qual:
                    if coord<best_coord:
                        best_tower=tower
                        best_qual=quality
                        best_coord=coord
        return [best_tower[0],best_tower[1]]

                    

                




        