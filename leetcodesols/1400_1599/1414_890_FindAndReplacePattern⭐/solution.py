class Solution:
    #Liked this solution. So I tried to define an invariant that uniquely determines the structure of the string
    #independent of what actual characters are in it. Its an so for example the string 'abb' gets mapped into
    #[0, 1, 1] and the string 'mee' also gets mapped into [0, 1, 1]. If those two representation are equal
    #then there exists a permutation that makes those two words the same. 
    #All we care about is that that underslying structure is the same, not the actual characters in it.
    #I think its optimal in time complexity btw
    #For example 'dkd' would not be equivalent to 'aab' because 'dkd' has representation
    #[0, 1, 0]
    
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        #This one "encrypts" the string, or calculates that invariant representation
        def encrypt(self, word: str)-> List[int]:
            crypto_list=[]
            counter={}
            i=0
            for ch in word:
                if ch not in counter:
                    counter[ch]=i
                    crypto_list.append(i)
                else:
                    crypto_list.append(counter[ch])
                i+=1
            return crypto_list
        #Then check for each word on the list if they have the same invariant representation
        #as target
        pattern_arr=encrypt(self, pattern)
        matches=[]
        for word in words:
            if encrypt(self, word)==pattern_arr:
                matches.append(word)
        return matches
    


        