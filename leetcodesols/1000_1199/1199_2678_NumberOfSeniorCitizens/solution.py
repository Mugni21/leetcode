class Solution:
    def countSeniors(self, details: List[str]) -> int:
        counter=0
        for i,v in enumerate(details):
            age=int(v[11:13])
            if age>60:
                counter+=1
        return counter

            
