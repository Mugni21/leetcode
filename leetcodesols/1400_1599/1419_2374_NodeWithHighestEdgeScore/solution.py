#First solution was the first that came to mind. Create a dict counting the scores
#Then sort the score count first by the edge score and then by node index
#return first element
#This need nlog(n) for the sorting


class Solution:
    #def edgeScore(self, edges: List[int]) -> int:
        #score_count={}
        #for i, node in enumerate(edges):
            #if node not in score_count:
                #score_count[node]=i
            #else:
                #score_count[node]=score_count[node]+i
        #arr=list(score_count.keys())
        #arr.sort(key=lambda x: (-score_count[x],x))
        #return arr[0]

#Linear solution. We already know all nodes are in [0,1,...,n]
#so we can just traverse once and then traverse again in order and keep track 
#of the max edge score. As we are traversing from 0 to n, keeping track of the max will always keep the 
#smallest index with such max! 
    def edgeScore(self, edges: List[int]) -> int:
        n=len(edges)
        score_count=[0]*n
        for i, node in enumerate(edges):
            score_count[node]+=i
        
        maxi=-1
        maxi_node=0
        for node,score in enumerate(score_count):
            if score>maxi:
                maxi=score
                maxi_node=node
        
        return maxi_node
        