# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def getLength(self, head: Optional[ListNode]) -> int:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        return length

    def reverseSublist(self, start: Optional[ListNode], k: int) -> [Optional[ListNode], Optional[ListNode]]:  # newHead, newTail
        if self.getLength(start) < k:
            return start, None

        [1,2,3,4,5,6]

        newHead = None
        newTail = start

        prev = None
        curr = start
        next = None
        for i in range(k):
            next = curr.next

            if i == k - 1:
                newHead = curr
            
            curr.next = prev

            prev = curr
            curr = next

        newTail.next = next
        return newHead, newTail

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = self.getLength(head)

        if length < k:
            return head

        numPods = (length // k) + (1 if length % k > 0 else 0)
        pods = []
        nextStart = head
        for i in range(numPods):
            pods.append(self.reverseSublist(nextStart, k))
            if pods[len(pods) - 1][1]:
                nextStart = pods[len(pods) - 1][1].next

        head = pods[0][0]
        for i in range(numPods - 1):
            if pods[i][1]:
                pods[i][1].next = pods[i + 1][0]

        return head
