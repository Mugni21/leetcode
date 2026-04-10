class Solution:

    #My crappy solution. I essentially count the frequency of each number first. The create a dictionary that
    #for each frequency stores a list that contains the elements that have that frequency on the original list. 
    #I sort those sublists in descending order (the ties in frquency are ordered in decreasing order)
    #Then I sort the frequencies and then I say that the output has to be the concatenation of the the elements of each
    #frequency now ordered in that descending order but multiplied by their oirignal frequency. So two, layers of sorting
    #First by their frequencies in ascending order and then for the ties in descending order
    def frequencySort(self, nums: List[int]) -> List[int]:
        #key:num, value:freq
        counts={}
        for i,k in enumerate(nums):
            if k not in counts: 
                counts[k]=1
            else:
                counts[k]+=1
        
        counts_list={}
        for freq in counts.values():
            counts_list[freq]=[num for num in counts if counts[num]==freq]
            counts_list[freq]=sorted(counts_list[freq],reverse=True)
        
        finalans=[]
        
        for freq in sorted(counts_list):
            for num in counts_list[freq]:
                finalans+=[num]*freq
        return finalans
    
    #Much better solution. Use a custom ordering. So we are going to create pairs (frequency,num)
    #Then we can define a lexigographic order on those pairs with a custom rule. First order them depending on 
    #frequency and if there are ties, sort them by descending order of the second coordinate
    #We can do this using nums.sort(key=lambda x: (function with the custom ordering ciretrion))
    #Se we are telling it to order a verctor x, by first ordering a transformation of that vector f(x)



    def frequencySort(self, nums: List[int])-> List[int]:
        counts={}
        for i,k in enumerate(nums):
            counts[k]=counts.get(k,0)+1

        #This is the cool part. First sort them by frequency (counts) and then the funciton x \mapsto -x simply
        #reverses the order!
        nums.sort(key=lambda x : (counts[x],-x))
        return nums
        



        
                


            


        
        