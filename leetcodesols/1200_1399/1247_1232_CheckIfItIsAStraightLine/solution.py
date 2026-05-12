class Solution:
    # def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    #     m=len(coordinates)
    #     if m<3:
    #         return True
        
    #     x1,y1=coordinates[0][0], coordinates[0][1]
    #     x2,y2=coordinates[1][0], coordinates[1][1]
    #     counter=0
    #     for x,y in coordinates:
    #         if x==x1:
    #             counter+=1
    #     if counter==m:
    #         return True
    #     if x2==x1:
    #         return False
    #     slope=(y2-y1)/ (x2-x1)
    #     b=y1-slope*x1
    #     for x,y in coordinates[2:]:
    #         if y!=slope*x+b:
    #             return False
    #     return True
    

    #Cleaner sol
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n=len(coordinates)
        if n<3:
            return True
        x1, y1= coordinates[0][0], coordinates[0][1]
        x2, y2= coordinates[1][0], coordinates[1][1]

        #To avoid division, we check if slope from (x,y) to (x1,y1) is the same as the 
        #slope from (x2,y2) to (x1,y1) for all points. 

        for x,y in coordinates:
            if (y-y1)*(x2-x1)!=(y2-y1)(x-x1):
                return False
        return True
     


    
    
    

    
        