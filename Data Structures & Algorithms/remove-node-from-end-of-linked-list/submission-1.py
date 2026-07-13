# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
        
        idx = size - n
        if idx == 0:
            return head.next

        curr = head
        for i in range(0, idx):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        return head