class Solution:

    def isgood(self, s: str)-> bool:
            for k in range(len(s)-1):
                if s[k].swapcase()==s[k+1]:
                    return False
            return True
    def makeGood(self, s: str) -> str:
        while not self.isgood(s):
            for k in range(len(s)-1):
                if not self.isgood(s[k:k+2]):
                    s=s[:k]+s[k+2:]
    
        return s

#much much better solution. Use a "stack". We start filling the word "left to right" character by character. 
#We check if we have added a bad pair everytime we add a new character!

class Solution:

 def makeGood(self, s: str) -> str:
    result = []

    for c in s:
        if result and result[-1].swapcase() == c:
            result.pop()   # remove last character
        else:
            result.append(c)  # keep this character

    return ''.join(result)


            

                

        

            

                

        