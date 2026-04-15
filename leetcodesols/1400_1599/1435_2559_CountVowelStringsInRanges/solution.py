class Solution:
    #I created a set with vowels and then checked if each word in words ended and started with a vowel
    #(looking up in dictionary is O(1)). I calculated the cumulative sum of all valid words we had seen
    #up to that point, including that point. 
    #Then, to know how many valid words we have seen in a given range (for each query), we simply
    #substract how many we have seen at the end of the query minus how many we have ssen up to the start of the
    #query!
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n=len(words)
        valid=[]
        vows=set()
        for vow in ['a','e','i','o','u']:
            vows.add(vow)
        
        cumsum=0
        for i,word in enumerate(words): 
            if (word[-1] in vows) and (word[0] in vows):
                cumsum+=1
                valid.append(cumsum)
            else: 
                valid.append(cumsum)

        
        q_len=len(queries)
        ans=[0]*q_len
        for i,query in enumerate(queries):
            init=query[0]
            end=query[1]
            if init!=0:
                ans[i]=valid[end]-valid[init-1]
            else:
                ans[i]=valid[end]
        return ans



    
        