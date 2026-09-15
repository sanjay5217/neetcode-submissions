# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_head = ListNode()
        m_curr = merged_head

        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                m_curr.next = curr1
                curr1 = curr1.next
            else:
                m_curr.next = curr2
                curr2 = curr2.next

            m_curr = m_curr.next

        if curr1 is None and curr2:
            m_curr.next = curr2
        elif curr2 is None and curr1:
            m_curr.next = curr1
        
        return merged_head.next

    

