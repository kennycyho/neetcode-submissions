# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        stack = []
        while head:
            stack.append(head)
            head = head.next
        
        rem = stack[-n]
        
        if n == len(stack):
            res = rem.next
            rem.next = None
            return res

        prev = stack[-n - 1]
        prev.next = rem.next
        rem.next = None
        return stack[0]