from time import time
from random import randint,seed

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        m=len(blocks)-k+1
        miniwhites=k
        for i in range(m):
            currentwhites=blocks[i:i+k].count('W')
            if currentwhites<miniwhites:
                miniwhites=currentwhites
        
        return miniwhites
    
    def minimumRecolors2(self, blocks: str, k: int) -> int:
        currentwhites = blocks[:k].count('W')
        miniwhites = currentwhites

        for i in range(len(blocks) - k):
            if blocks[i] == 'W':
                currentwhites -= 1
            if blocks[i + k] == 'W':
                currentwhites += 1
            miniwhites = min(miniwhites, currentwhites)

        return miniwhites
            



seed(0)


inp = ["W", "B"]

SIZE = 100000 * 2 * 2
K = SIZE // 10

s = Solution()

blocks = "".join([inp[randint(0, 1)] for _ in range(SIZE)])

start = time()
ans = s.minimumRecolors(blocks, K)
end = time()
total = end - start

print(f"got answer {ans} in {total:.4f}s")

start = time()
ans = s.minimumRecolors2(blocks, K)
end = time()
total = end - start
print(f"got answer {ans} in {total:.4f}s for second algo")
