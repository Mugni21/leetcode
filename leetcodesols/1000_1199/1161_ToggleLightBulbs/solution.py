class Solution:
    def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        counter={}
        for bulb in bulbs: 
            if bulb not in counter:
                counter[bulb]=1
            else:
                counter[bulb]+=1
        ons=[]
        for bulb in counter:
            if counter[bulb] % 2==1:
                ons.append(bulb)
        return sorted(ons)
        
#Beautiful solution:
#Instead of counting the parity of how the switch flips, simply add and remove from a set
#Only the ones who appear an odd number of times will be on the set in the end!
#Also, we can completely avoid sorting since we know the indices are in the range [1,100]
#We can simply list them from 1-100 in O(100) time!

#class Solution:
    #def toggleLightBulbs(self, bulbs: list[int]) -> list[int]:
        on = set()
        for b in bulbs:
            if b in on:
                on.remove(b)
            else:
                on.add(b)

        return [i for i in range(1, 101) if i in on]