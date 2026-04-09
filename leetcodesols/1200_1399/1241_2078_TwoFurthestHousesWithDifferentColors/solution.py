class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        maxi=0
        for i in range(len(colors)):
            for j in range(len(colors)):
                if colors[i] != colors[j]:
                    dist=abs(i-j)
                    if dist>maxi:
                        maxi=abs(i-j)
        return maxi
