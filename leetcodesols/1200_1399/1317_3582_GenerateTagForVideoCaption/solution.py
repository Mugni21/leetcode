class Solution:
    def generateTag(self, caption: str) -> str:
        captionlist=caption.split()

        if not captionlist:
            return "#"

        for i,word in enumerate(captionlist):
            captionlist[i]=word.lower().capitalize()
    
        caption_new=''.join(captionlist)

       
        caption_new='#'+caption_new[0].lower()+caption_new[1:]
       
         
        return caption_new[:100]

            
