# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        has_seen = set()
        while head.next:
            if head not in has_seen:
                has_seen.add(head)
                head = head.next
            else:
                return True
        return False
        