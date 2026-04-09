class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        pec=len(arr)//4
        for elem in arr:
            if arr.count(elem)>=pec:
                return elem


#Better sol: Just check if arr[i]==arr[i+len(s)//4] for some i! Linear time

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        k = n // 4

        for i in range(n - k):
            if arr[i] == arr[i + k]:
                return arr[i]