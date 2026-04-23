#First I thought in terms of "states" this reminded me of another problem I solved that had the 
#exact same architecture, but its a bit overengineered. Its a state machine

class Solution:
    def partitionString(self, s: str) -> int:
        n=len(s)
        j=0
        exploring=False
        ss=0
        current_seen=set()
        while j<n:
            if exploring==True:
                if s[j] not in current_seen:
                    current_seen.add(s[j])
                else:
                    exploring=False

            if exploring==False:
                current_seen=set()
                current_seen.add(s[j])
                ss+=1
                exploring=True
            j+=1
        
        return ss

#Exact same idea but much simpler:


    #def partitionString(self, s: str) -> int:
        n=len(s)
        j=0
        ss=1
        current_seen=set()
        while j<n:
            if s[j] not in current_seen:
                current_seen.add(s[j])
            else:
                current_seen=set()
                current_seen.add(s[j])
                ss+=1
            j+=1
        return ss




           

      





        
           

      





        