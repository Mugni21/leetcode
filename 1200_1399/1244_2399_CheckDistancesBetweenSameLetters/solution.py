class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        #97
        for i in range(len(s)):
            for j in range(len(s)):
                if i !=j and s[i]==s[j]:
                    dist=abs(i-j)-1
                    num=ord(s[i])-97
                    if dist!=distance[num]:
                            return False
        
        return True

#Better version: Keep track of the elements we have already seen with a dictionary! We dont have to loop n^2 just n

#class Solution:
#    def checkDistances(self, s: str, distance: List[int]) -> bool:
        first = {}
        
        for i, ch in enumerate(s):
            if ch in first:
                if i - first[ch] - 1 != distance[ord(ch) - ord('a')]:
                    return False
            else:
                first[ch] = i
        
        return True