# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp_list=[]
        while head.next:
            temp_list.append(head.val)
            head=head.next
        temp_list.append(head.val)
        
        max_sum=0
        m=len(temp_list)
        for i in range(int(m/2)):
            if temp_list[i]+temp_list[(m-1)-i]>max_sum:
                max_sum=temp_list[i]+temp_list[(m-1)-i]
        
        return max_sum

#So apparently my solution is optimal in time, not in space, since I have to duplicate using my 
#temp_list. There is an approach using "fast" and "slow" pointers. The slow one traverses the linked
#list by skipping one node, so when we let both pointers traverse the list. When, the fast one reaches the end
#the slow one would be exactly in the middle. So then we can reverse the last one and start comparing it
#with the first one......I want to internalize reversing a linked list before trying this. But here's the
#idea: 

#class Solution:
    #def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head

        # Find middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse second half starting at slow
        prev = None
        curr = slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # prev is now head of reversed second half
        max_sum = 0
        first = head
        second = prev

        while second:
            max_sum = max(max_sum, first.val + second.val)
            first = first.next
            second = second.next

        return max_sum