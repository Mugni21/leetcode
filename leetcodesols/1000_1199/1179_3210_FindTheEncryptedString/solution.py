class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        n=len(s)
        new=''.join([s[(i+k)%n] for i in range(n)])
        return new
        