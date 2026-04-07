class Solution:
 


    def convertDateToBinary(self, date: str) -> str:
        year=int(date[:4])
        month=int(date[5:7])
        day=int(date[8:])
        return str(bin(year)[2:])+'-'+str(bin(month)[2:])+'-'+str(bin(day)[2:])
        
        