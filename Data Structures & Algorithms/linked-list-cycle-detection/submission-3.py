# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def twoPointers(self, p1, p2):
        if p1 == p2:
            return True
        if p2 is None or p2.next is None:
            return False
        return self.twoPointers(p1.next, p2.next.next)

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        return self.twoPointers(head, head.next)