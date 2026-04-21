class Solution:
    def minFlips(self, target: str) -> int:
        flips = 0
        expected = '0'
        
        for ch in target:
            if ch != expected:
                flips += 1
                expected = ch
        
        return flips