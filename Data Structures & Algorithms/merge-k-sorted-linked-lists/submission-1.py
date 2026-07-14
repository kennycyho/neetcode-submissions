# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeTwoLists(list1: ListNode, list2: ListNode) -> ListNode:
            dummy = ListNode()
            head = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            if not list1:
                head.next = list2
            if not list2:
                head.next = list1
            return dummy.next
        
        if len(lists) == 0:
            return None

        res = lists[0]
        for i in range(1, len(lists)):
            res = mergeTwoLists(res, lists[i])
        
        return res