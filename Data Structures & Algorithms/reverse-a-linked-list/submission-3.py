# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        shit = None
        piss = head

        while piss:
            cum = piss.next
            piss.next = shit
            shit = piss
            piss = cum

        return shit