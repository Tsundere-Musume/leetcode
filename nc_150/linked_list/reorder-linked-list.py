class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        last = None
        while second:            
            temp = second.next
            second.next = last
            last = second
            second = temp

        turn = True
        dummy = node =  ListNode()
        while head and last:
            if turn:
                node.next = head
                head = head.next
            else:
                node.next = last
                last = last.next
            turn = not turn
            node = node.next

        node.next = head or last



        
