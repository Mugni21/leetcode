import heapq
#Not optimal, but I'm having fun with heaps
class Solution:

    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxes=[(-uni,numbox) for numbox,uni in boxTypes]
        heapq.heapify(boxes)
        added=0
        while truckSize>0 and boxes:
            uni,numbox=heapq.heappop(boxes)
            if numbox>0:
                deleted=min(numbox,truckSize)
                truckSize-= deleted
                numbox-= deleted
                added-=uni*(deleted)
        return added
            





        