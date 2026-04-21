# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#Here I keep track of the state I am in with the boolean prev. If its true its because I am inside of
#A connected component for the first time, so I only add 1 to the connected components counter when I FIRST enter a new
#connected component. Otherwise I just keep traversing the linked list. When I exit a conected component
#I turn the boolean again to True, so that the next time I enter a connected component I add 1. 
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        nums_set={num for num in nums}
        link1=head
        cc=0
        prev=True
        while link1:
            if link1.val in nums_set and prev :
                cc+=1
                prev=False
            if link1.val not in nums_set:
                prev=True
            link1=link1.next
            
        return cc

            
        