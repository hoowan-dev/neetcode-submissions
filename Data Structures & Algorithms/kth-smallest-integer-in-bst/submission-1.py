# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def iterate(node: Optional[TreeNode]):
            if iterate.solution != -1:
                return
            
            if node.left:
                iterate(node.left)

            if iterate.iteration == k and iterate.solution == -1:
                iterate.solution = node.val

            iterate.iteration += 1

            if node.right:
                iterate(node.right)

        iterate.iteration = 1
        iterate.solution = -1

        iterate(root)
        return iterate.solution
