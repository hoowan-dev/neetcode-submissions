# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        solution = []

        if not root:
            return solution

        evalNodes = [root]
        while len(evalNodes) > 0:
            levelNodes = evalNodes
            solution.append(levelNodes[-1].val)
            evalNodes = []
            
            for node in levelNodes:
                if node.left:
                    evalNodes.append(node.left)
                if node.right:
                    evalNodes.append(node.right)

        return solution