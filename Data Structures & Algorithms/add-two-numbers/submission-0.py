# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            head = ListNode()
            current = head

            while l1 is not None or l2 is not None:
                l1_val = 0
                if l1 is not None:
                    l1_val = l1.val
                    l1 = l1.next

                l2_val = 0
                if l2 is not None:
                    l2_val = l2.val
                    l2 = l2.next

                sum = l1_val + l2_val + current.val
                current.val = sum % 10
                carry = 1 if (sum > 9) else 0
                
                if l1 is not None or l2 is not None or carry == 1:
                    next = ListNode(carry)
                    current.next = next
                    current = next

            return head

        