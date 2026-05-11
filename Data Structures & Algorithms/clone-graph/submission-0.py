"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        head = Node(node.val, None)
        visited = { node.val : head }   # id of visited node -> new copy of node

        remainingNodes = [node]
        while len(remainingNodes) != 0:
            nextNode = remainingNodes.pop()
            nextNodeCopy = visited[nextNode.val]

            for neighbor in nextNode.neighbors:
                if neighbor.val not in visited:
                    neighborCopy = Node(neighbor.val)
                    visited[neighbor.val] = neighborCopy
                    remainingNodes.append(neighbor)

                nextNodeCopy.neighbors.append(visited[neighbor.val])

        return head
            
