import heapq
import math

#First time using a heap. So a heap is just a list that is not fully sorted, but that
#makes it easy to always acces the smallest element. If we flip signs we can easily acces the largest element
#So we import heapq and heapq.heapify(List) just turns any number list into a heap
#Here we can now always acces the largest element at any time
#So at each second, we extract the largest element (this is heapq.heapop) this removes it from 
#the heap, so we do the neccesary operations to it, and we then put it inside the heap again
#with heapq.heappush(heap,element). This automatically again reorders the heap so we can 
#acccess the largest element at the next timestep. In the end we just add all the remaining things on 
#the heap.....It is still a list so it preserves all the list methods!

class Solution:

    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-x for x in gifts]
        heapq.heapify(gifts)

        for _ in range(k):
            largest=-heapq.heappop(gifts)
            reduced=-math.floor(largest**(1/2))
            heapq.heappush(gifts,reduced)
        return -sum(gifts)

      

        