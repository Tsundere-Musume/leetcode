from typing import Optional
from collections import defaultdict
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        seen =  defaultdict(lambda : Node(-1))
        h = curr = head
        while curr:
            node = seen[curr]
            node.val = curr.val
            if curr.next:
                node.next = seen[curr.next]
            if  curr.random:
                node.random = seen[curr.random]
            curr = curr.next
        return seen[h]





        
