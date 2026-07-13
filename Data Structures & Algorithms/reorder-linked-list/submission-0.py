# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverse (self, head):
        if head is None or head.next is None:
            return head
        new_head = self.reverse(head.next)
        next = head.next
        next.next = head
        head.next = None
        return new_head

    def merge(self, node1, node2):
        'Merge starting from node1'
        if node1 is None:
            return node2
        if node2 is None:
            return node1
        node1.next = self.merge(node2, node1.next)
        return node1


    def reorderList(self, head: Optional[ListNode]) -> None:
        if head is None:
            return head
        #slow/fast pointer - once fast reaches end, slow is at halfway point
        p1 = p2 = head
        while p2 is not None and p2.next is not None:
            p1 = p1.next
            p2 = p2.next.next
        
        #reverse list from slow_p +1
        reversed_half = self.reverse(p1.next)
        p1.next = None
        #merge original head and reversed head
        self.merge(head, reversed_half)