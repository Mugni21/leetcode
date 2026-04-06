class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counters=[0]*(max(arr)+1)
        for v in arr:
            counters[v]+=1
        #range(start,stop (NOT included), step)
        #so we dont count the 0 (only positive intries admitted) and -1
        #traverses the list backwards
        for i in range(len(counters)-1,0,-1):
            if counters[i]==i:
                return i
        else:
            return -1