# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = p2 = head
        for i in range(n):
            p2 = p2.next
        
        prev = None
        while p2:
            prev = p1
            p1 = p1.next
            p2 = p2.next
        
        #p1 = node to remove
        if prev is not None:
            prev.next = p1.next
        if p1 is head:
            head = p1.next
        p1.next = None

        return head