class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def countpeaks(self, num: int):
            nums=str(num)
            peaks=0
            valleys=0
            for k in range(len(nums)-2):
                if int(nums[k])<int(nums[k+1])>int(nums[k+2]):
                    peaks+=1
                if int(nums[k])>int(nums[k+1])<int(nums[k+2]):
                    valleys+=1

            return peaks+valleys
    
        wavy=0

        for k in range(num1,num2,1):
            wavy+=countpeaks(k)
        
        return wavy


#COuldn't come up with anything better than brute force






    

        

