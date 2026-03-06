from typing import Optional, List
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:    
    def merge_two_lists(self, list1, list2) -> Optional[ListNode]:
        if not list1 and not list2:
            return None

        head = curr =  ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        curr.next = list1 or list2
        return head.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        head = lists[0]
        for i in range (1, len(lists)):
            head = self.merge_two_lists(head, lists[i])
        return head




