# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findDepth(self, node: Optional[TreeNode], currDepth = 0) -> int:
        leftDepth, rightDepth = 0, 0

        if node.left:
            leftDepth = self.findDepth(node.left, currDepth)

        if node.right:
            rightDepth = self.findDepth(node.right, currDepth)

        return max(leftDepth, rightDepth) + 1
        
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.findDepth(root)