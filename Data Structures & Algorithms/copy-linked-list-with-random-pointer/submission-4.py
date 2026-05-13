"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        originalToCopyMap = {}   # original node-ref -> copied node-ref

        curr = head
        while curr:
            if curr not in originalToCopyMap:
                originalToCopyMap[curr] = Node(curr.val)
            
            if curr.next and curr.next not in originalToCopyMap:
                originalToCopyMap[curr.next] = Node(curr.next.val)
            
            if curr.random and curr.random not in originalToCopyMap:
                originalToCopyMap[curr.random] = Node(curr.random.val)

            currCopy = originalToCopyMap[curr]
            if curr.next:
                currCopy.next = originalToCopyMap[curr.next]

            if curr.random:
                currCopy.random = originalToCopyMap[curr.random]

            curr = curr.next

        return originalToCopyMap[head]