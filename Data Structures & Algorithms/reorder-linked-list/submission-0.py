# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        curr_s = slow.next
        prev = slow.next = None
        while curr_s:
            temp = curr_s.next
            curr_s.next = prev
            prev = curr_s
            curr_s = temp

        curr1, curr2 = head, prev

        while curr1 and curr2:
            t1, t2 = curr1.next, curr2.next
            curr1.next = curr2
            curr2.next = t1
            curr1, curr2 = t1, t2
        
            


        

