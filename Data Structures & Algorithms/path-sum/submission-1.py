# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root == None:
            return False

        pathStack = [ root ]
        while len(pathStack) != 0:
            leaf = pathStack.pop()
            if leaf.left == None and leaf.right == None and leaf.val == targetSum:
                return True
            
            if leaf.left != None:
                leaf.left.val += leaf.val
                pathStack.append(leaf.left)
            
            if leaf.right != None:
                leaf.right.val += leaf.val
                pathStack.append(leaf.right)

        return False
