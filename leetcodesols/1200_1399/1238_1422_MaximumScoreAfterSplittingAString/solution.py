class Solution:
    def maxScore(self, s: str) -> int:
        tot=0
        for k in range(len(s)-1):
            left=s[:k+1]
            right=s[k+1:]
            lefts=left.count('0')
            rights=right.count('1')
            score=lefts+rights
            if score>tot:
                tot=score
        return tot

##Cleaner solution. The first one has to split and count on each step, we can just split and keep track of the element we just split at
#to see if it adds or substracts to the score: 

#class Solution:
#    def maxScore(self, s: str) -> int:
        zeros = 0
        ones = s.count('1')
        best = 0

        for i in range(len(s) - 1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1

            best = max(best, zeros + ones)

        return best