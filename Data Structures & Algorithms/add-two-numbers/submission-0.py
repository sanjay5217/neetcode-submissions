# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # 9922 + 879 = 4801
        # 2 -> 2 -> 9 -> 9 -> ....
        # 9 -> 7 -> 8
        # 11 -> 9 -> 17 -> 9 -> ....
        res = ListNode()
        curr = res
        carry = 0

        while l1 or l2 or carry != 0:
            if l1: curr1 = l1.val
            else: curr1 = 0
            if l2: curr2 = l2.val
            else: curr2 = 0

            value = curr1 + curr2 + carry
            carry = value // 10
            value = value % 10
            curr.next = ListNode(value)

            curr = curr.next 
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return res.next

                


