class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val > list2.val:
            head = list2
            curr = list2
            other = list1
        else:
            head = list1
            curr = list1
            other = list2

        while curr and other:
            nxt = curr.next
            
            if nxt and nxt.val <= other.val:
                curr = nxt
            else:
                curr.next = other
                curr = other
                other = nxt

        return head