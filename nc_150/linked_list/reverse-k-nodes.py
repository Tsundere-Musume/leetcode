from typing import Optional
# Definition for singly-lined list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        n_item = 0  # size of the linked list
        curr = head

        # get the size
        while curr:
            n_item += 1
            curr = curr.next

        remaining = n_item
        first = True
        curr = head
        last_tail = None
        while remaining >= k: 
            last = None
            tail = curr
            n = k
            remaining -= k
            while curr and n > 0: 
                temp = curr.next                             # 1 2 3 4 5 6 | 2 1 4 3 6 5 
                curr.next= last 
                last = curr 
                curr = temp
                n -= 1
            if last_tail:
                last_tail.next = last
                print(last_tail.val)
            last_tail = tail
            if first:
                new_head = last
                first= False
        tail.next = curr
        return new_head

