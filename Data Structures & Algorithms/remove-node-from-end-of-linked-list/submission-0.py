# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # single case
        if n == 1 and not head.next:
            return None
        
        # get to the end
        curr = head
        length = 1
        while curr.next:
            length += 1
            curr = curr.next
        
        index = length - n + 1
        curr_index = 1
        curr = head
        prev = None

        while curr and curr_index < index:
            curr_index += 1
            prev = curr
            curr = curr.next
        
        # delete curr
        if prev:
            prev.next = curr.next
            return head
        else:
            return head.next
        
        # 1 -> 2 -> 3 -> 4 n = 4
        # curr = 1
        # prev = N
        # curr_index = 1
        # index = 1

        
