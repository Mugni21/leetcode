# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


#First time solving a linkedlist proble. Fun
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        #Here tail1 is the tail of list 1 from node b+1 until the end of list1
        tail1=list1
        for i in range(b+1):
            tail1=tail1.next

        #Here endlist2 is just the last node of list2
        endlist2=list2
        while endlist2.next:
            endlist2=endlist2.next
        
            
        #Then I tell list2 that its new tail is the tail we just cut from tail1
        #So now the last pointer of list2 is "attached" to the tail of list1 from 
        #the previous operation
        endlist2.next=tail1

        #Now here, I extract the node a-1 from list1
        endblist1=list1
        for j in range(a-1):
            endblist1=endblist1.next
        
        #Now attach to the node a-1 of list 1, endlist2 which includes list2 and the tail of list
        #1
        endblist1.next=list2

        return list1


        
        