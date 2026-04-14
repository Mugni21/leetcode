class Solution:
    def vowelConsonantScore(self, s: str) -> int:
        counter={}
        for char in s:
            counter[char]=counter.get(char,0)+1
        vowels=['a','e','i','o','u']
        consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
        v=0
        for vowel in vowels:
            if vowel in counter:
                v+=counter[vowel]
        
        c=0
        for cons in consonants:
            if cons in counter:
                c+=counter[cons]

        if c>0:
            return v // c
        else:
            return 0

        