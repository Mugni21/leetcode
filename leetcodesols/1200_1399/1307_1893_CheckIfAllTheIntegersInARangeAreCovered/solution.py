class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        interval=set(range(left,right+1))
        for l,r in ranges:
            for num in range(left,right+1):
                if l<=num<=r:
                    interval.discard(num)
                if not interval:
                    return True
        return False

        