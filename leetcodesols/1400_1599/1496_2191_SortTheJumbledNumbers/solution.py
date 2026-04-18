class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        mapd={}
        for i,mapi in enumerate(mapping):
            mapd[str(i)]=str(mapi)
        mapped_nums=[]
        num_aux=[]
        for i, num in enumerate(nums):
            num_aux.append((num,i))

        def map_num(num):
            num=str(num)
            mapped_num=[mapd[ch] for ch in num]
            return int(''.join(mapped_num))

        num_aux.sort(key=lambda x: (map_num(x[0]),x[1]))
        nums=[num[0] for num in num_aux]
        return nums

#Even cleaner solution. So the dictionary was unnecessary. Also, python sorting preserves the original
#Order if there are ties, so there was no need to encode the position with the (value,index) idea above!
#Its the same idea, just cleaner. 

    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        def mapped_num(num):
                return int(''.join([str(mapping[int(ch)]) for ch in str(num)]))
        return sorted(nums,key=mapped_num)



