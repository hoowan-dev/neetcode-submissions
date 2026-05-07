# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2

        if list2 == None:
            return list1

        head = ListNode()
        if list1.val <= list2.val:
            head.val = list1.val
            list1 = list1.next
        else:
            head.val = list2.val
            list2 = list2.next

        next = head

        while list1 != None and list2 != None:
            next.next = ListNode()
            next = next.next
            if list1.val <= list2.val:
                next.val = list1.val
                list1 = list1.next
            else:
                next.val = list2.val
                list2 = list2.next

        while list1 != None:
            next.next = ListNode(list1.val)
            next = next.next
            list1 = list1.next

        while list2 != None:
            next.next = ListNode(list2.val)
            next = next.next
            list2 = list2.next  

        return head
