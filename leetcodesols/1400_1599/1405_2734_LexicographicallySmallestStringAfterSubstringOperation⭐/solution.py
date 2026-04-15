class Solution:
    #Super simple solution. Just skip the a's that are like a prefix, and change everyuthing until you see the
    #next a again! 
    #If the tdring was just a's, then onluy change the last 'digit'. 


    ###REMEMBER: ord() converts a character into an integer (given my some mysterious bijection)
    #then chr() converst an integer into a character using the inverse of that mysterious bijection again

    def smallestString(self, s: str) -> str:
        n=len(s)
        i=0
        while i<n and s[i]=='a':
            i+=1
        
        if i==n:
            s=s[:-1]+'z'
            return s
        news=s[:i]
        
        while i<n and s[i]!='a':
            news+=chr(ord(s[i])-1)
            i+=1
        news+=s[i:]

        return news

        





        

        

    

                 
        