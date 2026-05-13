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

        refToNodeCopyMap = {}

        curr = head
        while curr:
            if curr not in refToNodeCopyMap:
                refToNodeCopyMap[curr] = Node(curr.val)
            
            if curr.next and curr.next not in refToNodeCopyMap:
                refToNodeCopyMap[curr.next] = Node(curr.next.val)
            
            if curr.random and curr.random not in refToNodeCopyMap:
                refToNodeCopyMap[curr.random] = Node(curr.random.val)

            currCopy = refToNodeCopyMap[curr]
            if curr.next:
                currCopy.next = refToNodeCopyMap[curr.next]

            if curr.random:
                currCopy.random = refToNodeCopyMap[curr.random]

            curr = curr.next

        return refToNodeCopyMap[head]