class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sent=sentence.split()
        vows = {'a', 'e', 'i', 'o', 'u'}
        for i, word in enumerate(sent):
            if word[0].lower() in vows:
                new=word+'ma'+'a'*(i+1)
            else:
                new=word[1:]+word[0]+'ma'+'a'*(i+1)
            sent[i]=new
        return ' '.join(sent)
            



        