from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = curr =  ListNode()
        while carry  or (l1 and l2):
            s  = carry
            if l1:
                s += l1.val
                l1 = l1.next
            if l2:
                s += l2.val
                l2 = l2.next
            carry = 0 if s < 10 else 1
            curr.next = ListNode(s % 10)
            curr = curr.next
        curr.next = l1 or l2
        return dummy.next




        
