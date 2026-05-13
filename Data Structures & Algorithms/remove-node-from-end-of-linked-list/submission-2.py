# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head.next == None:
            return None
        
        len = 0
        curr = head
        while curr:
            curr = curr.next
            len += 1

        target = len - n

        if target == 0:
            head = head.next
            return head

        curr = head
        prev = None
        for i in range(target):
            prev = curr
            curr = curr.next

        if curr:
            prev.next = curr.next
        else:
            prev.next = None

        return head
        '''
        r = head
        for i in range(n):
            r = r.next

        lPrev = None
        l = head

        while r:
            lPrev = l
            l = l.next
            r = r.next

        if l:
            lPrev.next = l.next
        else:
            lPrev.next = None

        return head
        '''