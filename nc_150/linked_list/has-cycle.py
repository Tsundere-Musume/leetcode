class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seenNodes = set()
        curr = head
        while curr:
            if curr in seenNodes:
                return True
            seenNodes.add(curr)
            curr = curr.next
        return False

        
