class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        n=len(batteryPercentages)
        tested=0
        for i,k in enumerate(batteryPercentages):
            if k>0:
                tested+=1
                for j in range(i+1,n):
                    batteryPercentages[j]=max(0,batteryPercentages[j]-1)
        return tested
            

#Cleaner solution O(n). We are not going to decreasde the battery of all the following ones after we test. 
#We will just keep track of how many we have tested up to point i. If the initial battery minus the amount of tests
#is positive, then we test again. If not, we dont test!

#class Solution: 
    #def countTestedDevices(self, batteryPercentages: List[int])-> int: 
        n=len(batteryPercentages)
        tested=0
        for i,k in enumerate(batteryPercentages):
            if k>tested: 
                tested+=1
        return tested

        