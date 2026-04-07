class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        repeat=set()
        for i,v in enumerate(words):
            for j,w in enumerate(words):
                if i!=j and v in w:
                    repeat.add(v)
        return list(repeat)