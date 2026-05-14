# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        nodeStack = [root]

        while (len(nodeStack) > 0):
            node = nodeStack.pop()
            leftTmp = node.left
            node.left = node.right
            node.right = leftTmp

            if node.left:
                nodeStack.append(node.left)

            if node.right:
                nodeStack.append(node.right)

        return root